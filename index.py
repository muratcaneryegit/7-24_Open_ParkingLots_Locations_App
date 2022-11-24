import streamlit as st
import pandas as pd
istanbulpark=pd.read_csv('ispark_parking (1).csv')
counties=istanbulpark['COUNTY_NAME'].unique()
county=st.sidebar.selectbox("Choose County",counties)
time24=st.sidebar.checkbox("24 Hour")
if time24:
    istanbulpark=istanbulpark[istanbulpark['WORKING_TIME']=="24 Hour"]
istanbulpark=istanbulpark[istanbulpark['COUNTY_NAME']==county]
df=istanbulpark[['LONGITUDE','LATITUDE']]
df.columns=["lon","lat"]
st.map(df)
st.sidebar.write("Number of parking lots in the district ",county," : ",len(df))
st.dataframe(istanbulpark)





