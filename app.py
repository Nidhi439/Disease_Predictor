# app.py
import streamlit as st
import pandas as pd
import joblib

# Load model, encoder, and description data
model = joblib.load('model/rf_model.joblib')
le = joblib.load('model/label_encoder.joblib')

# Load symptoms from dataset
df = pd.read_csv('dataset/Training.csv')
symptoms = df.columns[:-1]

# Disease descriptions (you could also load this from a file)
disease_descriptions = {
    "Acne": "A skin condition that occurs when hair follicles become plugged with oil and dead skin cells.",
    "AIDS": "A chronic immune system disease caused by the human immunodeficiency virus (HIV).",
    "Alcoholic hepatitis": "Liver inflammation caused by drinking alcohol.",
    "Allergy": "An immune system reaction to a foreign substance that's not typically harmful to your body.",
    "Arthritis": "Inflammation of one or more joints, causing pain and stiffness.",
    "Bronchial Asthma": "A respiratory condition marked by spasms in the bronchi of the lungs.",
    "Cervical spondylosis": "Age-related wear and tear affecting the spinal disks in the neck.",
    "Chicken pox": "A highly contagious viral infection causing an itchy, blister-like rash.",
    "Common Cold": "A viral infection of your nose and throat (upper respiratory tract).",
    "Dengue": "A mosquito-borne viral infection causing a severe flu-like illness.",
    "Diabetes": "A metabolic disease that causes high blood sugar.",
    "Dimorphic hemorrhoids(piles)": "Swollen and inflamed veins in the rectum and anus.",
    "Fungal infection": "Infection caused by fungi, often in skin or nails.",
    "Hypertension": "A condition in which the force of the blood against artery walls is too high.",
    "Hyperthyroidism": "Overproduction of thyroid hormone by the thyroid gland.",
    "Hypothyroidism": "Underproduction of thyroid hormone by the thyroid gland.",
    "Impetigo": "A highly contagious skin infection that mainly affects infants and children.",
    "Jaundice": "Yellowing of the skin and eyes due to high bilirubin levels.",
    "Malaria": "A mosquito-borne infectious disease affecting humans and animals.",
    "Migraine": "A headache that can cause severe throbbing pain or pulsing sensation.",
    "Peptic ulcer disease": "Sores that develop on the lining of stomach, small intestine or esophagus.",
    "Pneumonia": "Infection that inflames air sacs in one or both lungs.",
    "Psoriasis": "A skin disease that causes red, itchy scaly patches.",
    "Tuberculosis": "A potentially serious infectious bacterial disease affecting the lungs.",
    "Typhoid": "A bacterial infection that can spread throughout the body.",
    "Urinary tract infection": "Infection in any part of the urinary system.",
    "Varicose veins": "Enlarged, twisted veins often appearing blue or dark purple.",
    "Hepatitis A": "A highly contagious liver infection caused by the hepatitis A virus.",
    "Hepatitis B": "A serious liver infection caused by the hepatitis B virus.",
    "Hepatitis C": "An infection caused by a virus that attacks the liver.",
    "Hepatitis D": "A serious liver disease caused by infection with the hepatitis D virus.",
    "Hepatitis E": "A liver disease caused by the hepatitis E virus.",
    "GERD": "Gastroesophageal reflux disease, a chronic digestive disorder.",
    "Heart disease": "A range of conditions that affect your heart.",
    "Paralysis (brain hemorrhage)": "Loss of muscle function due to bleeding in the brain."
}

st.title("🩺 Disease Prediction from Symptoms")
st.write("Select symptoms and click Predict")

# User multiselect with search functionality
selected_symptoms = st.multiselect(
    "Choose Symptoms (start typing to search)", 
    list(symptoms),
    help="Select all symptoms you're experiencing"
)

# Create input for model
input_data = [1 if symptom in selected_symptoms else 0 for symptom in symptoms]

# Predict
if st.button("Predict Disease"):
    if not selected_symptoms:
        st.warning("Please select at least one symptom")
    else:
        prediction = model.predict([input_data])[0]
        disease = le.inverse_transform([prediction])[0]
        
        st.success(f"Predicted Disease: **{disease}**")
        
        # Display description if available
        if disease in disease_descriptions:
            st.info(f"**Description:** {disease_descriptions[disease]}")
        else:
            st.warning("No additional information available for this disease.")
        
        # Add some general advice
        st.subheader("Next Steps")
        st.write("""
        - This prediction is based on the symptoms you provided
        - It's recommended to consult with a healthcare professional for proper diagnosis
        - Do not self-medicate based on this prediction
        - If symptoms persist or worsen, seek medical attention immediately
        """)
        
        # Add some space at the bottom
        st.markdown("---")
        st.caption("Note: This tool is for informational purposes only and not a substitute for professional medical advice.")