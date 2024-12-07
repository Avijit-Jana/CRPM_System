import streamlit as st
import matplotlib.pyplot as plt
from main import Database

def webapp():
    with st.sidebar:
        st.write('This is a Customer Relationship and Product Management (CRPM) System that integrates backend functionality using Python and Object-Oriented Programming (OOP), a relational database, and a front-end framework.')

    # Create three tabs
    tab1, tab2 = st.tabs(["Customer", "Product"])

    with tab1:
        st.subheader("Enter Customer Information")
        col1, col2, col3 = st.columns(3)

        with col1:
            customer_name = st.text_input('Customer Name', placeholder='e.g. John Doe') 
            country = st.text_input('Country', placeholder='e.g. India')
            email = st.text_input('Email', placeholder='e.g. abc@email.com')
            
        with col2:
            gender = st.selectbox('Gender',['Male','Female','Other'])
            state = st.text_input('State', placeholder='e.g. Maharashtra')
            phone = st.text_input('Phone Number', placeholder='e.g. 8965666556')

        with col3:
            age = st.number_input('Age', min_value=0, max_value=100, step=1)
            city = st.text_input('City', placeholder='e.g. Mumbai')
            purchase_date = st.date_input('Purchase Date')

        address = st.text_area('Address', placeholder='e.g. 123, ABC Road, XYZ Area, Mumbai')
        
        # Button CSS
        st.markdown("""
        <style>
        .stButton > button {
            font-weight: bold;
            height: 50px;
            width: 200px;
            color: blue;
            # background-color: cyan;
            display: block;
            margin: auto;
        }
        </style>
        """, unsafe_allow_html=True)

        values = [customer_name, gender, age, country, state, city, email, phone, purchase_date, address]
        
        if st.button('Submit', key='customer'):
            st.info('Customer Information Submitted')
            from main import database
            database().insert_customer(values)
        
    with tab2:
        st.subheader("Enter Product Information")
        col1, col2, col3 = st.columns(3)

        # Add content to the first column
        with col1:
            product_id = st.number_input('Product ID', step=1)
            price = st.number_input('Price')
            stock = st.number_input('Stock')
            
        with col2:
            product_name = st.text_input('Product Name', placeholder='e.g. iPhone 13')
            quantity = st.number_input('Quantity')
            status = st.text_input('Order Status', placeholder='e.g. Delivered')

        with col3:
            order_date = st.date_input('Order Date')
            catagory = st.text_input('Category', placeholder='e.g. Electronics')
            order_id = st.number_input('Order ID', step=1)

        product_description = st.text_area('Product Description', placeholder='e.g. This is a product description')

        values1 = [product_id, product_name, quantity, order_date, price, status, catagory, stock, product_description]

        if st.button('Submit', key='product'):
            st.info('Product Information Submitted')
            from main import database
            database().insert_product(values1)


if __name__ == "__main__":
    webapp()