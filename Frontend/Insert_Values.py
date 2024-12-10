import streamlit as st
from data import Database

# Global database instance
d = Database("store.db")

def validate_inputs(values):
    """Check if all inputs are non-empty or valid."""
    return all(value is not None and value != "" for value in values)

def webapp():
    with st.sidebar:
        st.write(
            "This is a Customer Relationship and Product Management (CRPM) System "
            "that integrates backend functionality using Python and Object-Oriented Programming (OOP), "
            "a relational database, and a front-end framework."
        )

    # Create two tabs
    tab1, tab2 = st.tabs(["Customer Info", "Product Info"])

    # Customer Information Section
    with tab1:
        st.subheader("Enter Customer Information")
        col1, col2, col3 = st.columns(3)

        # Input fields for customer information
        with col1:
            customer_name = st.text_input("Customer Name", placeholder="e.g. John Doe")
            country = st.text_input("Country", placeholder="e.g. India")
            email = st.text_input("Email", placeholder="e.g. abc@email.com")
            order_status = st.selectbox("Order Status", ["Delivered", "Pending", "Cancelled"])
            
        with col2:
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            state = st.text_input("State", placeholder="e.g. Maharashtra")
            phone = st.text_input("Phone Number", placeholder="e.g. 8965666556")
            product_name = st.text_input("Product Name", placeholder="e.g. iPhone 13", key="product_name_tab1")

        with col3:
            age = st.number_input("Age", min_value=0, max_value=100, step=1)
            city = st.text_input("City", placeholder="e.g. Mumbai")
            order_date = st.date_input("Order Date")
            quantity = st.number_input("Quantity", min_value=1, max_value=100, step=1)

        address = st.text_area("Address", placeholder="e.g. 123, ABC Road, XYZ Area, Mumbai")

        # Collect customer values
        customer_values = [
            customer_name, gender, age, country, state, city, str(order_date),
            phone, email, order_status, product_name, quantity, address
        ]

        st.markdown(
            """
            <style>
            .stButton > button {
                font-weight: bold;
                height: 50px;
                width: 200px;
                color: blue;
                margin: auto;
                display: block;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Submit", key="customer"):
            if validate_inputs(customer_values):
                d.add_customer(customer_values)
                st.success("Customer Information Submitted")
            else:
                st.error("Please fill in all fields.")

    # Product Information Section
    with tab2:
        st.subheader("Enter Product Information")
        col1, col2, col3 = st.columns(3)

        # Input fields for product information
        with col1:
            product_name = st.text_input("Product Name", placeholder="e.g. iPhone 13", key="product_name_tab2")
            stock = st.number_input("Stock", min_value=0, step=1)
            color = st.text_input("Product Color", placeholder="e.g. Black")
            
        with col2:
            category = st.text_input("Category", placeholder="e.g. Electronics")
            cost_price = st.number_input("Cost Price", min_value=0.0, step=0.01)
            discount = st.number_input("Discount (%)", min_value=0.0, max_value=100.0, step=0.1)

        with col3:
            brand = st.text_input("Brand", placeholder="e.g. Apple")
            unit_price = st.number_input("Unit Price", min_value=0.0, step=0.01)
            product_status = st.selectbox("Product Status", ["Available", "Out of Stock"])

        product_description = st.text_area("Product Description", placeholder="e.g. This is a product description")

        # Collect product values
        product_values = [
            product_name, stock, color, category, cost_price, discount,
            brand, unit_price, product_status, product_description
        ]

        if st.button("Submit", key="product"):
            if validate_inputs(product_values):
                d.add_product(product_values)
                st.success("Product Information Submitted")
            else:
                st.error("Please fill in all fields.")

if __name__ == "__main__":
    webapp()
