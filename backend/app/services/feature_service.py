from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.models import (
    Location,
    Route,
    Traffic,
    Weather,
    RoadCondition,
    Disruption,
    Accessibility,
)


def _nearest_location(db: Session, lat: float, lng: float):
    """Find the closest known location to a lat/lng point."""
    return (
        db.query(Location)
        .order_by(
            func.pow(Location.latitude - lat, 2)
            + func.pow(Location.longitude - lng, 2)
        )
        .first()
    )


def fetch_route_features(
    db: Session,
    origin_lat: float,
    origin_lng: float,
    dest_lat: float,
    dest_lng: float,
) -> dict:
    """
    Finds the closest known locations to origin/destination, then pulls
    road condition, traffic, weather, accessibility, and disruptions
    for that trip from the database.
    """

    origin_loc = _nearest_location(db, origin_lat, origin_lng)
    dest_loc = _nearest_location(db, dest_lat, dest_lng)

    route = None
    road_condition = None
    traffic = None
    disruptions = []

    if origin_loc and dest_loc:
        route = (
            db.query(Route)
            .filter(
                (
                    (Route.source_location_id == origin_loc.location_id)
                    & (Route.destination_location_id == dest_loc.location_id)
                )
                | (
                    (Route.source_location_id == dest_loc.location_id)
                    & (Route.destination_location_id == origin_loc.location_id)
                )
            )
            .first()
        )

        if route:
            road_condition = (
                db.query(RoadCondition)
                .filter(RoadCondition.route_id == route.route_id)
                .first()
            )
            traffic = (
                db.query(Traffic)
                .filter(Traffic.route_id == route.route_id)
                .first()
            )
            disruptions = (
                db.query(Disruption)
                .filter(
                    Disruption.route_id == route.route_id,
                    Disruption.status != "Resolved",
                )
                .all()
            )

    weather = None
    accessibility = None
    if dest_loc:
        weather = (
            db.query(Weather)
            .filter(Weather.location_id == dest_loc.location_id)
            .order_by(Weather.recorded_at.desc())
            .first()
        )
        accessibility = (
            db.query(Accessibility)
            .filter(Accessibility.location_id == dest_loc.location_id)
            .first()
        )

    return {
        "route_id": route.route_id if route else None,
        "road_condition": {
            "surface_score": road_condition.surface_score,
            "drainage_score": road_condition.drainage_score,
            "damage_count": road_condition.damage_count,
            "condition_status": road_condition.condition_status,
        } if road_condition else None,
        "traffic": {
            "congestion_percent": traffic.congestion_percent,
            "congestion_level": traffic.congestion_level,
            "delay_factor": traffic.delay_factor,
        } if traffic else None,
        "weather": {
            "temperature_c": weather.temperature_c,
            "rainfall_mm": weather.rainfall_mm,
            "humidity_percent": weather.humidity_percent,
            "weather_condition": weather.weather_condition,
        } if weather else None,
        "accessibility": {
            "road_access_score": accessibility.road_access_score,
            "transport_access_score": accessibility.transport_access_score,
            "risk_score": accessibility.risk_score,
            "overall_accessibility_score": accessibility.overall_accessibility_score,
        } if accessibility else None,
        "disruptions": [
            {
                "disruption_type": d.disruption_type,
                "severity": d.severity,
                "description": d.description,
                "status": d.status,
            }
            for d in disruptions
        ],
    }
