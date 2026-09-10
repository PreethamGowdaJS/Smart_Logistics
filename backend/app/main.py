from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import route_optimize, disruptions, accessibility, locations, routes_list , simulation

app = FastAPI(title="Smart Logistics API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(route_optimize.router, prefix="/api/route", tags=["route"])
app.include_router(disruptions.router, prefix="/api/disruptions", tags=["disruptions"])
app.include_router(accessibility.router, prefix="/api/accessibility", tags=["accessibility"])
app.include_router(locations.router, prefix="/api/locations", tags=["locations"])
app.include_router(routes_list.router, prefix="/api/database", tags=["database"])
app.include_router(simulation.router, prefix="/api/simulation", tags=["simulation"])

@app.get("/")
def health():
    return {"status": "ok", "service": "smart-logistics-backend"}