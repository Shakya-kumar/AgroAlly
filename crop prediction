# Crop dataset containing soil type, temperature, and pH level for different crops
crop_database = {
    "wheat": {"soil_type": "loamy", "temperature": "15-25°C", "ph_level": 6.0},
    "rice": {"soil_type": "clayey", "temperature": "20-35°C", "ph_level": 5.5},
    "tomato": {"soil_type": "sandy loam", "temperature": "20-30°C", "ph_level": 6.0},
    # Add more crops and their details as needed
}

# Function to recommend crops based on user input
def recommend_crops(location, soil_type, climate):
    recommended_crops = []
    for crop, details in crop_database.items():
        if details["soil_type"] == soil_type and details["temperature"] in climate:
            recommended_crops.append(crop)
    return recommended_crops

# Function to suggest soil adjustments for a specific crop
def suggest_soil_adjustments(crop):
    if crop in crop_database:
        details = crop_database[crop]
        # Sample soil adjustment suggestions based on crop's optimal conditions
        soil_adjustments = f"For {crop}, it's recommended to maintain pH level around {details['ph_level']}, and ensure adequate {details['soil_type']} soil type."
        return soil_adjustments
    else:
        return "Crop not found in the database."

# Main function to interact with the user
def main():
    print("Welcome to Crop Recommendation Bot!")
    location = input("Please enter your location: ")
    soil_type = input("Please enter your soil type (e.g., loamy, clayey, sandy loam): ")
    climate = input("Please enter your climate temperature range (e.g., 20-30°C): ")

    recommended_crops = recommend_crops(location, soil_type, climate)
    if recommended_crops:
        print("Based on your location, soil type, and climate, we recommend the following crops:")
        for crop in recommended_crops:
            print("- " + crop)
        
        specific_crop = input("Would you like information on growing a specific crop? If yes, please enter the crop name: ")
        if specific_crop.lower() in recommended_crops:
            print("Here are some soil adjustment suggestions for growing " + specific_crop + ":")
            print(suggest_soil_adjustments(specific_crop.lower()))
        else:
            print("Sorry, we don't have information on growing " + specific_crop + " in your area.")
    else:
        print("Sorry, we couldn't find any suitable crops for your location, soil type, and climate.")

if __name__ == "__main__":
    main()
