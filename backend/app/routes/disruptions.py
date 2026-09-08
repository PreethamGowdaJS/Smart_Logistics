from fastapi import APIRouter, Query

router = APIRouter()

@router.get("")
def get_disruptions(region: str = Query(...)):
    # TODO: wire to weather API + ML risk model
    return {
        "region": region,
        "alerts": [
            {"type": "fog", "severity": "medium", "lat": 30.9, "lng": 76.8}
        ]
    }
