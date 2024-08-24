from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('Crop_dataset.csv')

# List of attributes to consider for calculations
attributes = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

# Function to calculate Euclidean distance between two points
def euclidean_distance(x1, x2):
    return np.linalg.norm(x1 - x2)

# Function to find the closest row in the dataset
def find_closest_row(input_values, dataset):
    distances = dataset[attributes].apply(lambda row: euclidean_distance(input_values, row), axis=1)
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

# Dictionary to map English crop names to Hindi names
crop_name_mapping = {
    "rice": "चावल",
    "maize": "मक्का",
    "chickpea": "चना",
    "kidneybeans": "राजमा",
    "pigeonpeas": "तूर दाल",
    "mothbeans": "मोत दाल",
    "mungbean": "मूंग",
    "blackgram": "काला चना",
    "lentil": "दाल",
    "pomegranate": "अनार",
    "banana": "केला",
    "mango": "आम",
    "grapes": "अंगूर",
    "watermelon": "तरबूज",
    "muskmelon": "खरबूजा",
    "apple": "सेब",
    "orange": "संतरा",
    "papaya": "पपीता",
    "coconut": "नारियल",
    "cotton": "रुई",
    "jute": "जूट",
    "coffee": "कॉफी",
    "wheat": "गेहूं",
    "sugarcane": "गन्ना",
    "corn": "भुट्टा",
    "groundnut": "मूँगफली",
    "tea": "चाय",
    "rubber": "रबड़",
    "turmeric": "हल्दी",
    "pepper": "काली मिर्च",
    "tomato": "टमाटर"
}

# Reverse mapping from Hindi to English
hindi_to_english = {v: k for k, v in crop_name_mapping.items()}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_values = np.array([data['N'], data['P'], data['K'], data['temperature'], data['humidity'], data['ph'], data['rainfall']])
    closest_row = find_closest_row(input_values, df)
    closest_crop = closest_row['label']
    hindi_name = crop_name_mapping.get(closest_crop, "Unknown")
    response = {
        'crop': closest_crop,
        'hindi_name': hindi_name,
        'details': closest_row.to_dict()
    }
    return jsonify(response)

@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.get_json()
    input_values = np.array([data['N'], data['P'], data['K'], data['temperature'], data['humidity'], data['ph'], data['rainfall']])
    crop_name = data['crop_name'].strip().lower()
    crop_name_english = crop_name_mapping.get(crop_name, None)
    crop_name_hindi = hindi_to_english.get(crop_name, None)

    if crop_name_english or crop_name_hindi:
        selected_crop = crop_name_english if crop_name_english else crop_name_hindi
        crop_data = df[df['label'].str.lower() == selected_crop]
        avg_values = crop_data[attributes].mean().values
        adjustments = avg_values - input_values
        hindi_name = crop_name_mapping.get(selected_crop, "Unknown")
        adjustments_details = {attr: {'current': input_values[i], 'required': avg_values[i], 'adjustment': adjustments[i]} for i, attr in enumerate(attributes)}
        response = {
            'crop': selected_crop,
            'hindi_name': hindi_name,
            'adjustments': adjustments_details
        }
    else:
        response = {'error': f"The crop '{crop_name}' is not available in the dataset."}
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
