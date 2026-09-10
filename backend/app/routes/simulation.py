from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SimulationRequest(BaseModel):
    scenario: str
    routeId: str

@router.post("")
def run_simulation(req: SimulationRequest):
    # Simple rule-based simulation for now — can be upgraded to
    # actually re-run risk scoring with adjusted weather/traffic inputs
    scenario_messages = {
        "heavy_rain": "Simulated heavy rainfall increases risk by ~25% and ETA by ~20% on this route.",
        "landslide": "Simulated landslide risk renders this route high-risk; alternate route recommended.",
        "festival_traffic": "Simulated festival congestion adds approximately 30 minutes to ETA.",
    }

    message = scenario_messages.get(
        req.scenario,
        f"Simulated '{req.scenario}' scenario applied to route {req.routeId}."
    )

    return {"message": message, "scenario": req.scenario, "routeId": req.routeId}