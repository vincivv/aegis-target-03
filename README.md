# aegis-target-03 · inventory service

Flask inventory API with stock reservations.

Monitored by [AEGIS](https://github.com/vincivv): every push to this repo is scanned autonomously by an AEGIS sentinel agent.

## Run

```bash
pip install -r requirements.txt && python app.py
```

## Routes

- `GET /health`
- `GET /items`
- `GET /items/<sku>`
- `POST /items/<sku>/reserve {qty}`
