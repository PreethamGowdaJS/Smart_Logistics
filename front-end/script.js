/* =====================================================
   NER SMART LOGISTICS
   FRONTEND API CONFIGURATION
===================================================== */


/* =====================================================
   1. BACKEND URL
===================================================== */

/*
   Your backend teammate will give you this URL.

   Example:

   const API_BASE_URL =
       "https://smart-logistics-api.onrender.com";

   For now keep it empty.
*/

const API_BASE_URL = "http://127.0.0.1:8000";


/* =====================================================
   2. API HELPER
===================================================== */

async function apiRequest(endpoint, options = {}) {

    if (!API_BASE_URL) {
        throw new Error("Backend API is not connected yet.");
    }

    const response = await fetch(
        `${API_BASE_URL}${endpoint}`,
        {
            headers: {
                "Content-Type": "application/json",
                ...options.headers
            },
            ...options
        }
    );

    if (!response.ok) {
        throw new Error(
            `API Error: ${response.status}`
        );
    }

    return await response.json();
}


/* =====================================================
   3. DASHBOARD DATA
===================================================== */

async function loadDashboardData() {

    try {

       const routes =
            await apiRequest("/api/database/routes");
        
       const vehicles =
            await apiRequest("/api/database/vehicles");
        
       const disruptions =
            await apiRequest("/api/database/disruptions");

       const accessibilityData =
            await apiRequest("/api/database/accessibility");

        document.getElementById("totalRoutes")
            .textContent =
            routes.length;

        document.getElementById("activeVehicles")
            .textContent =
            vehicles.length;

        document.getElementById("riskAlerts")
            .textContent =
            disruptions.length;
       
        const accessibility =
        accessibilityData.length > 0
           ? Math.round(
                accessibilityData.reduce(
                   (sum, item) => sum + item.overall_accessibility_score,
                   0
                ) / accessibilityData.length
            )
            : null;

        document.getElementById("accessibility")
            .textContent =
            accessibility !== null
                ? `${accessibility}%`
                : "--%";

        document.getElementById("regionalScore")
            .textContent =
            accessibility !== null
                ? `${accessibility}%`
                : "--%";

        if (accessibility !== null) {

            document.getElementById("accessProgress")
                .style.width =
                `${accessibility}%`;

        }

    }

    catch (error) {

        console.log(
            "Dashboard data unavailable:",
            error.message
        );

    }

}


/* =====================================================
   4. ROUTES
===================================================== */

async function loadRoutes() {

    try {

        const routes =
           await apiRequest("/api/database/routes");

        displayRoutes(routes);

    }

    catch (error) {

        console.log(
            "Route data unavailable:",
            error.message
        );

    }

}


/* =====================================================
   DISPLAY ROUTES
===================================================== */

function displayRoutes(routes) {

    const table =
        document.getElementById("routesTable");

    table.innerHTML = "";

    if (!routes || routes.length === 0) {

        table.innerHTML = `
            <tr>
                <td colspan="4">
                    <div class="empty-state">

                        <i class="fa-solid fa-route"></i>

                        <span>No routes available</span>

                        <small>
                            Backend returned no route data
                        </small>

                    </div>
                </td>
            </tr>
        `;

        return;
    }


    routes.slice(0, 5).forEach(route => {

        const row =
            document.createElement("tr");

        row.innerHTML = `

            <td>
                <strong>
                    ${escapeHTML(route.route_id ?? "--")}                </strong>
            </td>

            <td>
                ${escapeHTML(route.route_status ?? "--")}
            </td>

            <td>
                ${escapeHTML(route.risk_level ?? "--")}
            </td>

            <td>
                ${escapeHTML(route.estimated_time_min ?? "--")}min
            </td>

        `;

        table.appendChild(row);

    });

}


/* =====================================================
   5. ROUTE DROPDOWN
===================================================== */

async function loadRouteOptions() {

    try {

        const routes =
          await apiRequest("/api/database/routes");

        const select =
            document.getElementById("affectedRoute");

        routes.forEach(route => {

            const option =
                document.createElement("option");

            option.value =
                route.id;

            option.textContent =
                route.name;

            select.appendChild(option);

        });

    }

    catch (error) {

        console.log(
            "Route options unavailable:",
            error.message
        );

    }

}


/* =====================================================
   6. WHAT-IF SIMULATION
===================================================== */

async function runSimulation() {

    const scenario =
        document.getElementById("scenario").value;

    const route =
        document.getElementById("affectedRoute").value;

    const result =
        document.getElementById("simulationResult");


    if (!scenario || !route) {

        result.innerHTML = `

            <i class="fa-solid fa-circle-exclamation"></i>

            <span>
                Select a scenario and route first.
            </span>

        `;

        return;
    }


    result.innerHTML = `

        <i class="fa-solid fa-spinner fa-spin"></i>

        <span>
            Connecting to simulation engine...
        </span>

    `;


    try {

        const data =
            await apiRequest(
                "/api/simulation",
                {
                    method: "POST",

                    body: JSON.stringify({

                        scenario: scenario,

                        routeId: route

                    })

                }
            );


        result.innerHTML = `

            <i class="fa-solid fa-check-circle"></i>

            <span>
                ${escapeHTML(
                    data.message ??
                    "Simulation completed."
                )}
            </span>

        `;

    }

    catch (error) {

        result.innerHTML = `

            <i class="fa-solid fa-circle-info"></i>

            <span>
                Simulation backend is not connected yet.
            </span>

        `;

    }

}


/* =====================================================
   7. AI ANALYSIS
===================================================== */

async function loadAIInsights() {

    try {

        const data =
          await apiRequest(
             "/api/route/optimize",
                {
                   method: "POST",
                   body: JSON.stringify({
                    origin: {
                    lat: 26.1445,
                    lng: 91.7362
                   },
                   destination: {
                    lat: 25.5788,
                    lng: 91.8933
                   },
                   vehicle_type: "truck",
                   avoid_tolls: false
                   })
                }
            );

        console.log(
            "AI Insights:",
            data
        );

        /*
           Later you can display:

           data.risk
           data.recommendation
           data.confidence
        */
       document.getElementById("aiRisk").textContent =
           `${data.risk_score}%`;

        const riskLevel =
           data.risk_score >= 70
              ? "High Risk"
              : data.risk_score >= 40
              ? "Medium Risk"
              : "Low Risk";

       console.log("Risk Level:", riskLevel);
       document.getElementById("aiRiskLevel").textContent = riskLevel;
       document.getElementById("aiAccessibility").textContent =
           `${data.accessibility_score}%`;

       document.getElementById("aiRouteScore").textContent =
           `${data.route_score}/100`;

       document.getElementById("aiEta").textContent =
            `${data.eta_minutes} min`;

        document.getElementById("aiRecommendation").textContent =
           data.route_score >= 60
              ? "Recommended Route"
              : "Use Caution";

    }

    catch (error) {

        console.log(
            "AI backend unavailable:",
            error.message
        );

    }

}


/* =====================================================
   8. NAVIGATION
===================================================== */

const navLinks =
    document.querySelectorAll(".nav-link");


navLinks.forEach(link => {

    link.addEventListener(
        "click",
        function () {

            navLinks.forEach(
                item =>
                    item.classList.remove("active")
            );

            this.classList.add("active");

        }
    );

});


/* =====================================================
   9. AI BUTTON
===================================================== */

document
    .getElementById("aiAnalysisBtn")
    .addEventListener(
        "click",
        loadAIInsights
    );


/* =====================================================
   10. SIMULATION BUTTON
===================================================== */

document
    .getElementById("simulateBtn")
    .addEventListener(
        "click",
        runSimulation
    );


/* =====================================================
   11. SECURITY
===================================================== */

function escapeHTML(value) {

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}


/* =====================================================
   12. INITIALIZE
===================================================== */
let map;
let routeLayer;

document.addEventListener("DOMContentLoaded", function () {
    loadDashboardData();
    loadRoutes();
    loadRouteOptions();
    loadLocationOptions();
    loadAIInsights();
    initializeMap();
    loadRouteBetween(
        { lat: 26.1445, lng: 91.7362 },
        { lat: 25.5788, lng: 91.8933 }
    );
});

function initializeMap() {
    map = L.map("mapContainer").setView([25.8, 93.5], 6);

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: "&copy; OpenStreetMap contributors",
        noWrap: true
    }).addTo(map);
}
async function loadRouteBetween(origin, destination) {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/api/route/optimize",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    origin: origin,
                    destination: destination,
                    vehicle_type: "truck",
                    avoid_tolls: false
                })
            }
        );

        if (!response.ok) {
            throw new Error("Route API failed");
        }

        const data = await response.json();

        console.log("Route data:", data);

        document.getElementById("routeDistance").textContent =
            `${data.distance_km} km`;

        document.getElementById("routeEta").textContent =
            `${data.eta_minutes} min`;

        if (routeLayer) {
            map.removeLayer(routeLayer);
        }

        routeLayer = L.geoJSON(data.route_geojson).addTo(map);

        map.fitBounds(routeLayer.getBounds());

        console.log("Distance:", data.distance_km, "km");
        console.log("ETA:", data.eta_minutes, "minutes");

    } catch (error) {

        console.error("Route loading failed:", error);

    }
}

 
/* =====================================================
   LOCATION SELECTOR
===================================================== */

let allLocations = [];

async function loadLocationOptions() {
    try {
        allLocations = await apiRequest("/api/locations");

        const originSelect = document.getElementById("originSelect");
        const destinationSelect = document.getElementById("destinationSelect");

        allLocations.forEach(loc => {
            const label = `${loc.city}, ${loc.state}`;

            const originOption = document.createElement("option");
            originOption.value = loc.location_id;
            originOption.textContent = label;
            originSelect.appendChild(originOption);

            const destOption = document.createElement("option");
            destOption.value = loc.location_id;
            destOption.textContent = label;
            destinationSelect.appendChild(destOption);
        });
    } catch (error) {
        console.log("Location options unavailable:", error.message);
    }
}

function getLocationById(id) {
    return allLocations.find(loc => loc.location_id === id);
}

async function findRouteFromSelection() {
    const originId = document.getElementById("originSelect").value;
    const destinationId = document.getElementById("destinationSelect").value;

    if (!originId || !destinationId) {
        alert("Please select both origin and destination.");
        return;
    }

    if (originId === destinationId) {
        alert("Origin and destination must be different.");
        return;
    }

    const originLoc = getLocationById(originId);
    const destLoc = getLocationById(destinationId);

    if (!originLoc || !destLoc) {
        console.log("Could not find selected locations.");
        return;
    }

    await loadRouteBetween(
        { lat: originLoc.latitude, lng: originLoc.longitude },
        { lat: destLoc.latitude, lng: destLoc.longitude }
    );
}

document.getElementById("findRouteBtn")
    .addEventListener("click", findRouteFromSelection);

