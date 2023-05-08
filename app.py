import streamlit as st
import pandas as pd
import numpy as np
import pickle


model = pickle.load(open("./artifacts/model.pkl", "rb"))
scaler = pickle.load(open("./artifacts/preprocessor.pkl", "rb"))

######################################## Streamlit ##############################################

Delivery_person_Age = st.number_input("Age")
Delivery_person_Ratings = st.number_input("Ratings")
Weather_condtitions = st.selectbox("Weather Condtions: ", ['Fog', 'Stormy', 'Sandstorms', 'Windy', 'Cloudy', 'Sunny'])
Road_traffic_density = st.selectbox("Traffic: ", ['Jam', 'High', 'Medium', 'Low'])
Vehicle_condition = st.selectbox("Vehicle_condition: ", [2, 1, 0, 3])
Type_of_vehicle  = st.selectbox("Type of vechicle: ", ['motorcycle', 'scooter', 'electric_scooter', 'bicycle'])
Type_of_order = st.selectbox("Type_of_order: ", ['Snack', 'Meal', 'Drinks', 'Buffet'])
multiple_diliveries = st.selectbox("multiple_diliveries", [3., 1., 0., 2.])
Festival = st.radio("Festival: ", ["No", "Yes"])
City = st.selectbox("City: ", ['Metropolitian', 'Urban', 'Semi-Urban'])
Displacement = st.number_input("Displacement")

data = [[Delivery_person_Age, Delivery_person_Ratings, Weather_condtitions, Road_traffic_density, Vehicle_condition, Type_of_order, Type_of_vehicle, multiple_diliveries, Festival, City, Displacement]]
#data = np.reshape(data, (1, -1))
#print(data)
data = pd.DataFrame(data=data)#, columns=['Delivery_person_Age', 'Delivery_person_Ratings', 'Weather_conditions', 'Road_traffic_density', 'Vehicle_condition',  'Type_of_order', 'Type_of_vehicle' 'multiple_deliveries', 'Festival', 'City', 'Displacement'], index=False)
#print(data)
new_data = scaler.transform(data)

prediction = model.predict(new_data)
submit = st.button('Predict')
if submit:
    st.write('Response',prediction[0])