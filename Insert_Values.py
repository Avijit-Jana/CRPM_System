import streamlit as st
import matplotlib.pyplot as plt

def webapp():
    with st.sidebar:
        st.write('This is a Customer Relationship and Product Management (CRPM) System that integrates backend functionality using Python and Object-Oriented Programming (OOP), a relational database, and a front-end framework.')

    # Create three tabs
    tab1, tab2 = st.tabs(["Customer", "Product"])

    with tab1:
        st.subheader("Customer Information")
        col1, col2, col3 = st.columns(3)

        with col1:
            customer_name = st.text_input('Customer Name', placeholder='e.g. John Doe') 
            country = st.text_input('Country', placeholder='e.g. India')
            purchase_date = st.date_input('Purchase Date')
            
        with col2:
            gender = st.selectbox('Gender',['Male','Female','Other'])
            state = st.text_input('State', placeholder='e.g. Maharashtra')
            phone = st.text_input('Phone Number', placeholder='e.g. 8965666556')

        with col3:
            age = st.number_input('Age', min_value=0, max_value=100, step=1)
            city = st.text_input('City', placeholder='e.g. Mumbai')
            email = st.text_input('Email', placeholder='e.g. abc@email.com')

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

        values = [customer_name, gender, age, country, state, city, purchase_date, phone, email, address]
        
        if st.button('Submit', key='customer'):
            st.info('Customer Information Submitted')
            from main import database
            d = database()
            d.insert_customer(values)
        
    with tab2:
        st.subheader("Product Information")
        col1, col2, col3 = st.columns(3)

        # Add content to the first column
        with col1:
            product_name = st.text_input('Product Name')
            price = st.number_input('Price')
            stock = st.number_input('Stock')
            
        with col2:
            quantity = st.number_input('Quantity')
            status = st.text_input('Order Status')
            shipping_address = st.text_input('Shipping Address').expandtabs()

        with col3:
            order_date = st.date_input('order Date')
            catagory = st.text_input('Category')

        if st.button('Submit', key='product'):
            st.info('Product Information Submitted')


if __name__ == "__main__":
    webapp()