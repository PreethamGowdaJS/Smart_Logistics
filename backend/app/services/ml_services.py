def predict_risk(features: dict) -> float:
    road = features.get("road_condition") or {}
    traffic = features.get("traffic") or {}
    weather = features.get("weather") or {}

    surface_score = road.get("surface_score", 50)
    damage_count = road.get("damage_count", 0)
    congestion_percent = traffic.get("congestion_percent", 0)
    rainfall_mm = weather.get("rainfall_mm", 0)

    risk_score = (
        (100 - surface_score) * 0.4
        + damage_count * 5
        + congestion_percent * 0.3
        + rainfall_mm * 0.5
    )

    return round(min(max(risk_score, 0), 100), 2)

def predict_eta(features: dict, distance_km: float, base_duration: float) -> float:
    traffic = features.get("traffic") or {}
    road = features.get("road_condition") or {}
    weather = features.get("weather") or {}

    delay_factor = traffic.get("delay_factor", 1.0)
    surface_score = road.get("surface_score", 50)
    rainfall_mm = weather.get("rainfall_mm", 0)

    eta = base_duration * delay_factor

    # Add extra delay for poor road conditions
    if surface_score < 50:
        eta *= 1.15

    # Add extra delay during heavy rainfall
    if rainfall_mm > 50:
        eta *= 1.20

    return round(eta, 2)

def calculate_route_score(
    risk_score: float,
    accessibility_score: float,
    distance_km: float,
    eta_minutes: float
) -> float:

    risk_component = 100 - risk_score
    accessibility_component = accessibility_score

    # Lower distance and ETA are better
    distance_component = max(0, 100 - (distance_km / 5))
    eta_component = max(0, 100 - (eta_minutes / 5))

    score = (
        risk_component * 0.35
        + accessibility_component * 0.30
        + distance_component * 0.15
        + eta_component * 0.20
    )

    return round(min(max(score, 0), 100), 2)