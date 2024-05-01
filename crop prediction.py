import pandas as pd
import numpy as np  

# Read the CSV file
df = pd.read_csv('Crop_dataset.csv')

# Function to calculate Euclidean distance between two points
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))

# Function to find the closest row in the dataset
def find_closest_row(input_values, dataset):
    closest_row = None
    min_distance = float('inf')

    for index, row in dataset.iterrows():
        row_values = row[:-1]  # Exclude the last column which is the label
        distance = euclidean_distance(input_values, row_values)
        if distance < min_distance:
            min_distance = distance
            closest_row = row

    return closest_row

# Take 7 integer inputs
print("Enter the values for nitrogen composition (N), Phosphorus content (P), potassium content (K)")
print("temperature(in degree Celcius),humidity,PH,rainfall (in cm)")
attributes = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

input_values = []
for attr in attributes:
    value = int(input(f"Enter the value of {attr}: "))
    input_values.append(value)

# Find the closest row in the dataset
closest_row = find_closest_row(input_values, df)

# Check if exact match found
exact_match = True
for i in range(7):
    if input_values[i] != closest_row[i]:
        exact_match = False
        break

# Print the result
if exact_match:
    print("Exact match found!")
    print("Label:", closest_row.iloc[-1])
else:
    print("Closest row found:")
    print(closest_row)

# Ask if user wants crop suggestion
response = input("Do you want to grow a specific crop? (yes/no): ").lower()

if response == "yes":
    # Prompt user to enter the crop name
    crop_name = input("Enter the crop name you want to grow: ")

    # Check if the crop name exists in the dataset
    if crop_name in df['label'].values:
        # Filter dataset to get rows corresponding to the selected crop
        crop_data = df[df['label'] == crop_name]

        # Calculate average values for each attribute
        avg_values = crop_data[attributes].mean().values

        # Calculate adjustments needed based on the differences
        adjustments = avg_values - input_values

        # Print adjustments needed for each attribute
        print(f"To grow {crop_name}, you need the following adjustments:")
        for attr, adjustment in zip(attributes, adjustments):
            current_value = input_values[attributes.index(attr)]
            required_value = avg_values[attributes.index(attr)]

            if adjustment > 0:
                print(f"Your {attr} is {current_value}, but {crop_name} requires an average of {required_value}. "
                      f"You need to boost {attr} by {adjustment:.2f}.")
            elif adjustment < 0:
                print(f"Your {attr} is {current_value}, but {crop_name} requires an average of {required_value}. "
                      f"You have excess {attr} by {-adjustment:.2f}.")
            else:
                print(f"Your {attr} is already optimal for {crop_name}.")

    else:
        print(f"The crop '{crop_name}' is not available in the dataset.")

else:
    print("Thank you for using the program!")
