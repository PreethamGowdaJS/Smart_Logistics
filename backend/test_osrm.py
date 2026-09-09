import asyncio

from app.services.osrm_service import get_route


async def main():
    # Guwahati
    origin_lat = 26.1445
    origin_lng = 91.7362

    # Shillong
    dest_lat = 25.5788
    dest_lng = 91.8933

    route = await get_route(
        origin_lat,
        origin_lng,
        dest_lat,
        dest_lng
    )

    print("Route found!")
    print("Distance:", route["distance_km"], "km")
    print("Duration:", route["duration_minutes"], "minutes")
    print("Geometry received:", bool(route["route_geojson"]))


asyncio.run(main())