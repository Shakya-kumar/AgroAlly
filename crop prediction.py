print("----------------------------------------------crop prediction-------------------------------------------")
import pandas as pd
import numpy as np

# Read the CSV file (replace 'Crop_dataset.csv' with the correct file path)
df = pd.read_csv('Crop_dataset.csv')

# Function to calculate Euclidean distance between two points
def euclidean_distance(x1, x2):
    return np.linalg.norm(x1 - x2)

# Function to find the closest row in the dataset
def find_closest_row(input_values, dataset):
    distances = dataset.iloc[:, :-2].apply(lambda row: euclidean_distance(input_values, row), axis=1)
    closest_index = distances.idxmin()
    closest_row = dataset.loc[closest_index]
    return closest_row

# Dictionary to store SI unit information for each attribute
unit_info = {
    "N": "kg/ha",
    "P": "kg/ha",
    "K": "kg/ha",
    "temperature": "°C",
    "humidity": "%",
    "ph": "pH (1-14)",
    "rainfall": "mm"
}

# Take input values in SI units
print("Enter the values for nitrogen composition (N), Phosphorus content (P), potassium content (K),")
print("temperature (in degree Celsius), humidity (%), pH (in the range of 1 to 14), rainfall (in mm)")

attributes = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
input_values = []

# Collect user input and convert to appropriate data type
for attr in attributes:
    unit = unit_info[attr]
    while True:
        try:
            value = float(input(f"Enter the value of {attr} ({unit}): "))
            if attr == "ph" and not (1 <= value <= 14):
                print("Error: pH value must be between 1 and 14.")
                continue
            input_values.append(value)
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

# Find the closest row in the dataset
closest_row = find_closest_row(np.array(input_values), df)

# Print the result
print("\nClosest row found:")
print(closest_row)

# Ask if user wants crop suggestion
response = input("Do you want to grow a specific crop? (yes/no): ").lower()

if response == "yes":
    # Prompt user to enter the crop name
    crop_name = input("Enter the crop name you want to grow: ")

    # Check if the crop name exists in the dataset (in either label or Indian_name)
    if crop_name in df['label'].values or crop_name in df['Indian_name'].values:
        # Filter dataset to get rows corresponding to the selected crop
        crop_data = df[df['label'] == crop_name]  # Filter by label
        if crop_data.empty:
            crop_data = df[df['Indian_name'] == crop_name]  # Filter by Indian_name if label doesn't match

        # Calculate average values for each attribute
        avg_values = crop_data[attributes].mean().values

        # Calculate adjustments needed based on the differences
        adjustments = avg_values - input_values

        # Print adjustments needed for each attribute
        print(f"\nTo grow {crop_name}, you need the following adjustments:")
        for attr, adjustment in zip(attributes, adjustments):
            unit = unit_info[attr]
            current_value = input_values[attributes.index(attr)]
            required_value = avg_values[attributes.index(attr)]

            if adjustment > 0:
                print(f"Your {attr} is {current_value:.2f} {unit}, but {crop_name} requires an average of {required_value:.2f} {unit}.")
                print(f"You need to boost {attr} by {abs(adjustment):.2f} {unit}.")
            elif adjustment < 0:
                print(f"Your {attr} is {current_value:.2f} {unit}, but {crop_name} requires an average of {required_value:.2f} {unit}.")
                print(f"You have excess {attr} by {abs(adjustment):.2f} {unit}.")
            else:
                print(f"Your {attr} is already optimal for {crop_name}.")

    else:
        print(f"The crop '{crop_name}' is not available in the dataset.")

else:
    print("Thank you for using the program!")
