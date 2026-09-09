from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import (
    Location,
    Route,
    Traffic,
    Weather,
    RoadCondition,
    Disruption,
    Accessibility,
    Vehicle,
)

router = APIRouter()


@router.get("/locations")
def get_locations(db: Session = Depends(get_db)):
    locations = db.query(Location).all()

    return [
        {
            "location_id": x.location_id,
            "city": x.city,
            "state": x.state,
            "latitude": x.latitude,
            "longitude": x.longitude,
            "location_type": x.location_type,
        }
        for x in locations
    ]


@router.get("/routes")
def get_routes(db: Session = Depends(get_db)):
    routes = db.query(Route).all()

    return [
        {
            "route_id": x.route_id,
            "source_location_id": x.source_location_id,
            "destination_location_id": x.destination_location_id,
            "distance_km": x.distance_km,
            "estimated_time_min": x.estimated_time_min,
            "road_condition": x.road_condition,
            "route_status": x.route_status,
            "risk_level": x.risk_level,
        }
        for x in routes
    ]


@router.get("/traffic")
def get_traffic(db: Session = Depends(get_db)):
    traffic = db.query(Traffic).all()

    return [
        {
            "traffic_id": x.traffic_id,
            "route_id": x.route_id,
            "congestion_percent": x.congestion_percent,
            "congestion_level": x.congestion_level,
            "delay_factor": x.delay_factor,
            "recorded_at": x.recorded_at,
        }
        for x in traffic
    ]


@router.get("/weather")
def get_weather(db: Session = Depends(get_db)):
    weather = db.query(Weather).all()

    return [
        {
            "weather_id": x.weather_id,
            "location_id": x.location_id,
            "temperature_c": x.temperature_c,
            "rainfall_mm": x.rainfall_mm,
            "humidity_percent": x.humidity_percent,
            "weather_condition": x.weather_condition,
            "recorded_at": x.recorded_at,
        }
        for x in weather
    ]


@router.get("/road-conditions")
def get_road_conditions(db: Session = Depends(get_db)):
    conditions = db.query(RoadCondition).all()

    return [
        {
            "road_condition_id": x.road_condition_id,
            "route_id": x.route_id,
            "surface_score": x.surface_score,
            "drainage_score": x.drainage_score,
            "damage_count": x.damage_count,
            "condition_status": x.condition_status,
            "updated_at": x.updated_at,
        }
        for x in conditions
    ]


@router.get("/disruptions")
def get_disruptions(db: Session = Depends(get_db)):
    disruptions = db.query(Disruption).all()

    return [
        {
            "disruption_id": x.disruption_id,
            "location_id": x.location_id,
            "route_id": x.route_id,
            "disruption_type": x.disruption_type,
            "severity": x.severity,
            "description": x.description,
            "status": x.status,
            "reported_at": x.reported_at,
        }
        for x in disruptions
    ]


@router.get("/accessibility")
def get_accessibility(db: Session = Depends(get_db)):
    accessibility = db.query(Accessibility).all()

    return [
        {
            "accessibility_id": x.accessibility_id,
            "location_id": x.location_id,
            "road_access_score": x.road_access_score,
            "transport_access_score": x.transport_access_score,
            "risk_score": x.risk_score,
            "overall_accessibility_score": x.overall_accessibility_score,
            "recorded_at": x.recorded_at,
        }
        for x in accessibility
    ]


@router.get("/vehicles")
def get_vehicles(db: Session = Depends(get_db)):
    vehicles = db.query(Vehicle).all()

    return [
        {
            "vehicle_id": x.vehicle_id,
            "vehicle_type": x.vehicle_type,
            "latitude": x.latitude,
            "longitude": x.longitude,
            "speed_kmh": x.speed_kmh,
            "vehicle_status": x.vehicle_status,
            "last_updated": x.last_updated,
        }
        for x in vehicles
    ]