from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.osrm_service import get_route
from app.services.feature_service import fetch_route_features

router = APIRouter()


class LatLng(BaseModel):
    lat: float
    lng: float


class RouteRequest(BaseModel):
    origin: LatLng
    destination: LatLng
    vehicle_type: str = "truck"
    avoid_tolls: bool = False


def calculate_scores(features: dict) -> dict:
    road_condition = features.get("road_condition") or {}
    traffic = features.get("traffic") or {}
    weather = features.get("weather") or {}
    accessibility = features.get("accessibility") or {}

    surface_score = road_condition.get("surface_score", 50)
    damage_count = road_condition.get("damage_count", 0)
    congestion_percent = traffic.get("congestion_percent", 0)
    rainfall_mm = weather.get("rainfall_mm", 0)

    risk_score = (100 - surface_score) * 0.4 + damage_count * 5 + congestion_percent * 0.3 + rainfall_mm * 0.5
    risk_score = round(min(max(risk_score, 0), 100), 2)

    road_access_score = accessibility.get("road_access_score", 50)
    transport_access_score = accessibility.get("transport_access_score", 50)
    accessibility_score = round((road_access_score + transport_access_score) / 2, 2)

    return {"risk_score": risk_score, "accessibility_score": accessibility_score}


@router.post("/optimize")
async def optimize_route(req: RouteRequest, db: Session = Depends(get_db)):

    route = await get_route(
        req.origin.lat,
        req.origin.lng,
        req.destination.lat,
        req.destination.lng
    )

    features = fetch_route_features(
        db,
        req.origin.lat,
        req.origin.lng,
        req.destination.lat,
        req.destination.lng
    )

    scores = calculate_scores(features)

    return {
        "route_geojson": route["route_geojson"],
        "distance_km": route["distance_km"],
        "eta_minutes": route["duration_minutes"],
        "risk_score": scores["risk_score"],
        "accessibility_score": scores["accessibility_score"],
        "disruptions": features["disruptions"]
    }