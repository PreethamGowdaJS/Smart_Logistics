from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Route, Vehicle, Disruption, Accessibility

router = APIRouter()

@router.get("/routes")
def get_all_routes(db: Session = Depends(get_db)):
    routes = db.query(Route).all()
    return [
        {
            "route_id": r.route_id,
            "source_location_id": r.source_location_id,
            "destination_location_id": r.destination_location_id,
            "distance_km": r.distance_km,
            "estimated_time_min": r.estimated_time_min,
            "road_condition": r.road_condition,
            "route_status": r.route_status,
            "risk_level": r.risk_level
        }
        for r in routes
    ]

@router.get("/vehicles")
def get_all_vehicles(db: Session = Depends(get_db)):
    vehicles = db.query(Vehicle).all()
    return [
        {
            "vehicle_id": v.vehicle_id,
            "vehicle_type": v.vehicle_type,
            "latitude": v.latitude,
            "longitude": v.longitude,
            "speed_kmh": v.speed_kmh,
            "vehicle_status": v.vehicle_status,
            "last_updated": v.last_updated
        }
        for v in vehicles
    ]

@router.get("/disruptions")
def get_all_disruptions(db: Session = Depends(get_db)):
    disruptions = db.query(Disruption).filter(Disruption.status != "Resolved").all()
    return [
        {
            "disruption_id": d.disruption_id,
            "location_id": d.location_id,
            "route_id": d.route_id,
            "disruption_type": d.disruption_type,
            "severity": d.severity,
            "description": d.description,
            "status": d.status,
            "reported_at": d.reported_at
        }
        for d in disruptions
    ]

@router.get("/accessibility")
def get_all_accessibility(db: Session = Depends(get_db)):
    records = db.query(Accessibility).all()
    return [
        {
            "accessibility_id": a.accessibility_id,
            "location_id": a.location_id,
            "road_access_score": a.road_access_score,
            "transport_access_score": a.transport_access_score,
            "risk_score": a.risk_score,
            "overall_accessibility_score": a.overall_accessibility_score,
            "recorded_at": a.recorded_at
        }
        for a in records
    ]