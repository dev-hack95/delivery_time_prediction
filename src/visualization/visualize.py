import folium
import pandas as pd
import numpy as np
import plotly.express as px 
import streamlit as st
from streamlit_folium import st_folium

df = pd.read_csv("data/raw/finalTrain.csv")
#df_1 = pd.read_csv("data/raw/raw.csv")

st.set_page_config(
    page_title="Viz Dashboard",
    page_icon="✅",
    layout="wide",
)



st.sidebar.header("Filters: ")

distance = st.sidebar.multiselect(
    "Select: ",
    options=df.index
)  

st.title("Delivery Time Prediction")

def create_map(i):
    map_1 = folium.Map(location=[df.loc[i][4], df.loc[i][5]])
    folium.Marker([df.loc[i][4], df.loc[i][5]], popup='<i>Restaurant</i>', tooltip='Restaurant').add_to(map_1)
    folium.Marker([df.loc[i][6], df.loc[i][7]], popup='<i>Delevery Location</i>', tooltip='Delevery Location', icon=folium.Icon(color='red')).add_to(map_1)
    folium.PolyLine(locations=[[df.loc[i][4], df.loc[i][5]], [df.loc[i][6], df.loc[i][7]]],color='blue').add_to(map_1)
    st_data = st_folium(map_1, width=725)
    return st_data

create_map(1)



Weather = st.sidebar.multiselect(
    "Weather: ",
    options=df["Weather_conditions"].unique(),
    default=df["Weather_conditions"].unique()
)

Traffic = st.sidebar.multiselect(
    "Traffic Density",
    options=df["Road_traffic_density"].unique(),
    default=df["Road_traffic_density"].unique()
)

vehicle = st.sidebar.multiselect(
    "Type_of_vehicle: ",
    options=df['Type_of_vehicle'].unique(),
    default=df['Type_of_vehicle'].unique()
)





df_selection = df.query( "Weather_conditions == @Weather & Road_traffic_density == @Traffic & Type_of_vehicle == @vehicle")

#st.dataframe(df_selection)

st.header("Impact of categorical data on Delivery time")

fig_1 = px.histogram(x=df_selection['Time_taken (min)'])
st.plotly_chart(fig_1, use_container_width=True)


st.header("Rating distribution")
fig_2 = px.histogram(x=df['Delivery_person_Ratings'])
st.plotly_chart(fig_2)


#fig_2 = px.histogram(x = df['Delivery_person_Age'], y = np.median(df['Time_taken (min)']))
#st.plotly_chart(fig_2, use_container_width=True)