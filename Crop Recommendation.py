def recommend_crops(ph, carbon, nitrogen, sulfur, water_capacity):
    # Connect to the database
    conn = sqlite3.connect("crop_details.db")
    cursor = conn.cursor()

    # Query crops based on user input
    cursor.execute("""
        SELECT crop_name
        FROM crops
        WHERE ph_level <= ? AND carbon_content >= ? AND nitrogen_content >= ?
            AND sulfur_content >= ? AND water_holding_capacity >= ?
    """, (ph, carbon, nitrogen, sulfur, water_capacity))

    recommended_crops = [row[0] for row in cursor.fetchall()]

    # Close the connection
    conn.close()

    return recommended_crops

# Get user input
user_ph = float(input("Enter pH level: "))
user_carbon = float(input("Enter carbon content: "))
user_nitrogen = float(input("Enter nitrogen content: "))
user_sulfur = float(input("Enter sulfur content: "))
user_water_capacity = float(input("Enter water holding capacity: "))

# Get crop recommendations
crops_to_grow = recommend_crops(user_ph, user_carbon, user_nitrogen, user_sulfur, user_water_capacity)
print(f"Recommended crops: {', '.join(crops_to_grow)}")
