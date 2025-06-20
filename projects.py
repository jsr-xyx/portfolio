import streamlit as st

def show():
    st.title("📂 Projects")

    # === Project 1: Ultimate Stats Tracker ===
    st.subheader("🥏 Ultimate Stats Tracker")

    st.write("""
    A personal app I built to track and analyze my Ultimate Frisbee performance.

    It logs game-by-game stats like goals, assists, turnovers, Ds, OB pulls, and more.  
    I also calculate plus/minus, pull success %, and visualize trends with Altair.  
    The app supports CSV export, filtering, and full stat reset — all built in Python and Streamlit.
    """)

    # GitHub link to the tracker project repo
    st.markdown(
        '<a href="https://github.com/jsr-xyx/ultimate-tracker" target="_blank">📂 View GitHub Repo</a>',
        unsafe_allow_html=True
    )

    # Link to open tracker as a separate Streamlit app
    st.markdown(
        '<a href="https://ultimate-tracker.streamlit.app" target="_blank">🚀 Open Ultimate Tracker</a>',
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.caption("More projects coming soon.")
