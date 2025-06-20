def show():
    import streamlit as st
    st.title("📂 Projects")
    st.subheader("🥏 Ultimate Stats Tracker")
    st.image("images/tracker_screenshot.png", use_column_width=True)
    st.write("""
    A personal stats tracker I built to analyze performance in Ultimate Frisbee games.
    Built in Python using Streamlit and pandas. Tracks goals, throws, turnovers and visualizes trends.
    """)
    st.markdown("[🔗 Live Demo]()")
    st.markdown("[📂 GitHub Repo](https://github.com/jsr-xyx/ultimate-tracker)")
