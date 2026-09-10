from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Location

router = APIRouter()

@router.get("")
def get_locations(db: Session = Depends(get_db)):
    locations = db.query(Location).all()
    return [
        {
            "location_id": loc.location_id,
            "city": loc.city,
            "state": loc.state,
            "latitude": loc.latitude,
            "longitude": loc.longitude,
            "location_type": loc.location_type
        }
        for loc in locations
    ]