import streamlit as st
import about, projects, contact, tracker

st.set_page_config(page_title="Jesse Xue | Portfolio", layout="wide")

st.sidebar.title("📌 Navigate")
page = st.sidebar.radio("Go to:", ["🏠 Home", "📂 Projects", "👤 About", "📫 Contact", "🥏 Ultimate Tracker"])

if page == "🏠 Home":
    st.title("Jesse Xue")
    st.subheader("Economics & Statistics Student")
    st.write("I use Python to turn real-world data into useful insight—on and off the field.")
    st.markdown("[📂 View Projects](#projects)")
    st.markdown("[📫 Contact Me](#contact)")

elif page == "📂 Projects":
    projects.show()

elif page == "👤 About":
    about.show()

elif page == "📫 Contact":
    contact.show()

elif page == "🥏 Ultimate Tracker":
    tracker.show()
