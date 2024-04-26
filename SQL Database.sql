import sqlite3

# Connect to the database (create if not exists)
conn = sqlite3.connect("crop_details.db")
cursor = conn.cursor()

# Create a table for crop details
cursor.execute("""
    CREATE TABLE IF NOT EXISTS crops (
        crop_id INTEGER PRIMARY KEY,
        crop_name TEXT,
        ph_level REAL,
        carbon_content REAL,
        nitrogen_content REAL,
        sulfur_content REAL,
        water_holding_capacity REAL
    )
""")

# Insert sample data (you can add more crops)
cursor.execute("""
    INSERT INTO crops (crop_name, ph_level, carbon_content, nitrogen_content, sulfur_content, water_holding_capacity)
    VALUES ('Rice', 6.0, 0.5, 0.2, 0.1, 0.8)
""")

# Commit changes and close the connection
conn.commit()
conn.close()
