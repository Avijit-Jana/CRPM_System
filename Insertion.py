import streamlit as st
import matplotlib.pyplot as plt

def webapp():
    with st.sidebar:
        st.write('This is a Customer Relationship and Product Management (CRPM) System')

    # Create three tabs
    tab1, tab2, tab3 = st.tabs(["Customer", "Product", "Dashboard"])

    with tab1:
        st.subheader("Customer Information")
        col1, col2, col3 = st.columns(3)

        with col1:
            customer_name = st.text_input('Customer Name')
            country = st.text_input('Country')
            purchase_date = st.date_input('Purchase Date')
            
        with col2:
            gender = st.selectbox('Gender',['Male','Female','Other'])
            state = st.text_input('State')
            phone = st.text_input('Phone Number')

        with col3:
            age = st.number_input('Age', min_value=0, max_value=100, step=1)
            city = st.text_input('City')
            email = st.text_input('Email')

        address = st.text_area('Address')
        
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
        
        if st.button('Submit'):
            st.info('Customer Information Submitted')
            from main import database
            d = database()
            d.insert_customer(values)
        
    with tab2:
        st.subheader("Product Information")
        col1, col2, col3 = st.columns(3)

        # Add content to the first column
        with col1:
            st.text_input('Product Name')
            st.number_input('Price')
            
        with col2:
            st.number_input('Quantity')
            st.text_input('Order Status')

        with col3:
            # st.date_input('Purchase Date')
            st.text_input('Shipping Address')

    with tab3:
        st.subheader("Dasboard")
        st.write('Charts')


if __name__ == "__main__":
    webapp()