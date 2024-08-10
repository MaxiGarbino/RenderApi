from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/predict/")
async def predict_image(image: UploadFile = File(...)):
    # Aquí podrías agregar el procesamiento de la imagen para detección de melanoma
    # Por ahora, devolvemos un string fijo.
    return {"result": "Melanoma"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
