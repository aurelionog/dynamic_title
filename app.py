import streamlit as st
from scrap_amazon import generate_product_description

# Streamlit interface
st.title('Product Title and Description Generator')

# Sidebar for input controls and instructions
with st.sidebar:
    st.header("Instructions")
    st.text("Enter the product details and select \n"
            "a demographic to generate a tailored \n"
            "product title and description.")
    
    # Demographic examples
    st.header("Demographic Examples")
    demographic_options = {
        "Retired lady in New Jersey": "Retired lady from New Jersey who enjoys watching movies and online shopping.",
        "Young professional in NYC": "Young professional living in NYC, interested in tech gadgets and fitness.",
        "College student": "College student from California studying remotely and interested in gaming and streaming.",
        "Outdoor enthusiast": "Outdoor enthusiast who enjoys camping and hiking, interested in sustainable products."
    }
    demographic_choice = st.selectbox("Choose a Demographic", list(demographic_options.keys()))

# Input fields for product details
product_title = st.text_input('Product Title', 'Samsung 27” Curved Monitor')
product_description = st.text_area('Product Description', 'Ultra-slim design, 1800R curvature, AMD FreeSync, 4ms response time, Eye Saver Mode.')

demographic_info = demographic_options[demographic_choice]

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