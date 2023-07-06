import streamlit as st
import langchain_code

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Choose a Cuisine", ("Indian", "Arabic","American","Itailan","Chinese","Japenese"))



if cuisine:
    res = langchain_code.gen_rest_name_and_item(cuisine)

    st.header(res['restaurant_name'].strip())
    menu_items = res['Menu_items'].strip().split(",")
    st.write("** Menu Items **")

    for item in menu_items:
        st.write(" - ",item)

