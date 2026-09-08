from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

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
def optimize_route(req: RouteRequest):
    # TODO: call maps teammate's OSRM/Mapbox service for actual route
    # TODO: call ML service for risk_score
    # Returning mocked shape so frontend/ML can integrate against this NOW
    return {
        "route_geojson": {"type": "LineString", "coordinates": [
            [req.origin.lng, req.origin.lat],
            [req.destination.lng, req.destination.lat]
        ]},
        "eta_minutes": 120,
        "risk_score": 0.3,
        "accessibility_score": 0.75,
        "disruptions": []
    }
