import httpx

OSRM_BASE_URL = "https://router.project-osrm.org"


async def get_route(origin_lat, origin_lng, dest_lat, dest_lng):

    url = (
        f"{OSRM_BASE_URL}/route/v1/driving/"
        f"{origin_lng},{origin_lat};"
        f"{dest_lng},{dest_lat}"
        f"?overview=full&geometries=geojson"
    )

    async with httpx.AsyncClient(timeout=20.0) as client:
        response = await client.get(url)

    response.raise_for_status()

    data = response.json()

    if not data.get("routes"):
        raise ValueError("No route found")

    route = data["routes"][0]

    return {
        "distance_km": round(route["distance"] / 1000, 2),
        "duration_minutes": round(route["duration"] / 60, 2),
        "route_geojson": route["geometry"]
    }