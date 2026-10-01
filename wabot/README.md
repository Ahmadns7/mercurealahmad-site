# WABot — WhatsApp AI Gateway (MercuReal)

FastAPI webhook endpoint for Meta WhatsApp Business API.
Connects to Oracle Free Tier VM + Autonomous DB.

## Deploy (Oracle Free Tier)
- VM: AMD 1/8 OCPU, 1 GB RAM (Always Free) — runs FastAPI + webhook
- DB: Oracle Autonomous DB 20 GB (Always Free) — business profiles, message logs
- Storage: Object Storage 10 GB (Always Free) — media files
- Domain: `wabot.mercureal.ng` or `wabot.ng` (register ~$10/yr)
- SSL: Let's Encrypt

## Quick Start
1. Set `META_WABA_TOKEN` and `META_PHONE_NUMBER_ID` in `.env`.
2. `pip install -r requirements.txt`
3. `uvicorn main:app --host 0.0.0.0 --port 8000`
4. Point Meta webhook URL to `https://your-domain/webhook`

## Revenue
- Starter: ₦39,000/mo ($24) — 1 WA number, basic workflow, 500 msg/mo.
- Business: ₦79,000/mo ($48) — 2 numbers, AI dynamic replies, analytics.
- Setup: ₦49,000 ($30) — connect + 2 workflows.

First customer: use +234 708 394 7529 for demo; text 5 closest SMBs; 7-day trial.
