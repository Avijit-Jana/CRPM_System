import streamlit as st
from main import *
import matplotlib

def webapp():
    with st.sidebar:
        st.write('This is a Customer Relationship and Product Management (CRPM) System')

    # Create three tabs
    tab1, tab2, tab3 = st.tabs(["Customer", "Product", "Dashboard"])
    # Add content to the first tab

    with tab1:
        st.subheader("Customer Information")
        # Create two columns of equal width
        col1, col2, col3 = st.columns(3)

        with col1:
            st.text_input('Customer Name')
            st.text_input('Phone Number')
            
        with col2:
            st.selectbox('Select',['Male','Female','Other'])
            st.text_input('Email Address')

        with col3:
            st.date_input('Date of Birth')
            st.text_input('Address')
        
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
        st.button('Submit')
        
    with tab2:
        # Create two columns of equal width
        col1, col2, col3 = st.columns(3)

        # Add content to the first column
        with col1:
            st.text_input('Product Name')
            st.number_input('Price')
            
        with col2:
            st.number_input('Quantity')
            st.text_input('Order Status')

        with col3:
            st.date_input('Purchase Date')
            st.text_input('Shipping Address')

    with tab3:
        st.write('Charts')

