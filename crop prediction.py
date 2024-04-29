import pandas as pd

# Read the CSV file
df = pd.read_csv('crop_prediction.csv')

# Function to calculate Euclidean distance between two points
def euclidean_distance(x1, x2):
    return sum((x1[i] - x2[i])**2 for i in range(len(x1))) ** 0.5

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
print("Enter the values for n, p, k, temperature, humidity, pH, and rainfall:")
input_values = []
for _ in range(7):
    value = int(input())
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

