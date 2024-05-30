from fastapi import FastAPI
from roku.enums import Power
import roku.const
import os

from roku.ecp import Device

app = FastAPI()

host = os.environ["HOST"]
port = os.environ["PORT"] = "8060"

rokuDevice = Device(host, port)


@app.get("/")
async def root():
    return {"message": "Roku Controller"}


@app.get("/power")
async def power():
    return {"power": "On"}


@app.get("/power/{z}")
async def power(z: Power):
    return {"power": rokuDevice.press_key(z.value)}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
