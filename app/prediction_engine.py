import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os
from tensorflow.keras import layers, models, regularizers

# =========================================================
# Dynamic Path Configuration
# =========================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "animal_faces_ultimate.keras")
CLASS_NAMES_PATH = os.path.join(BASE_DIR, "models", "class_names.txt")
IMG_SIZE = (224, 224)

class ModelEngine:
    def __init__(self):
        self.model = None
        self.class_names = []
        
        # 1. Load class names first
        self._load_class_names()
        
        # 2. Build architecture and load weights
        self._build_and_load_model()

    def _load_class_names(self):
        """Loads class labels from the text file."""
        if os.path.exists(CLASS_NAMES_PATH):
            with open(CLASS_NAMES_PATH, "r") as f:
                self.class_names = [line.strip() for line in f.readlines()]
            print(f"✅ Class names loaded: {self.class_names}")
        else:
            raise FileNotFoundError(f"❌ Class names file not found at: {CLASS_NAMES_PATH}")

    def _build_and_load_model(self):
        """
        Robust Solution: Manually reconstructs the model architecture and loads weights only.
        This resolves Keras version mismatches between the training environment (Kaggle) 
        and the local environment.
        """
        print("🏗️ Rebuilding model architecture manually...")
        
        try:
            num_classes = len(self.class_names)
            
            # --- 1. Redefine Architecture (Must match training code exactly) ---
            data_augmentation = models.Sequential([
                layers.RandomFlip("horizontal"),
                layers.RandomRotation(0.1),
                layers.RandomZoom(0.1),
                layers.RandomContrast(0.2),    
                layers.RandomBrightness(0.2),  
            ])

            base_model = tf.keras.applications.MobileNetV2(
                input_shape=(224, 224, 3),
                include_top=False,
                weights=None # No need for ImageNet weights, we load our own
            )
            
            # Since we are loading trained weights, trainable status is less critical here, but for consistency:
            base_model.trainable = True 

            # Assemble the model
            self.model = models.Sequential([
                layers.Input(shape=(224, 224, 3)),
                data_augmentation,
                layers.Rescaling(1./127.5, offset=-1),
                base_model,
                layers.GlobalAveragePooling2D(), # 👈 Explicitly defined to prevent layer mismatch
                layers.Dropout(0.3),
                layers.Dense(num_classes, 
                             activation='softmax',
                             kernel_regularizer=regularizers.l2(0.001)) 
            ])
            
            print("⚖️ Loading trained weights...")
            
            # --- 2. Load Weights from File ---
            if os.path.exists(MODEL_PATH):
                # Using load_weights is safer than load_model across versions
                self.model.load_weights(MODEL_PATH)
                print("✅ Model successfully initialized (Weights Loaded).")
            else:
                raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")

        except Exception as e:
            print(f"❌ Error constructing the model: {e}")
            raise e

    def preprocess_image(self, image_bytes):
        """Converts raw bytes to a processed numpy array."""
        try:
            img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
            img = img.resize(IMG_SIZE)
            img_array = np.array(img)
            img_array = np.expand_dims(img_array, axis=0)
            return img_array
        except Exception as e:
            raise ValueError(f"Error processing image: {e}")

    def predict(self, image_bytes):
        """Main prediction logic."""
        processed_img = self.preprocess_image(image_bytes)
        predictions = self.model.predict(processed_img)
        predicted_idx = np.argmax(predictions[0])
        predicted_label = self.class_names[predicted_idx]
        confidence = float(np.max(predictions[0]))
        
        return {
            "prediction": predicted_label,
            "confidence": round(confidence * 100, 2),
            "details": {cls: float(score) for cls, score in zip(self.class_names, predictions[0])}
        }

# Initialize engine
engine = ModelEngine()