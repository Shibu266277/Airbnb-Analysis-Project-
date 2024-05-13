# Importing Libraries
import pandas as pd
import pymongo
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image

# Stream lit page making 
# Displaying image in the first column
with st.sidebar:
    st.image("D:/DATA_SCIENCE/ALL_PROJECTS/Airbnb.png",width=150)

    st.caption("Airbnb Data Visualization | By Shibu")
    # Menu items (assuming it's supposed to be in the sidebar)
    
    selected = option_menu("Menu", ["Home", "Explore","Contact Us"],
                           icons=["house", "graph-up-arrow", "phone book"],
                           menu_icon="menu-button-wide",
                           default_index=0,
                           styles={"nav-link": {"font-size": "20px",
                                                "text-align": "left",
                                                "margin": "-2px",
                                                "--hover-color": "#FF5A5F"},
                                   "nav-link-selected": 
                                   {"background-color": "#FF5A5F"}})


 # Explain about airbnb data has description in Home option   
if selected == 'Home':

    st.markdown(f""" <style>
                    .stApp {{
                        background: url('https://www.spinxdigital.com/app/uploads/2022/11/image-airbnb.jpg');
                        background-size: cover;
                    }}
                    
                    </style>""", unsafe_allow_html=True)
    
    styled_header = "<h1 style='color: orange;'>Welcome To Airbnb Project Data Analysis</h1>"
    st.markdown(styled_header, unsafe_allow_html=True)

    home_text = "In this data analysis project, we delve into the world of Airbnb listings."
    styled_text = f"<h4 style='color: blue; text-align: left;'>{home_text}</h4>"
    st.markdown(styled_text, unsafe_allow_html=True)
    st.markdown("## :blue[Domain] : Travel Industry, Property Management and Tourism")
    st.markdown("## :blue[Technologies used] : Python, Pandas, Plotly, Streamlit, MongoDB")
    st.markdown("## :blue[Overview] : To analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends. ")
    st.markdown("#   ")
    st.markdown("#   ")

# Airbnb Data Viewed by charts methods
if selected=="Explore":
    
    st.markdown(f""" <style>.stApp {{
                background: url('https://news.airbnb.com/wp-content/uploads/sites/4/2023/11/PJMPHOTO18Q436_SNYA72_0609.jpg?fit=2500%2C1667');   
                background-size: cover}}
                </style>""",unsafe_allow_html=True)

    # Upload Cleaned DataFrame Data
    df=pd.read_csv("D:\DATA_SCIENCE\ALL_PROJECTS\Airbnb.csv")

    country = st.sidebar.multiselect('Select a Country',sorted(df.Country.unique()),sorted(df.Country.unique()))
    prop = st.sidebar.multiselect('Select Property_Type',sorted(df.Property_Type.unique()),sorted(df.Property_Type.unique()))
    room = st.sidebar.multiselect('Select Room_Type',sorted(df.Room_Type.unique()),sorted(df.Room_Type.unique()))

    query = f'Country in {country} & Room_Type in {room} & Property_Type in {prop}'    

    col1,col2=st.columns([1,1],gap='small')

    with col1:
      
        df1 = df.query(query).groupby(["Property_Type"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.bar(df1,
                         title='Top 10 Property Types With Count',
                         x='Property_Type', y='count',
                         orientation='v',color='Property_Type',
                         hover_name='Property_Type',
                         color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True) 
        
        
        df1= df.query(query).groupby(["Room_Type"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.pie(df1,
                             title=' Room_Type With Count',
                             values='count',names="Room_Type")
        fig.update_traces(textposition='inside', textinfo='value+label')
        st.plotly_chart(fig,use_container_width=True)    
        
              
        df1= df.query(query).groupby(["Cancellation_policy"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.line(df1,
                             title=' Cancellation_Policy With Count',
                             x='Cancellation_policy',y='count',text='count',markers=True)
        fig.update_traces(textposition="top center")                    
        st.plotly_chart(fig,use_container_width=True)
        
        
        df1= df.query(query).groupby(["Number_Of_Reviews"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.bar(df1,
                             title=' Number_Of_Reviews With Count',
                             x="Number_Of_Reviews",y="count",
                             text="count", orientation='v',
                             color='count',color_continuous_scale=px.colors.sequential.Darkmint_r)
        fig.update_traces( textposition='outside')
        st.plotly_chart(fig,use_container_width=True)
        
        
    with col2: 
      
        df1= df1= df.query(query).groupby('Property_Type',as_index=False)['Minimum_Nights'].mean()
        fig = px.pie(df1,
                             title='Minimum_Nights With Property_Type',
                             values="Minimum_Nights",names="Property_Type")
        fig.update_traces(textposition='inside', textinfo='value+label')
        st.plotly_chart(fig,use_container_width=True) 
        
        
        df1= df1= df.query(query).groupby(["Maximum_Nights"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.pie(df1,
                             title='Maximum_Nights With Count',
                             values='count',names="Maximum_Nights")
        fig.update_traces(textposition='inside')
        fig.update_layout(uniformtext_minsize=12)
        st.plotly_chart(fig,use_container_width=True)
        
        
        df1= df1= df.query(query).groupby(["Host_Neighbourhood"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.bar(df1,
                             title='Host Neighbourhood With Count',
                             x="Host_Neighbourhood", y="count",
                             orientation='v',color='count',
                             color_continuous_scale=px.colors.sequential.Bluered_r)
        st.plotly_chart(fig,use_container_width=True)
        
        
        df1= df1= df.query(query).groupby("Property_Type",as_index=False)['Price'].mean().sort_values(by='Price',ascending=False)[:10]
        fig = px.bar(df1,
                             title=' Property With Mean Price ',
                             x="Property_Type",y="Price",
                             text="Price", orientation='v',
                             color='Property_Type',color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True) 

 # Detail collecting for data       
elif selected=="Contact Us": 

    st.markdown(f""" <style>.stApp {{
                    background: url('https://blog.artonemfg.com/hubfs/airbnb-3399753_1920.jpg');   
                    background-size: cover}}
                    </style>""",unsafe_allow_html=True)

    st.subheader(':Black[Airbnb Data Visualisation]')
    st.markdown(''':red[**I Created this Airbnb Data Analysis Project Using "Python" to perform Data Cleansing, Understand Dataset, 
                "Exploratery Data anslysis (EDA)" and Creating "Dashboard report" Using "Power BI".
                Since 2008, guests and hosts have used Airbnb to expand on travelling possibilities and present more unique,
                personalized way of experiencing the world. This dataset describes the listing activity and metrics in Amsterdam,
                Netherland for 2019.The objective of the project is to perform data visualization techniques to understand the insight of the data.
                This project aims to apply Exploratory Data Analysis (EDA) and Business Intelligence tools such as Power BI to get a visual understanding of the data.**]''')

    coll1, coll2 = st.columns(2)
    with coll1: 
        st.title("Contact Us")  
        st.caption(":red[Note:*fill all mandatory fields]") 
                
        Name = st.text_input("Name*")
        Mobile = st.text_input("Mobile*")
        Email = st.text_input("Email*")
        Message = st.text_area("Message (optional)")
        
        if st.button("Submit"):
            st.success('''Thank you for your Message, We will get back to you soon''')
