def show():
    import streamlit as st

    st.title("📂 Projects")

    # === Project 1 ===
    st.subheader("🥏 Ultimate Stats Tracker")
    st.image("images/tracker_screenshot.png", use_column_width=True)
    st.write("""
    A personal stats tracker I built to analyze my performance in Ultimate Frisbee games.
    
    It logs goals, assists, turnovers, and visualizes performance trends with pandas and Altair.  
    This was a fun way to combine my passion for data with the sport I love.
    """)

    st.markdown(
        '<a href="https://yunxuan-portfolio.streamlit.app" target="_blank">🔗 Live Demo</a>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<a href="https://github.com/jsr-xyx/ultimate-tracker" target="_blank">📂 GitHub Repo</a>',
        unsafe_allow_html=True
    )
