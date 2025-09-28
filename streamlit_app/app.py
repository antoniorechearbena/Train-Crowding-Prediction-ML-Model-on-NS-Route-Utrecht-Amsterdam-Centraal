import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="ML Results Dashboard",
    layout="wide",
    
)

with st.sidebar:
    st.subheader("Menu")
    if "section" not in st.session_state:
        st.session_state["section"] = "Home"
    
    selected = option_menu(
        None,
        ["Home", "ML Models"],
        icons = ["house", "cpu"],
        default_index=0,
        key = "main_menu",
        styles = {
            "container": {"padding": "0rem"},
            "icon": {"font-size": "1.1rem"},
            "nav-link":{
                "font-size": "0.95rem",
                "padding": "0.35rem 0.7rem",
                "border-radius": "8px",
                "margin": "0.15rem 0.15rem"
            },
            "nav-link-selected": {"background-color": "#4b90ff", "color": "white"},
        },
    )

if selected != st.session_state["section"]:
    st.session_state["section"] = selected
    st.rerun()
    
section = selected

if section == "Home":
    st.markdown(
        "<h1 style ='text-align: center; maring-top: 0.5rem;'>Basic User Interface</h1>",
        unsafe_allow_html = True
    )
    st.markdown(
        "<p style = 'text-align: center; font-size: 1.05rem; opacity: .85;'>"
        "Dashboard for users to check any useful information before they board their train."
        "</p>",
        unsafe_allow_html = True
    )
    st.divider()

    #Any content goes here

    st.markdown("---")
    st.markdown("""
        <div style = 'text-align: center; font-size: 0.95rem; opacity: .9;'>
            Contact:
            <a href = "mailto: antonio_reche_cazorla@hotmail.com">antonio_reche_cazorla@hotmail.com</a> 
            Linkedln: <a href = "https://linkedin.com/in/antoniorechecazorla/" target = "_blank">Antonio-Reche</a>
            GitHub: <a href = "https://github.com/antoniorechearbena" target = "_blank">github.com/antoniorechearbena</a>
        </div>        
    """,
    unsafe_allow_html=True
    )

elif section == "ML Models":
    st.header("ML Models")
    tab_overview, tab_training, tab_results = st.tabs(["Overview", "Training", "Results"])

    with tab_overview:
        st.write("Explain the purpose of the models, the problem, and the features used.")
        st.markdown("""
            - Algorithms tried
            - Why each one was chosen
            - Target Variable and label definition
        """)

    with tab_training:
        st.write("Explain how the models where train(e.g. data trained on, techniques, tuning, feature engineering, hyperparameters)")
        st.markdown("""
            - Train/Validation/Test strategy
            - Feature engineering steps
            - Tuning
            - Hyperparameters
        """)

    with tab_results:
        st.write("Summarize metrics and learning from experiments")
        st.markdown("""
            - Metrics
            - Key Comparisions and Takeaways
            - Error Analysis highlights
        """)

