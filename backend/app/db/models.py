from sqlalchemy import Column, String, Integer, Float, Date, DateTime
from app.db.database import Base


class Location(Base):
    __tablename__ = "locations"

    location_id = Column(String(10), primary_key=True)
    city = Column(String(100))
    state = Column(String(100))
    latitude = Column(Float)
    longitude = Column(Float)
    location_type = Column(String(50))


class Route(Base):
    __tablename__ = "routes"

    route_id = Column(String(10), primary_key=True)
    source_location_id = Column(String(10))
    destination_location_id = Column(String(10))
    distance_km = Column(Float)
    estimated_time_min = Column(Integer)
    road_condition = Column(String(50))
    route_status = Column(String(50))
    risk_level = Column(String(20))


class Accessibility(Base):
    __tablename__ = "accessibility"

    accessibility_id = Column(String(10), primary_key=True)
    location_id = Column(String(10))
    road_access_score = Column(Integer)
    transport_access_score = Column(Integer)
    risk_score = Column(Integer)
    overall_accessibility_score = Column(Integer)
    recorded_at = Column(DateTime)


class Disruption(Base):
    __tablename__ = "disruptions"

    disruption_id = Column(String(10), primary_key=True)
    location_id = Column(String(10))
    route_id = Column(String(10))
    disruption_type = Column(String(50))
    severity = Column(String(20))
    description = Column(String(255))
    status = Column(String(50))
    reported_at = Column(DateTime)


class Traffic(Base):
    __tablename__ = "traffic"

    traffic_id = Column(String(10), primary_key=True)
    route_id = Column(String(10))
    congestion_percent = Column(Float)
    congestion_level = Column(String(20))
    delay_factor = Column(Float)
    recorded_at = Column(DateTime)


class Weather(Base):
    __tablename__ = "weather"

    weather_id = Column(String(10), primary_key=True)
    location_id = Column(String(10))
    temperature_c = Column(Float)
    rainfall_mm = Column(Float)
    humidity_percent = Column(Float)
    weather_condition = Column(String(50))
    recorded_at = Column(DateTime)


class RoadCondition(Base):
    __tablename__ = "road_conditions"

    road_condition_id = Column(String(10), primary_key=True)
    route_id = Column(String(10))
    surface_score = Column(Integer)
    drainage_score = Column(Integer)
    damage_count = Column(Integer)
    condition_status = Column(String(50))
    updated_at = Column(DateTime)


class Logistics(Base):
    __tablename__ = "logistics"

    shipment_id = Column(String(10), primary_key=True)
    source_location_id = Column(String(10))
    destination_location_id = Column(String(10))
    cargo_type = Column(String(100))
    weight_kg = Column(Float)
    priority = Column(String(20))
    shipment_status = Column(String(50))
    planned_date = Column(Date)


class Vehicle(Base):
    __tablename__ = "vehicles"

    vehicle_id = Column(String(10), primary_key=True)
    vehicle_type = Column(String(50))
    latitude = Column(Float)
    longitude = Column(Float)
    speed_kmh = Column(Float)
    vehicle_status = Column(String(50))
    last_updated = Column(DateTime)


class Facility(Base):
    __tablename__ = "facilities"

    facility_id = Column(String(10), primary_key=True)
    facility_name = Column(String(100))
    facility_type = Column(String(50))
    location_id = Column(String(10))
    latitude = Column(Float)
    longitude = Column(Float)
    capacity = Column(Integer)
    accessibility_score = Column(Integer)
    status = Column(String(50))


class PublicTransport(Base):
    __tablename__ = "public_transport"

    transport_id = Column(String(10), primary_key=True)
    source_location_id = Column(String(10))
    destination_location_id = Column(String(10))
    transport_mode = Column(String(50))
    availability = Column(String(50))
    frequency_per_day = Column(Integer)
    status = Column(String(50))


class Alert(Base):
    __tablename__ = "alerts"

    alert_id = Column(String(10), primary_key=True)
    location_id = Column(String(10))
    route_id = Column(String(10))
    alert_type = Column(String(50))
    severity = Column(String(20))
    message = Column(String(255))
    alert_status = Column(String(50))
    created_at = Column(DateTime)


class DataQuality(Base):
    __tablename__ = "data_quality"

    quality_id = Column(String(10), primary_key=True)
    table_name = Column(String(100))
    validation_rule = Column(String(255))
    missing_value_check = Column(String(50))
    duplicate_check = Column(String(50))
    validity_status = Column(String(20))
    last_checked = Column(Date)


class DataSource(Base):
    __tablename__ = "data_sources"

    source_id = Column(String(10), primary_key=True)
    provider = Column(String(100))
    dataset_name = Column(String(150))
    source_type = Column(String(50))
    purpose = Column(String(150))
    reference = Column(String(255))
    last_updated = Column(String(100))