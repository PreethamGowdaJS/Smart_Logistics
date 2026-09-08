from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import route_optimize, disruptions, accessibility

app = FastAPI(title="Smart Logistics API")

# Wide open CORS for hackathon speed — frontend can hit this from anywhere
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(route_optimize.router, prefix="/api/route", tags=["route"])
app.include_router(disruptions.router, prefix="/api/disruptions", tags=["disruptions"])
app.include_router(accessibility.router, prefix="/api/accessibility", tags=["accessibility"])

@app.get("/")
def health():
    return {"status": "ok", "service": "smart-logistics-backend"}
