# Backend — Smart Logistics API

## Run locally
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Visit `http://localhost:8000/docs` for interactive Swagger UI — share this URL with
frontend/ML teammates so they can test endpoints without asking you.

## Endpoints (see /docs/api-contracts.md for full contract)
- `POST /api/route/optimize`
- `GET  /api/disruptions?region=X`
- `POST /api/accessibility/score`

All currently return mocked data matching the agreed contract shape.
Replace TODOs in each route file as DB/ML/Maps integrations come online.
