from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from app.services.osrm_service import get_route

router = APIRouter()

class LatLng(BaseModel):
    lat: float
    lng: float

class RouteRequest(BaseModel):
    origin: LatLng
    destination: LatLng
    vehicle_type: str = "truck"
    avoid_tolls: bool = False

@router.post("/optimize")
async def optimize_route(req: RouteRequest):
    route = await get_route(
        req.origin.lat,
        req.origin.lng,
        req.destination.lat,
        req.destination.lng
    )
    # TODO: call maps teammate's OSRM/Mapbox service for actual route
    # TODO: call ML service for risk_score
    # Returning mocked shape so frontend/ML can integrate against this NOW
    return {
        "route_geojson": route["route_geojson"],
        "eta_minutes": route["duration_minutes"],
        "risk_score": 0.3,
        "accessibility_score": 0.75,
        "disruptions": []
    }
