import streamlit as st
from scrap_amazon import generate_product_description

# Streamlit interface
st.title('Product Title and Description Generator')

# Input fields for product details
product_title = st.text_input('Product Title', 'Samsung 27” Curved Monitor')
product_description = st.text_area('Product Description', 'Ultra-slim design, 1800R curvature, AMD FreeSync, 4ms response time, Eye Saver Mode.')

# Input fields for demographic information
demographic_info = st.text_area('Demographic Information', 'Retired lady from New Jersey who enjoys watching movies and online shopping.')

# Button to generate description
if st.button('Generate Description'):
    product_details = {'title': product_title, 'description': product_description}
    title, description, seo_metadata = generate_product_description(product_details, demographic_info)
    st.subheader('Generated Title:')
    st.write(title)
    st.subheader('Generated Description:')
    st.write(description)
    st.subheader('SEO Metadata:')
    st.write(seo_metadata)