from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AccessibilityRequest(BaseModel):
    location_id: str

@router.post("/score")
def get_accessibility_score(req: AccessibilityRequest):
    # TODO: pull from DB once accessibility table is ready
    return {
        "location_id": req.location_id,
        "wheelchair_access": True,
        "ramp_present": False,
        "score": 0.6
    }
