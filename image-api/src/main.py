from fastapi import FastAPI, File, UploadFile
from typing import List
from datetime import datetime

app = FastAPI()

# Lista de imágenes
images = []

# Registro de logs
logs = []

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # Leemos el contenido del archivo y lo guardamos internamente junto con el nombre del archivo
    content = await file.read()
    images.append({"filename": file.filename, "content": content})
    
    # Escribimos un registro de log
    log_message = f"{datetime.now()} - Se ha cargado la imagen: {file.filename}"
    logs.append(log_message)
    
    return {"message": "Imagen cargada exitosamente"}

@app.get("/images/")
async def list_images():
    # Escribimos un registro de log
    log_message = f"{datetime.now()} - Se ha consultado el listado de imágenes"
    logs.append(log_message)
    
    # Devolvemos el listado de nombres de archivos de las imágenes
    return {"images": [image["filename"] for image in images]}

@app.get("/image/{image_id}")
async def get_image(image_id: int):
    if 0 <= image_id < len(images):
        # Escribimos un registro de log
        log_message = f"{datetime.now()} - Se ha consultado la imagen: {images[image_id]['filename']}"
        logs.append(log_message)
        
        # Devolvemos los datos binarios de la imagen directamente
        return images[image_id]["content"]
    else:
        # Escribimos un registro de log
        log_message = f"{datetime.now()} - No se encontró la imagen con el ID: {image_id}"
        logs.append(log_message)
        
        return {"error": "Image not found"}

@app.get("/logs/")
async def get_logs():
    # Escribimos un registro de log
    log_message = f"{datetime.now()} - Se ha consultado el registro de logs"
    logs.append(log_message)
    
    # Devolvemos el registro de logs
    return {"logs": logs}