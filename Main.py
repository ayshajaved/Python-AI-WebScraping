import streamlit as st
import pandas as pd

st.title("Python AI WebScraping")
url = st.text_input("Enter URL of a Website to Scrap: ")
if st.button("Scrape"):
    st.write("Scraping Website")
    