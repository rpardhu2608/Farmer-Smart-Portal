import sqlite3

# Connect to SQLite Database
conn = sqlite3.connect("farmer_portal.db", check_same_thread=False)

# Create Cursor
cursor = conn.cursor()

# ==========================================
# Farmer Registration Table
# ==========================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS farmers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    mobile TEXT,
    village TEXT,
    district TEXT,
    state TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# ==========================================
# Weather History Table
# ==========================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS weather_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    temperature REAL,
    humidity INTEGER,
    pressure INTEGER,
    wind_speed REAL,
    weather TEXT,
    searched_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# ==========================================
# Market Prices Table
# ==========================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS market_prices(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_name TEXT,
    market_name TEXT,
    price REAL,
    price_date TEXT
)
""")

# ==========================================
# Soil Guide Table
# ==========================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS soil_data(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    soil_type TEXT,
    ph REAL,
    nitrogen TEXT,
    phosphorus TEXT,
    potassium TEXT,
    recommended_crop TEXT,
    fertilizer TEXT
)
""")

# ==========================================
# Government Schemes Table
# ==========================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS government_schemes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_name TEXT,
    description TEXT,
    eligibility TEXT,
    website TEXT
)
""")

# ==========================================
# Disease Detection Table
# ==========================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS disease_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_name TEXT,
    disease_name TEXT,
    confidence REAL,
    image_name TEXT,
    detected_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# ==========================================
# Feedback Table
# ==========================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    farmer_name TEXT,
    feedback TEXT,
    rating INTEGER,
    submitted_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

print("Farmer Smart Portal Database Created Successfully")