
import time
import cv2
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import numpy as np
from PIL import Image

import config
import inference


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}



@app.post("/{style}")
async def get_image(style: str, file: UploadFile = File(...)):
    image = np.array(Image.open(file.file))
    model = config.STYLES[style]
    start = time.time()
    output, resized = inference.inference(model, image)
    # save the styled image to a local disc
    name = f"D:/YASS.jpg"
    print(f"name: {name}")
    cv2.imwrite(name, output)
    models = config.STYLES.copy()
    del models[style]
    return {"name": name, "time": time.time() - start}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
