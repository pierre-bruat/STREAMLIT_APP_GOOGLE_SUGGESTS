#import streamlit as st
#import pandas as pd
#import sitemap_ping
#import urllib
#from urllib.request import urlopen
#from bs4 import BeautifulSoup
#import json
#import requests
#import time

#@st.cache

def convert_df(df):
	return df.to_csv().encode('utf-8')


def gSuggest(kw):
    googleSuggestURL="https://suggestqueries.google.com/complete/search?hl=fr&client=firefox&q="
    response = requests.get(googleSuggestURL+kw, headers={'User-agent':'Mozilla/5.0'})
    result = json.loads(response.content.decode('utf-8'))
    result = result[1]
    return result

st.title('Find Suggested queries 🕵')

form = st.form(key='my-form')
kw = form.text_input('keyword')
#depth = form.text_input('depth')
submit = form.form_submit_button('Submit')   
if submit:
    result = gSuggest(kw)
    result = pd.DataFrame(result)
    st.write(result)
    csv = convert_df(result)
    st.download_button(label="Download data as CSV", data=csv, file_name="my_data.csv",mime='text/csv')

