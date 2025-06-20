import streamlit as st
import about, projects, contact, tracker

# Config
st.set_page_config(page_title="Yunxuan (Jesse) Xue | Portfolio", layout="wide")

# Session state to track selected section
if "section" not in st.session_state:
    st.session_state.section = "home"

# Top nav bar
st.markdown("---")
cols = st.columns([1, 1, 1, 1, 1])
with cols[0]:
    if st.button("🏠 Home"):
        st.session_state.section = "home"
with cols[1]:
    if st.button("📂 Projects"):
        st.session_state.section = "projects"
with cols[2]:
    if st.button("👤 About"):
        st.session_state.section = "about"
with cols[3]:
    if st.button("📫 Contact"):
        st.session_state.section = "contact"
with cols[4]:
    if st.button("🥏 Tracker"):
        st.session_state.section = "tracker"
st.markdown("---")

# Show section
if st.session_state.section == "home":
    st.title("Yunxuan (Jesse) Xue")
    st.subheader("Economics Student | Stats Enthusiast")
    st.write("I use Python to turn real-world data into useful insight—on and off the field.")

elif st.session_state.section == "projects":
    projects.show()

elif st.session_state.section == "about":
    about.show()

elif st.session_state.section == "contact":
    contact.show()

elif st.session_state.section == "tracker":
    tracker.show()
