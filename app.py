import streamlit as st
import about, projects, contact, tracker

# Initialize state
if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

st.set_page_config(page_title="Yunxuan (Jesse) Xue | Portfolio", layout="wide")

# Sidebar navigation based on state
page = st.sidebar.radio("Go to:", ["🏠 Home", "📂 Projects", "👤 About", "📫 Contact"], index=["🏠 Home", "📂 Projects", "👤 About", "📫 Contact"].index(st.session_state.page))

# Pages
if page == "🏠 Home":
    st.title("Yunxuan (Jesse) Xue")
    st.subheader("Economics Student | Stats Enthusiast")
    st.write("I use Python to turn real-world data into useful insight—on and off the field.")

    if st.button("📂 View Projects"):
        st.session_state.page = "📂 Projects"

    if st.button("📫 Contact Me"):
        st.session_state.page = "📫 Contact"

elif page == "📂 Projects":
    projects.show()

elif page == "👤 About":
    about.show()

elif page == "📫 Contact":
    contact.show()
