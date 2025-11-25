from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from prediction_engine import engine
import uvicorn
import os

# ========================================================
# App Initialization
# ========================================================
app = FastAPI(title="Animal Faces Classifier AI 🦁")

# ========================================================
# 1. Prediction Endpoint (API)
# Note: Defined first to ensure priority over static routes.
# ========================================================
@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    """
    Receives an uploaded image, processes it, and returns the classification result.
    """
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image (JPG or PNG).")
    
    try:
        # Read file content
        file_content = await file.read()
        
        # Send to prediction engine
        result = engine.predict(file_content)
        
        # Attach filename to response
        result["filename"] = file.filename
        
        return result

    except Exception as e:
        # Handle unexpected errors
        return {"error": f"Internal Server Error: {str(e)}"}

# ========================================================
# 2. Root Endpoint (Serves the Frontend)
# ========================================================
@app.get("/")
async def read_index():
    """
    Serves the index.html file when the user visits the root URL.
    """
    # Ensure the file exists
    file_path = os.path.join("static", "index.html")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        return {"error": "Frontend file (index.html) not found in 'static' folder!"}

# ========================================================
# 3. Mount Static Files (CSS / JS)
# ========================================================
# Allows the browser to access style.css and script.js via /static/...
# Note: In your HTML, link files like this: <link href="/static/style.css">
app.mount("/static", StaticFiles(directory="static"), name="static")

# ========================================================
# Main Execution
# ========================================================
if __name__ == "__main__":
    print("🚀 Server is starting... Please wait.")
    print("🌍 Open your browser at: http://localhost:8000")
    
    # Run server on port 8000 with auto-reload enabled
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)