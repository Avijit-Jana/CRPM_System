import streamlit as st
import matplotlib,sqlite3


with st.sidebar:
    st.write('This is a Customer Relationship and Product Management (CRPM) System')
    
st.title('View The Data')
try:
    conn = sqlite3.connect('store.db')
    c = conn.cursor()
    c.execute('SELECT * FROM customers')
    customer = c.fetchall()
    c.execute('SELECT * FROM products')
    product = c.fetchall()
    c.execute('SELECT * FROM purchases')
    purchase = c.fetchall()
    conn.close()
except:
    st.write('Error: Unable to fetch data from the database')

tab1, tab2, tab3, dasboard = st.tabs(['Customers', 'Products', 'Purchases', 'Dashboard'])

with tab1:
    st.write('Customers')
    st.write(customer)

with tab2:
    st.write('Products')
    st.write(product)

with tab3:
    st.write('Purchases')
    st.write(purchase)

with dasboard:
    st.write('Dashboard')
    st.write('This is the dashboard')