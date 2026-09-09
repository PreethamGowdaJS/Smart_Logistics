--
-- PostgreSQL database dump
--

\restrict 3k9PM9Soc1SvxHVdKowc2v1Eh8fcGVljrWF2fJMDaKBRjdKKOPOqHL07Pg0XUSf

-- Dumped from database version 18.6
-- Dumped by pg_dump version 18.6

-- Started on 2026-09-09 13:39:45

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 228 (class 1259 OID 16439)
-- Name: accessibility; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.accessibility (
    accessibility_id character varying(10) NOT NULL,
    location_id character varying(10),
    road_access_score integer,
    transport_access_score integer,
    risk_score integer,
    overall_accessibility_score integer,
    recorded_at timestamp without time zone
);


ALTER TABLE public.accessibility OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 16451)
-- Name: alerts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alerts (
    alert_id character varying(10) NOT NULL,
    location_id character varying(10),
    route_id character varying(10),
    alert_type character varying(50),
    severity character varying(20),
    message character varying(255),
    alert_status character varying(50),
    created_at timestamp without time zone
);


ALTER TABLE public.alerts OWNER TO postgres;

--
-- TOC entry 232 (class 1259 OID 16465)
-- Name: data_quality; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.data_quality (
    quality_id character varying(10) NOT NULL,
    table_name character varying(100),
    validation_rule character varying(255),
    missing_value_check character varying(50),
    duplicate_check character varying(50),
    validity_status character varying(20),
    last_checked date
);


ALTER TABLE public.data_quality OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 16457)
-- Name: data_sources; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.data_sources (
    source_id character varying(10) NOT NULL,
    provider character varying(100),
    dataset_name character varying(150),
    source_type character varying(50),
    purpose character varying(150),
    reference character varying(255),
    last_updated character varying(100)
);


ALTER TABLE public.data_sources OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16409)
-- Name: disruptions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.disruptions (
    disruption_id character varying(10) NOT NULL,
    location_id character varying(10),
    route_id character varying(10),
    disruption_type character varying(50),
    severity character varying(20),
    description character varying(255),
    status character varying(50),
    reported_at timestamp without time zone
);


ALTER TABLE public.disruptions OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 16427)
-- Name: facilities; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.facilities (
    facility_id character varying(10) NOT NULL,
    facility_name character varying(100),
    facility_type character varying(50),
    location_id character varying(10),
    latitude double precision,
    longitude double precision,
    capacity integer,
    accessibility_score integer,
    status character varying(50)
);


ALTER TABLE public.facilities OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16385)
-- Name: locations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.locations (
    location_id character varying(10) NOT NULL,
    city character varying(100),
    state character varying(100),
    latitude double precision,
    longitude double precision,
    location_type character varying(50)
);


ALTER TABLE public.locations OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 16445)
-- Name: logistics; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.logistics (
    shipment_id character varying(10) NOT NULL,
    source_location_id character varying(10),
    destination_location_id character varying(10),
    cargo_type character varying(100),
    weight_kg double precision,
    priority character varying(20),
    shipment_status character varying(50),
    planned_date date
);


ALTER TABLE public.logistics OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 16433)
-- Name: public_transport; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.public_transport (
    transport_id character varying(10) NOT NULL,
    source_location_id character varying(10),
    destination_location_id character varying(10),
    transport_mode character varying(50),
    availability character varying(50),
    frequency_per_day integer,
    status character varying(50)
);


ALTER TABLE public.public_transport OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16403)
-- Name: road_conditions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.road_conditions (
    road_condition_id character varying(10) NOT NULL,
    route_id character varying(10),
    surface_score integer,
    drainage_score integer,
    damage_count integer,
    condition_status character varying(50),
    updated_at timestamp without time zone
);


ALTER TABLE public.road_conditions OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16391)
-- Name: routes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.routes (
    route_id character varying(10) NOT NULL,
    source_location_id character varying(10),
    destination_location_id character varying(10),
    distance_km double precision,
    estimated_time_min integer,
    road_condition character varying(50),
    route_status character varying(50),
    risk_level character varying(20)
);


ALTER TABLE public.routes OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 16415)
-- Name: traffic; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.traffic (
    traffic_id character varying(10) NOT NULL,
    route_id character varying(10),
    congestion_percent double precision,
    congestion_level character varying(20),
    delay_factor double precision,
    recorded_at timestamp without time zone
);


ALTER TABLE public.traffic OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16421)
-- Name: vehicles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vehicles (
    vehicle_id character varying(10) NOT NULL,
    vehicle_type character varying(50),
    latitude double precision,
    longitude double precision,
    speed_kmh double precision,
    vehicle_status character varying(50),
    last_updated timestamp without time zone
);


ALTER TABLE public.vehicles OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16397)
-- Name: weather; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.weather (
    weather_id character varying(10) NOT NULL,
    location_id character varying(10),
    temperature_c double precision,
    rainfall_mm double precision,
    humidity_percent double precision,
    weather_condition character varying(50),
    recorded_at timestamp without time zone
);


ALTER TABLE public.weather OWNER TO postgres;

--
-- TOC entry 5091 (class 0 OID 16439)
-- Dependencies: 228
-- Data for Name: accessibility; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.accessibility (accessibility_id, location_id, road_access_score, transport_access_score, risk_score, overall_accessibility_score, recorded_at) FROM stdin;
A001	L001	68	55	62	61	2026-09-08 10:30:00
A002	L002	82	78	75	80	2026-09-08 10:30:00
A003	L003	75	68	70	72	2026-09-08 10:30:00
A004	L004	58	60	48	56	2026-09-08 10:30:00
A005	L005	62	55	60	59	2026-09-08 10:30:00
A006	L006	72	65	68	69	2026-09-08 10:30:00
A007	L007	65	50	64	58	2026-09-08 10:30:00
A008	L008	80	72	78	77	2026-09-08 10:30:00
\.


--
-- TOC entry 5093 (class 0 OID 16451)
-- Dependencies: 230
-- Data for Name: alerts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alerts (alert_id, location_id, route_id, alert_type, severity, message, alert_status, created_at) FROM stdin;
AL001	L004	R003	Landslide Risk	High	Heavy rainfall and poor road condition; consider alternate route	Active	2026-09-08 10:35:00
AL002	L009	R003	Road Disruption	Medium	Road damage reported; monitor route before dispatch	Active	2026-09-08 10:35:00
AL003	L002	R001	Traffic	Medium	Moderate congestion detected	Monitoring	2026-09-08 10:35:00
AL004	L001	R005	Weather	Medium	Heavy rain may affect travel time	Active	2026-09-08 10:35:00
\.


--
-- TOC entry 5095 (class 0 OID 16465)
-- Dependencies: 232
-- Data for Name: data_quality; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.data_quality (quality_id, table_name, validation_rule, missing_value_check, duplicate_check, validity_status, last_checked) FROM stdin;
Q001	locations	Coordinates numeric and valid	PASS	No duplicate location_id	PASS	2026-09-08
Q002	routes	Source and destination IDs exist	PASS	No duplicate route_id	PASS	2026-09-08
Q003	weather	Numeric values and timestamp valid	PASS	No duplicate weather_id	PASS	2026-09-08
Q004	disruptions	Severity and status valid	PASS	No duplicate disruption_id	PASS	2026-09-08
Q005	traffic	Congestion between 0 and 100%	PASS	No duplicate traffic_id	PASS	2026-09-08
Q006	vehicles	Coordinates and timestamp valid	PASS	No duplicate vehicle_id	PASS	2026-09-08
Q007	facilities	Capacity and accessibility valid	PASS	No duplicate facility_id	PASS	2026-09-08
Q008	logistics	Weight non-negative and location IDs valid	PASS	No duplicate shipment_id	PASS	2026-09-08
\.


--
-- TOC entry 5094 (class 0 OID 16457)
-- Dependencies: 231
-- Data for Name: data_sources; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.data_sources (source_id, provider, dataset_name, source_type, purpose, reference, last_updated) FROM stdin;
SRC001	Open Government Data	NER location/admin reference	Government/Open Data	Locations and regional reference	https://www.data.gov.in/	Prototype reference
SRC002	India Meteorological Department	Rainfall/weather reference	Government/Open Data	Weather and rainfall	https://www.data.gov.in/catalog/rainfall-india	Use live/API feed where available
SRC003	Transport/Government datasets	Road/transport reference	Government/Open Data	Routes and transport	https://data.gov.in/sector/transport	Use current source/API where available
SRC004	Prototype-generated records	Vehicle GPS/logistics/alerts and selected operational values	Synthetic Demo Data	Demonstration and testing	Internal prototype	Not live government data
\.


--
-- TOC entry 5086 (class 0 OID 16409)
-- Dependencies: 223
-- Data for Name: disruptions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.disruptions (disruption_id, location_id, route_id, disruption_type, severity, description, status, reported_at) FROM stdin;
D001	L004	R003	Landslide Risk	High	Heavy rainfall; possible slope instability	Monitoring	2026-09-08 09:30:00
D002	L009	R003	Road Damage	Medium	Damaged road section reported	Active	2026-09-08 08:45:00
D003	L002	R001	Waterlogging	Medium	Temporary water accumulation	Monitoring	2026-09-08 09:10:00
D004	L001	R005	Heavy Rain	Medium	Reduced visibility reported	Active	2026-09-08 09:50:00
\.


--
-- TOC entry 5089 (class 0 OID 16427)
-- Dependencies: 226
-- Data for Name: facilities; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.facilities (facility_id, facility_name, facility_type, location_id, latitude, longitude, capacity, accessibility_score, status) FROM stdin;
F001	Guwahati Medical Center	Hospital	L002	26.1448	91.7359	250	88	Open
F002	Shillong Relief Center	Relief Center	L004	25.5792	91.894	500	82	Open
F003	Imphal Distribution Hub	Warehouse	L003	24.8174	93.9372	300	76	Open
F004	Aizawl Emergency Center	Emergency Center	L005	23.7275	92.7179	150	79	Open
F005	Agartala Relief Warehouse	Warehouse	L008	23.8318	91.2872	400	84	Open
\.


--
-- TOC entry 5082 (class 0 OID 16385)
-- Dependencies: 219
-- Data for Name: locations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.locations (location_id, city, state, latitude, longitude, location_type) FROM stdin;
L001	Itanagar	Arunachal Pradesh	27.0844	93.6053	Capital City
L002	Guwahati	Assam	26.1445	91.7362	Major City
L003	Imphal	Manipur	24.817	93.9368	Capital City
L004	Shillong	Meghalaya	25.5788	91.8933	Capital City
L005	Aizawl	Mizoram	23.7271	92.7176	Capital City
L006	Kohima	Nagaland	25.6751	94.1086	Capital City
L007	Gangtok	Sikkim	27.3389	88.6065	Capital City
L008	Agartala	Tripura	23.8315	91.2868	Capital City
L009	Tura	Meghalaya	25.5141	90.2027	Major Town
L010	Dimapur	Nagaland	25.8629	93.7537	Transport Hub
\.


--
-- TOC entry 5092 (class 0 OID 16445)
-- Dependencies: 229
-- Data for Name: logistics; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.logistics (shipment_id, source_location_id, destination_location_id, cargo_type, weight_kg, priority, shipment_status, planned_date) FROM stdin;
S001	L002	L004	Medical Supplies	500	High	In Transit	2026-09-09
S002	L004	L009	Food Supplies	1200	High	Planned	2026-09-09
S003	L002	L003	Emergency Equipment	350	High	In Transit	2026-09-09
S004	L008	L002	Relief Materials	800	Medium	Planned	2026-09-10
S005	L007	L001	Essential Goods	600	Medium	Planned	2026-09-10
\.


--
-- TOC entry 5090 (class 0 OID 16433)
-- Dependencies: 227
-- Data for Name: public_transport; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.public_transport (transport_id, source_location_id, destination_location_id, transport_mode, availability, frequency_per_day, status) FROM stdin;
PT001	L002	L004	Bus	Available	8	Operational
PT002	L004	L009	Bus	Limited	4	Operational
PT003	L003	L006	Bus	Available	5	Operational
PT004	L008	L002	Bus	Available	6	Operational
PT005	L006	L010	Bus	Available	10	Operational
\.


--
-- TOC entry 5085 (class 0 OID 16403)
-- Dependencies: 222
-- Data for Name: road_conditions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.road_conditions (road_condition_id, route_id, surface_score, drainage_score, damage_count, condition_status, updated_at) FROM stdin;
RC001	R001	72	68	3	Moderate	2026-09-08 10:15:00
RC002	R002	70	65	2	Moderate	2026-09-08 10:15:00
RC003	R003	48	40	7	Poor	2026-09-08 10:15:00
RC004	R004	85	82	1	Good	2026-09-08 10:15:00
RC005	R005	62	55	4	Moderate	2026-09-08 10:15:00
RC006	R006	82	78	1	Good	2026-09-08 10:15:00
RC007	R007	58	50	5	Moderate	2026-09-08 10:15:00
RC008	R008	65	60	3	Moderate	2026-09-08 10:15:00
\.


--
-- TOC entry 5083 (class 0 OID 16391)
-- Dependencies: 220
-- Data for Name: routes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.routes (route_id, source_location_id, destination_location_id, distance_km, estimated_time_min, road_condition, route_status, risk_level) FROM stdin;
R001	L002	L004	98	180	Moderate	Open	Medium
R002	L003	L006	140	300	Moderate	Open	Medium
R003	L004	L009	323	600	Poor	Caution	High
R004	L006	L010	74	150	Good	Open	Low
R005	L007	L001	310	540	Moderate	Open	High
R006	L008	L002	590	720	Good	Open	Medium
R007	L001	L002	430	660	Moderate	Open	High
R008	L005	L004	450	780	Moderate	Open	High
\.


--
-- TOC entry 5087 (class 0 OID 16415)
-- Dependencies: 224
-- Data for Name: traffic; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.traffic (traffic_id, route_id, congestion_percent, congestion_level, delay_factor, recorded_at) FROM stdin;
T001	R001	55	Moderate	1.25	2026-09-08 10:20:00
T002	R002	42	Moderate	1.18	2026-09-08 10:20:00
T003	R003	78	High	1.55	2026-09-08 10:20:00
T004	R004	25	Low	1.05	2026-09-08 10:20:00
T005	R005	65	High	1.42	2026-09-08 10:20:00
T006	R006	30	Low	1.08	2026-09-08 10:20:00
\.


--
-- TOC entry 5088 (class 0 OID 16421)
-- Dependencies: 225
-- Data for Name: vehicles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vehicles (vehicle_id, vehicle_type, latitude, longitude, speed_kmh, vehicle_status, last_updated) FROM stdin;
V001	Relief Truck	26.1452	91.7355	42	In Transit	2026-09-08 10:25:00
V002	Medical Van	25.5795	91.8928	28	In Transit	2026-09-08 10:25:00
V003	Supply Truck	24.818	93.9355	35	In Transit	2026-09-08 10:25:00
V004	Emergency Vehicle	23.7278	92.7182	18	Available	2026-09-08 10:25:00
V005	Relief Truck	25.6745	94.1092	40	In Transit	2026-09-08 10:25:00
\.


--
-- TOC entry 5084 (class 0 OID 16397)
-- Dependencies: 221
-- Data for Name: weather; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.weather (weather_id, location_id, temperature_c, rainfall_mm, humidity_percent, weather_condition, recorded_at) FROM stdin;
W001	L001	24.5	18	82	Rainy	2026-09-08 10:00:00
W002	L002	29	12	78	Cloudy	2026-09-08 10:00:00
W003	L003	25	8	80	Cloudy	2026-09-08 10:00:00
W004	L004	20	25	88	Heavy Rain	2026-09-08 10:00:00
W005	L005	23	15	84	Rainy	2026-09-08 10:00:00
W006	L006	21.5	10	79	Cloudy	2026-09-08 10:00:00
W007	L007	17.5	5	76	Cloudy	2026-09-08 10:00:00
W008	L008	28	7	75	Partly Cloudy	2026-09-08 10:00:00
\.


--
-- TOC entry 4926 (class 2606 OID 16444)
-- Name: accessibility accessibility_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accessibility
    ADD CONSTRAINT accessibility_pkey PRIMARY KEY (accessibility_id);


--
-- TOC entry 4930 (class 2606 OID 16456)
-- Name: alerts alerts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alerts
    ADD CONSTRAINT alerts_pkey PRIMARY KEY (alert_id);


--
-- TOC entry 4934 (class 2606 OID 16470)
-- Name: data_quality data_quality_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_quality
    ADD CONSTRAINT data_quality_pkey PRIMARY KEY (quality_id);


--
-- TOC entry 4932 (class 2606 OID 16464)
-- Name: data_sources data_sources_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_sources
    ADD CONSTRAINT data_sources_pkey PRIMARY KEY (source_id);


--
-- TOC entry 4916 (class 2606 OID 16414)
-- Name: disruptions disruptions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.disruptions
    ADD CONSTRAINT disruptions_pkey PRIMARY KEY (disruption_id);


--
-- TOC entry 4922 (class 2606 OID 16432)
-- Name: facilities facilities_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.facilities
    ADD CONSTRAINT facilities_pkey PRIMARY KEY (facility_id);


--
-- TOC entry 4908 (class 2606 OID 16390)
-- Name: locations locations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.locations
    ADD CONSTRAINT locations_pkey PRIMARY KEY (location_id);


--
-- TOC entry 4928 (class 2606 OID 16450)
-- Name: logistics logistics_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.logistics
    ADD CONSTRAINT logistics_pkey PRIMARY KEY (shipment_id);


--
-- TOC entry 4924 (class 2606 OID 16438)
-- Name: public_transport public_transport_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.public_transport
    ADD CONSTRAINT public_transport_pkey PRIMARY KEY (transport_id);


--
-- TOC entry 4914 (class 2606 OID 16408)
-- Name: road_conditions road_conditions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.road_conditions
    ADD CONSTRAINT road_conditions_pkey PRIMARY KEY (road_condition_id);


--
-- TOC entry 4910 (class 2606 OID 16396)
-- Name: routes routes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.routes
    ADD CONSTRAINT routes_pkey PRIMARY KEY (route_id);


--
-- TOC entry 4918 (class 2606 OID 16420)
-- Name: traffic traffic_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.traffic
    ADD CONSTRAINT traffic_pkey PRIMARY KEY (traffic_id);


--
-- TOC entry 4920 (class 2606 OID 16426)
-- Name: vehicles vehicles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicles
    ADD CONSTRAINT vehicles_pkey PRIMARY KEY (vehicle_id);


--
-- TOC entry 4912 (class 2606 OID 16402)
-- Name: weather weather_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.weather
    ADD CONSTRAINT weather_pkey PRIMARY KEY (weather_id);


-- Completed on 2026-09-09 13:39:45

--
-- PostgreSQL database dump complete
--

\unrestrict 3k9PM9Soc1SvxHVdKowc2v1Eh8fcGVljrWF2fJMDaKBRjdKKOPOqHL07Pg0XUSf

