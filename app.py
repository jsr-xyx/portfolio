import streamlit as st
import about, projects, contact

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

st.set_page_config(page_title="Yunxuan (Jesse) Xue | Portfolio", layout="wide")

# Sidebar navigation
pages = ["🏠 Home", "📂 Projects", "👤 About", "📫 Contact"]
page = st.sidebar.radio("Go to:", pages, index=pages.index(st.session_state.page))
st.session_state.page = page  # Keep state in sync

# Page rendering logic
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
