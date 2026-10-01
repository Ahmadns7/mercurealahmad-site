from fastapi import FastAPI, Request
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="WABot — WhatsApp AI Gateway", version="1.0.0")

@app.get("/")
def health():
    return {"status": "WABot running on Oracle Free Tier", "brand": "MercuReal"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    # TODO: classify intent, query DB, generate AI reply
    return {"status": "received", "message": "Hello from WABot — built for Kano SMBs."}
