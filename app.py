import pandas as pd
import streamlit as st
import plotly.express as px




st.header("Market of Vehicles in the US")
st.write("FIlter the data below to see at what price are cars being sold")

df = pd.read_csv("vehicles_us.csv")
df.isnull().sum()
df["model_year"].fillna(df["model_year"].median(), inplace=True)
df["odometer"].fillna(df["odometer"].median(), inplace=True)
df["is_4wd"]=df['is_4wd'].fillna(0)
df["paint_color"].fillna(df["paint_color"].mode()[0], inplace=True)
df["transmission"].fillna(df["transmission"].mode()[0], inplace=True)

st.header('Price analysis')
st.write("#####" " Lets analyze what influences price the most. We will check how distibution of price varies depending on  transmission, engine or body type and state")
# Filter dataset
filtered_df = df[df['price'] <= 60000]

# Create histogram
fig1 = px.histogram(filtered_df, x="price", nbins=25, title="Histogram of Car Prices",
                   labels={"price": "Price ($)"}, color_discrete_sequence=["blue"])

# Update layout for better readability
fig1.update_layout(xaxis_title="Price ($)", yaxis_title="Frequency", 
                  bargap=0.05, template="plotly_white")

# Show plot
st.plotly_chart(fig1)

df['condition']= df["condition"].astype("category")

# Scatter plot of odometer vs price
fig2 = px.scatter(df, 
                 x='odometer', 
                 y='price', 
                 color='condition', 
                 color_continuous_scale='viridis', 
                 opacity=0.7,
                 title='Scatter Plot of Odometer vs. Price',
                 labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)'},
                 hover_data=df.columns)  # Adds more details on hover

# Show plot
st.plotly_chart(fig2)
# box plot condition vs price 
fig3 = px.box(df, 
             x="condition", 
             y="price", 
             color="condition", 
             title="Box Plot of Price by Vehicle Condition",
             labels={"condition": "Vehicle Condition", "price": "Price ($)"},
             boxmode="group")  # Groups different conditions

# Show plot
st.plotly_chart(fig3)
