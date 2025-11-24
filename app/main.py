from fastapi import FastAPI, File, UploadFile, HTTPException
from prediction_engine import engine
import uvicorn

app = FastAPI(title="Animal Faces Classifier API 🦁")

@app.get("/")
def home():
    return {"message": "Server is Running! Go to /docs to test."}

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")
    try:
        content = await file.read()
        result = engine.predict(content)
        result["filename"] = file.filename
        return result
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)