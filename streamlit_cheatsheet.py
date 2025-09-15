import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time
import random

st.set_page_config(
    page_title="Streamlit Cheat Sheet",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/icon?family=Material+Icons');
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Lato:wght@300;400;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #0F1123 0%, #090B17 100%);
        color: #ffffff;
        min-height: 100vh;
        font-family: 'Lato', sans-serif;
    }

    .main-header {
        background: transparent;
        border: 1px solid #8A4FFF;
        border-radius: 8px;
        padding: 2rem;
        margin-bottom: 2rem;
    }

    .gradient-title {
        background: linear-gradient(90deg, #8A4FFF 0%, #ffffff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Inter', sans-serif !important;
        font-weight: 700 !important;
        font-size: 3rem !important;
        margin-bottom: 0.5rem !important;
        letter-spacing: -0.025em !important;
    }

    .main-header p {
        color: #b3b3b3 !important;
        font-family: 'Lato', sans-serif;
        font-size: 1.3rem;
        font-weight: 400;
        margin: 0;
    }

    .section-card {
        background: transparent;
        border: none;
        border-radius: 0;
        padding: 0.5rem 0;
        margin: 2rem 0 1.5rem 0;
    }

    .section-card h2 {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        font-size: 1rem;
        margin: 0 0 0.5rem 0;
        letter-spacing: -0.005em;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid;
        border-image: linear-gradient(90deg, #8A4FFF 0%, transparent 100%) 1;
        display: inline-block;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(26, 29, 46, 0.6);
        border-radius: 8px;
        border: 1px solid rgba(138, 79, 255, 0.2);
        padding: 4px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 48px;
        border-radius: 6px;
        background: transparent;
        border: 1px solid transparent;
        color: #b3b3b3;
        font-weight: 500;
    }

    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: transparent;
        border: 1px solid #8A4FFF;
        color: #ffffff;
    }

    [data-testid="stCode"] {
        background: rgba(9, 11, 23, 0.8) !important;
        border: 1px solid rgba(138, 79, 255, 0.3);
        border-radius: 6px;
    }

    .stMarkdown h3 {
        color: #ffffff !important;
        font-weight: 500;
        font-size: 1rem;
    }

    .material-icons {
        font-family: 'Material Icons';
        font-weight: normal;
        font-style: normal;
        font-size: 20px;
        line-height: 1;
        letter-spacing: normal;
        text-transform: none;
        display: inline-block;
        white-space: nowrap;
        word-wrap: normal;
        direction: ltr;
        vertical-align: middle;
        margin-right: 8px;
    }

    .tab-content {
        display: flex;
        align-items: center;
    }

    .formation-hero {
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, rgba(138, 79, 255, 0.1) 0%, rgba(138, 79, 255, 0.05) 100%);
        border-radius: 16px;
        margin: 2rem 0;
    }

    .formation-hero h1 {
        font-family: 'Inter', sans-serif;
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(45deg, #8A4FFF 0%, #C777FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
    }

    .formation-hero p {
        font-size: 1.5rem;
        color: #b3b3b3;
        margin-bottom: 2rem;
    }

    .cta-button {
        display: inline-block;
        background: linear-gradient(45deg, #8A4FFF 0%, #C777FF 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
        transition: transform 0.2s ease;
    }

    .cta-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(138, 79, 255, 0.3);
    }

    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }

    .feature-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(138, 79, 255, 0.2);
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
    }

    .feature-card h3 {
        color: #8A4FFF;
        font-family: 'Inter', sans-serif;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }

    .feature-card p {
        color: #b3b3b3;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

def cheat_sheet():
    st.markdown("""
    <div class="main-header">
        <h1 class="gradient-title">Streamlit Cheat Sheet</h1>
        <p>Guide interactif des fonctionnalités Streamlit avec code et rendu côte à côte</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        ":material/settings: Installation & Bases",
        ":material/text_fields: Affichage Texte",
        ":material/analytics: Données & Graphiques",
        ":material/tune: Widgets Interactifs",
        ":material/dashboard: Mise en Page",
        ":material/flash_on: Avancé"
    ])

    with tab1:
        st.markdown("""
        <div class="section-card">
            <h2>Installation & Import</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Code:**")
            st.code("""
# Installation
pip install streamlit

# Lancer une app
streamlit run app.py

# Import convention
import streamlit as st
            """, language="bash")

        with col2:
            st.markdown("**Info:**")
            st.info("Streamlit se lance sur http://localhost:8501")
            st.write("Import toujours avec `st`")
            st.write("Auto-refresh quand le code change")

        st.markdown("""
        <div class="section-card">
            <h2>Configuration de page</h2>
        </div>
        """, unsafe_allow_html=True)

        col3, col4 = st.columns(2)

        with col3:
            st.markdown("**Code:**")
            st.code("""
st.set_page_config(
    page_title="Mon App",
    page_icon="🚀",
    layout="wide",  # ou "centered"
    initial_sidebar_state="expanded"
)
            """, language="python")

        with col4:
            st.markdown("**Résultat:**")
            st.write("Cette page utilise `layout='wide'`")
            st.write("Responsive automatique")
            st.write("Icône dans l'onglet navigateur")

    with tab2:
        st.markdown("""
        <div class="section-card">
            <h2>st.write() - Affichage universel</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code('st.write("Texte simple ou variables", variable)', language="python")
        with col2:
            st.write("Texte simple ou variables", "demo")

        st.markdown("""
        <div class="section-card">
            <h2>st.markdown() - Formatage riche</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code('st.markdown("**Texte en gras** _italique_")', language="python")
        with col2:
            st.markdown("**Texte en gras** _italique_")

        st.markdown("""
        <div class="section-card">
            <h2>st.title() - Titre principal</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code('st.title("Titre principal")', language="python")
        with col2:
            st.title("Titre principal")

        st.markdown("""
        <div class="section-card">
            <h2>st.header() - En-tête de section</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code('st.header("En-tête section")', language="python")
        with col2:
            st.header("En-tête section")

        st.markdown("""
        <div class="section-card">
            <h2>st.subheader() - Sous-titre</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code('st.subheader("Sous en-tête")', language="python")
        with col2:
            st.subheader("Sous en-tête")

        st.markdown("""
        <div class="section-card">
            <h2>st.caption() - Texte de légende</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code('st.caption("Texte de légende petit")', language="python")
        with col2:
            st.caption("Texte de légende petit")

        st.markdown("""
        <div class="section-card">
            <h2>st.text() - Texte brut</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code('st.text("Texte brut sans formatage")', language="python")
        with col2:
            st.text("Texte brut sans formatage")

        st.markdown("""
        <div class="section-card">
            <h2>st.latex() - Formules mathématiques</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code(r'st.latex(r"\\sum_{i=1}^{n} x_i^2")', language="python")
        with col2:
            st.latex(r"\sum_{i=1}^{n} x_i^2")

        st.markdown("""
        <div class="section-card">
            <h2>st.code() - Code avec coloration</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code("""st.code('''
def hello(name):
    return f"Hello {name}!"
''', language='python')""", language="python")
        with col2:
            st.code('''def hello(name):
    return f"Hello {name}!"''', language='python')

    with tab3:
        # DataFrame demo data
        df_demo = pd.DataFrame({
            'Nom': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'Score': [85, 92, 78]
        })

        st.markdown("""
        <div class="section-card">
            <h2>st.dataframe() - Tableau interactif</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code("""df = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 92, 78]
})
st.dataframe(df, use_container_width=True)""", language="python")
        with col2:
            st.dataframe(df_demo, use_container_width=True)

        st.markdown("""
        <div class="section-card">
            <h2>st.table() - Tableau statique</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code('st.table(df)', language="python")
        with col2:
            st.table(df_demo)

        st.markdown("""
        <div class="section-card">
            <h2>st.json() - Affichage JSON</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code('st.json({"nom": "Alice", "age": 25})', language="python")
        with col2:
            st.json({"nom": "Alice", "age": 25})

        st.markdown("""
        <div class="section-card">
            <h2>st.metric() - Métriques avec variation</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code('st.metric("Ventes", "1,234", "12%")', language="python")
        with col2:
            st.metric("Ventes", "1,234", "12%")

        # Chart demo data
        chart_data = pd.DataFrame({
            'valeurs': [1, 3, 2, 4, 5, 3, 6, 4, 7, 5]
        })

        st.markdown("""
        <div class="section-card">
            <h2>st.line_chart() - Graphique linéaire</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code("""chart_data = pd.DataFrame({
    'valeurs': [1, 3, 2, 4, 5, 3, 6, 4, 7, 5]
})
st.line_chart(chart_data)""", language="python")
        with col2:
            st.line_chart(chart_data)

        st.markdown("""
        <div class="section-card">
            <h2>st.bar_chart() - Graphique en barres</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code('st.bar_chart(chart_data)', language="python")
        with col2:
            st.bar_chart(chart_data)

        st.markdown("""
        <div class="section-card">
            <h2>st.area_chart() - Graphique en aires</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code('st.area_chart(chart_data)', language="python")
        with col2:
            st.area_chart(chart_data)

        st.markdown("""
        <div class="section-card">
            <h2>st.scatter_chart() - Nuage de points</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code('st.scatter_chart(chart_data)', language="python")
        with col2:
            st.scatter_chart(chart_data)

        st.markdown("""
        <div class="section-card">
            <h2>st.map() - Carte interactive</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code("""map_data = pd.DataFrame({
    'lat': [48.8566, 45.7640],
    'lon': [2.3522, 4.8357]
})
st.map(map_data)""", language="python")
        with col2:
            map_data = pd.DataFrame({
                'lat': [48.8566, 45.7640],
                'lon': [2.3522, 4.8357]
            })
            st.map(map_data)

        st.markdown("""
        <div class="section-card">
            <h2>st.plotly_chart() - Graphiques Plotly Express</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code("""import plotly.express as px

fig = px.scatter(
    df, x="Age", y="Score",
    color="Nom", size="Age",
    title="Age vs Score"
)
st.plotly_chart(fig, use_container_width=True)""", language="python")
        with col2:
            fig_scatter = px.scatter(
                df_demo, x="Age", y="Score",
                color="Nom", size="Age",
                title="Age vs Score",
                color_discrete_sequence=['#8A4FFF', '#C777FF', '#667eea']
            )
            fig_scatter.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white')
            )
            st.plotly_chart(fig_scatter, use_container_width=True)

        st.markdown("""
        <div class="section-card">
            <h2>st.plotly_chart() - Graphiques Graph Objects</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code("""import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Bar(
    x=['A', 'B', 'C'],
    y=[1, 3, 2],
    marker_color='#8A4FFF'
))
fig.update_layout(title="Custom Bar Chart")
st.plotly_chart(fig, use_container_width=True)""", language="python")
        with col2:
            fig_bar = go.Figure()
            fig_bar.add_trace(go.Bar(
                x=['A', 'B', 'C'],
                y=[1, 3, 2],
                marker_color='#8A4FFF'
            ))
            fig_bar.update_layout(
                title="Custom Bar Chart",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white')
            )
            st.plotly_chart(fig_bar, use_container_width=True)

    with tab4:
        st.markdown("""
        <div class="section-card">
            <h2>Widgets de saisie</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Code:**")
            st.code("""
# Saisie de texte
name = st.text_input("Nom", "Défaut")
description = st.text_area("Description")

# Nombres
age = st.number_input("Age", 0, 100, 25)
score = st.slider("Score", 0, 100, 50)

# Sélection
option = st.selectbox("Choix", ["A", "B", "C"])
options = st.multiselect("Multi", ["X", "Y", "Z"])

# Dates
date = st.date_input("Date")
time = st.time_input("Heure")

# Fichiers
uploaded = st.file_uploader("Upload", type=['csv'])

# Audio et caméra
audio = st.audio_input("Enregistrer audio")
photo = st.camera_input("Prendre photo")

# Chat input (pour chatbots)
chat_input = st.chat_input("Tapez votre message")

# Couleur
color = st.color_picker("Couleur")

# Feedback
feedback = st.feedback("thumbs")
feedback_faces = st.feedback("faces")
            """, language="python")

        with col2:
            st.markdown("**Résultat:**")

            # Saisie de texte
            name_demo = st.text_input("Nom", "Défaut", key="name_demo")
            description_demo = st.text_area("Description", key="desc_demo")

            # Nombres
            age_demo = st.number_input("Age", 0, 100, 25, key="age_demo")
            score_demo = st.slider("Score", 0, 100, 50, key="score_demo")

            # Sélection
            option_demo = st.selectbox("Choix", ["A", "B", "C"], key="option_demo")
            options_demo = st.multiselect("Multi", ["X", "Y", "Z"], key="multi_demo")

            # Dates
            date_demo = st.date_input("Date", key="date_demo")
            time_demo = st.time_input("Heure", key="time_demo")

            # Fichiers
            uploaded_demo = st.file_uploader("Upload", type=['csv'], key="upload_demo")

            # Audio et caméra
            audio_demo = st.audio_input("Enregistrer audio", key="audio_demo")
            photo_demo = st.camera_input("Prendre photo", key="photo_demo")

            # Chat input (pour chatbots)
            chat_input_demo = st.chat_input("Tapez votre message", key="chat_demo")

            # Couleur
            color_demo = st.color_picker("Couleur", key="color_demo")

            # Feedback
            feedback_demo = st.feedback("thumbs", key="feedback_demo")
            feedback_faces_demo = st.feedback("faces", key="faces_demo")

        st.markdown("""
        <div class="section-card">
            <h2>Boutons et contrôles</h2>
        </div>
        """, unsafe_allow_html=True)

        col3, col4 = st.columns(2)

        with col3:
            st.markdown("**Code:**")
            st.code("""
# Boutons
if st.button("Cliquer"):
    st.write("Cliqué!")

# Cases à cocher
agree = st.checkbox("J'accepte")
if agree:
    st.success("Accepté!")

# Boutons radio
choice = st.radio("Choix", ["Oui", "Non"])

# Toggle
enabled = st.toggle("Activer")

# Pills
pill = st.pills("Choisir", ["Option 1", "Option 2", "Option 3"])

# Segmented Control
segment = st.segmented_control(
    "Mode", ["Light", "Dark", "Auto"],
    default="Light"
)

# Download button
csv_data = df.to_csv()
st.download_button(
    "Télécharger CSV",
    csv_data,
    "data.csv",
    "text/csv"
)
            """, language="python")

        with col4:
            st.markdown("**Résultat:**")

            # Boutons
            if st.button("Cliquer", key="test_btn"):
                st.write("Cliqué!")

            # Cases à cocher
            agree_demo = st.checkbox("J'accepte", key="agree_demo")
            if agree_demo:
                st.success("Accepté!")

            # Boutons radio
            choice_demo = st.radio("Choix", ["Oui", "Non"], key="radio_demo")

            # Toggle
            enabled_demo = st.toggle("Activer", key="toggle_demo")

            # Pills
            pill_demo = st.pills("Choisir", ["Option 1", "Option 2", "Option 3"], key="pills_demo")

            # Segmented Control
            segment_demo = st.segmented_control(
                "Mode", ["Light", "Dark", "Auto"],
                default="Light", key="segment_demo"
            )

            # Download button
            csv_data = "nom,age\nAlice,25\nBob,30"
            st.download_button(
                "Télécharger CSV",
                csv_data,
                "data.csv",
                "text/csv",
                key="download_demo"
            )

    with tab5:
        st.markdown("""
        <div class="section-card">
            <h2>Layout - Colonnes et containers</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Code:**")
            st.code("""
# Colonnes
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Colonne 1")
with col2:
    st.write("Colonne 2")
with col3:
    st.write("Colonne 3")

# Colonnes avec ratios
col_a, col_b = st.columns([2, 1])
with col_a:
    st.write("Large (2/3)")
with col_b:
    st.write("Petite (1/3)")

# Container
with st.container():
    st.write("Dans un container")
    st.button("Bouton container")

# Sidebar
st.sidebar.write("Dans la sidebar")
st.sidebar.button("Bouton sidebar")
            """, language="python")

        with col2:
            st.markdown("**Résultat:**")

            st.markdown("*3 colonnes égales:*")
            demo_col1, demo_col2, demo_col3 = st.columns(3)
            with demo_col1:
                st.info("Col 1")
            with demo_col2:
                st.info("Col 2")
            with demo_col3:
                st.info("Col 3")

            st.markdown("*Colonnes avec ratio 2:1:*")
            demo_col_a, demo_col_b = st.columns([2, 1])
            with demo_col_a:
                st.success("Large (2/3)")
            with demo_col_b:
                st.warning("Petite (1/3)")

        st.markdown("""
        <div class="section-card">
            <h2>Expandeurs et onglets</h2>
        </div>
        """, unsafe_allow_html=True)

        col3, col4 = st.columns(2)

        with col3:
            st.markdown("**Code:**")
            st.code("""
# Expandeur
with st.expander("Voir plus"):
    st.write("Contenu caché")
    st.slider("Slider caché", 0, 10)

# Onglets dans du contenu
tab_a, tab_b = st.tabs(["Tab A", "Tab B"])
with tab_a:
    st.write("Contenu A")
with tab_b:
    st.write("Contenu B")

# Empty placeholder
placeholder = st.empty()
placeholder.write("Texte initial")
# Plus tard:
# placeholder.write("Texte mis à jour")

# Popover
with st.popover("Ouvrir popover"):
    st.write("Contenu du popover")
            """, language="python")

        with col4:
            st.markdown("**Résultat:**")

            with st.expander("Cliquer pour développer"):
                st.write("Contenu qui était masqué")
                demo_slider = st.slider("Slider dans expandeur", 0, 10, 5, key="exp_slider")

            demo_tab_a, demo_tab_b = st.tabs(["Demo A", "Demo B"])
            with demo_tab_a:
                st.write("Contenu de l'onglet A")
            with demo_tab_b:
                st.write("Contenu de l'onglet B")

    with tab6:
        st.markdown("""
        <div class="section-card">
            <h2>Messages et statuts</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Code:**")
            st.code("""
# Messages de statut
st.success("Opération réussie!")
st.info("Information")
st.warning("Attention!")
st.error("Erreur!")

# Alertes
st.balloons()  # Animation ballons
st.snow()      # Animation neige

# Toast notifications
st.toast("Message toast", icon='🎉')

# Progress bar
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)

# Spinner
with st.spinner('Chargement...'):
    time.sleep(2)
    st.success('Terminé!')
            """, language="python")

        with col2:
            st.markdown("**Résultat:**")
            st.success("Opération réussie!")
            st.info("Information importante")
            st.warning("Attention requise")
            st.error("Erreur détectée")

            if st.button("Lancer toast", key="toast_btn"):
                st.toast("Message toast envoyé!", icon='🎉')

            if st.button("Animation ballons", key="balloons_btn"):
                st.balloons()

        st.markdown("""
        <div class="section-card">
            <h2>Cache et session state</h2>
        </div>
        """, unsafe_allow_html=True)

        col3, col4 = st.columns(2)

        with col3:
            st.markdown("**Code:**")
            st.code("""
# Cache pour données
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

# Cache pour ressources
@st.cache_resource
def init_model():
    return load_model("model.pkl")

# Session State
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment"):
    st.session_state.counter += 1

st.write(f"Compteur: {st.session_state.counter}")

# Query parameters
st.query_params["page"] = "home"
current_page = st.query_params.get("page", "default")

# Formulaires
with st.form("my_form"):
    name = st.text_input("Nom")
    age = st.number_input("Age", 0, 100)
    submitted = st.form_submit_button("Valider")
    if submitted:
        st.write(f"Nom: {name}, Age: {age}")
            """, language="python")

        with col4:
            st.markdown("**Résultat:**")

            # Session state demo
            if 'demo_counter' not in st.session_state:
                st.session_state.demo_counter = 0

            col_inc, col_reset = st.columns(2)
            with col_inc:
                if st.button("+ Increment", key="inc_demo"):
                    st.session_state.demo_counter += 1
            with col_reset:
                if st.button("Reset", key="reset_demo"):
                    st.session_state.demo_counter = 0

            st.write(f"Compteur: {st.session_state.demo_counter}")

            # Form demo
            with st.form("demo_form", clear_on_submit=True):
                form_name = st.text_input("Votre nom", key="form_name")
                form_age = st.number_input("Votre âge", 0, 100, 25, key="form_age")
                form_submitted = st.form_submit_button("Envoyer")
                if form_submitted:
                    st.success(f"Formulaire envoyé! Nom: {form_name}, Age: {form_age}")

        st.markdown("""
        <div class="section-card">
            <h2>Fonctionnalités avancées</h2>
        </div>
        """, unsafe_allow_html=True)

        col5, col6 = st.columns(2)

        with col5:
            st.markdown("**Code:**")
            st.code("""
# Fragments (performance)
@st.fragment
def expensive_chart():
    # Code coûteux qui ne se ré-exécute que si nécessaire
    return st.line_chart(data)

# Dialogue modal
@st.dialog("Mon dialogue")
def show_dialog():
    st.write("Contenu du dialogue")
    if st.button("Fermer"):
        st.rerun()

if st.button("Ouvrir dialogue"):
    show_dialog()

# Secrets (configuration)
api_key = st.secrets["api_key"]

# Colonnes avec largeurs personnalisées
col1, col2, col3 = st.columns([1, 2, 1])

# HTML et CSS custom
st.markdown('''
<div style="background: red; padding: 10px;">
    HTML personnalisé
</div>
''', unsafe_allow_html=True)
            """, language="python")

        with col6:
            st.markdown("**Info avancées:**")
            st.info("**@st.cache_data** : Pour DataFrames, listes, dictionnaires")
            st.info("**@st.cache_resource** : Pour modèles ML, connexions DB")
            st.info("**@st.fragment** : Optimisation performance")
            st.success("**st.secrets** : Variables d'environnement sécurisées")
            st.warning("**st.query_params** : Gestion des paramètres URL")
            st.error("Le cache accélère drastiquement vos apps!")

            if st.button("Test rerun", key="rerun_btn"):
                st.success("Page rechargée!")
                st.rerun()

        st.markdown("""
        <div class="section-card">
            <h2>Authentification et sécurité</h2>
        </div>
        """, unsafe_allow_html=True)

        col7, col8 = st.columns(2)

        with col7:
            st.markdown("**Code:**")
            st.code("""
# Login simple avec session state
def login_page():
    st.title("Connexion")
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        if check_credentials(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error("Identifiants incorrects")

def check_credentials(username, password):
    # En production, utiliser une vraie DB
    users = {"admin": "password123", "user": "secret"}
    return users.get(username) == password

# Protection de page
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_page()
else:
    st.write(f"Connecté en tant que: {st.session_state.username}")
    if st.button("Déconnexion"):
        st.session_state.logged_in = False
        st.rerun()
            """, language="python")

        with col8:
            st.markdown("**Résultat (démo):**")

            # Simple auth demo
            if "demo_logged_in" not in st.session_state:
                st.session_state.demo_logged_in = False

            if not st.session_state.demo_logged_in:
                st.markdown("*Interface de connexion:*")
                demo_username = st.text_input("Nom d'utilisateur", key="demo_user")
                demo_password = st.text_input("Mot de passe", type="password", key="demo_pass")

                if st.button("Se connecter", key="demo_login"):
                    if demo_username == "admin" and demo_password == "demo":
                        st.session_state.demo_logged_in = True
                        st.session_state.demo_username = demo_username
                        st.success("Connexion réussie!")
                        st.rerun()
                    else:
                        st.error("Utilisez: admin / demo")
            else:
                st.success(f"Connecté: {st.session_state.get('demo_username', 'admin')}")
                if st.button("Déconnexion", key="demo_logout"):
                    st.session_state.demo_logged_in = False
                    st.rerun()

        st.markdown("""
        <div class="section-card">
            <h2>Hashing et sécurité avancée</h2>
        </div>
        """, unsafe_allow_html=True)

        col9, col10 = st.columns(2)

        with col9:
            st.markdown("**Code:**")
            st.code("""
import hashlib
import hmac

# Hashing des mots de passe
def hash_password(password, salt):
    return hashlib.pbkdf2_hmac('sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        100000)

# Vérification sécurisée
def verify_password(password, salt, hashed):
    return hmac.compare_digest(
        hash_password(password, salt),
        hashed
    )

# Utilisation avec Streamlit-Authenticator
# pip install streamlit-authenticator
import streamlit_authenticator as stauth

# Configuration
credentials = {
    'usernames': {
        'admin': {
            'email': 'admin@example.com',
            'name': 'Admin User',
            'password': '$2b$12$...'  # Hash bcrypt
        }
    }
}

authenticator = stauth.Authenticate(
    credentials,
    'app_name',
    'secret_key',
    cookie_expiry_days=30
)

name, authentication_status, username = authenticator.login()

if authentication_status == True:
    st.write(f'Bienvenue {name}')
    authenticator.logout('Logout', 'sidebar')
elif authentication_status == False:
    st.error('Username/password is incorrect')
            """, language="python")

        with col10:
            st.markdown("**Info sécurité:**")
            st.warning("⚠️ **Jamais** de mots de passe en plain text")
            st.info("🔒 **Utilisez** des librairies comme `streamlit-authenticator`")
            st.success("✅ **Hash** avec bcrypt ou pbkdf2")
            st.error("🚫 **Pas de secrets** dans le code source")

            st.markdown("**Bonnes pratiques:**")
            st.markdown("""
            - Utilisez `st.secrets` pour les clés API
            - Hash des mots de passe avec salt
            - Sessions avec expiration
            - HTTPS en production
            - Validation côté serveur
            """)

            st.code("""
# secrets.toml
[passwords]
admin_hash = "$2b$12$..."
api_key = "your-secret-key"

# Utilisation
admin_hash = st.secrets["passwords"]["admin_hash"]
            """, language="toml")

        st.markdown("""
        <div class="section-card">
            <h2>Interface de chat (ChatGPT-like)</h2>
        </div>
        """, unsafe_allow_html=True)

        col11, col12 = st.columns(2)

        with col11:
            st.markdown("**Code:**")
            st.code("""
# Chat complet avec historique
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Bonjour! Comment puis-je vous aider?"}
    ]

# Afficher l'historique
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input utilisateur
if prompt := st.chat_input("Tapez votre message"):
    # Ajouter message utilisateur
    st.session_state.chat_history.append(
        {"role": "user", "content": prompt}
    )

    # Afficher le message utilisateur
    with st.chat_message("user"):
        st.markdown(prompt)

    # Générer réponse (simulation)
    response = f"Echo: {prompt}"

    # Afficher avec streaming effect
    with st.chat_message("assistant"):
        response_stream = st.write_stream([c for c in response])

    # Ajouter à l'historique
    st.session_state.chat_history.append(
        {"role": "assistant", "content": response}
    )

# Effacer historique
if st.button("Effacer chat"):
    st.session_state.chat_history = []
    st.rerun()
            """, language="python")

        with col12:
            st.markdown("**Résultat (chat démo):**")

            # Initialize demo chat history
            if "demo_chat_history" not in st.session_state:
                st.session_state.demo_chat_history = [
                    {"role": "assistant", "content": "Bonjour! Je suis votre assistant demo. Comment puis-je vous aider?"}
                ]

            # Display chat messages in a container with fixed height
            chat_container = st.container(height=300)
            with chat_container:
                for message in st.session_state.demo_chat_history:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

            # Chat input
            if prompt := st.chat_input("Votre message demo", key="demo_chat"):
                # Add user message
                st.session_state.demo_chat_history.append(
                    {"role": "user", "content": prompt}
                )

                # Generate response
                responses = [
                    f"Intéressant! Vous avez dit: '{prompt}'",
                    f"Je comprends que vous mentionnez: {prompt}",
                    f"C'est une bonne question sur: {prompt}",
                    f"Merci pour votre message: '{prompt}'"
                ]
                response = random.choice(responses)

                # Add assistant response
                st.session_state.demo_chat_history.append(
                    {"role": "assistant", "content": response}
                )

                st.rerun()

            if st.button("Effacer chat demo", key="clear_demo_chat"):
                st.session_state.demo_chat_history = [
                    {"role": "assistant", "content": "Chat effacé! Comment puis-je vous aider?"}
                ]
                st.rerun()

def formation():
    # Container pour centrer le contenu
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        # Hero Section
        st.markdown("""
        <div class="formation-hero">
            <h1>Arrêtez de livrer des POCs.<br/>Construisez de <span style="background: linear-gradient(45deg, #8A4FFF 0%, #C777FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">vraies applications web</span> avec Streamlit.</h1>
            <p>La seule formation pour transformer vos scripts Streamlit en applications de production scalables, sécurisées et prêtes pour l'entreprise.</p>
            <a href="https://www.mes-formations-data.fr/formation/streamlit-unleashed" class="cta-button" style="color: white;">Passer au niveau supérieur</a>
            <p style="margin-top: 1rem; font-size: 0.9rem; opacity: 0.7;">Pour les Data Scientists & Développeurs qui veulent aller plus loin.</p>
        </div>
        """, unsafe_allow_html=True)

        # Social Proof
        st.markdown("""
        <div style="text-align: center; padding: 2rem 0; margin-bottom: 3rem;">
            <p style="font-size: 0.8rem; font-weight: 600; color: #666; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 1rem;">Des compétences utilisées par les équipes de</p>
            <div style="display: flex; justify-content: center; gap: 2rem; opacity: 0.4; flex-wrap: wrap;">
                <span style="font-weight: bold; font-size: 1.2rem;">DataCorp</span>
                <span style="font-weight: bold; font-size: 1.2rem;">AI Startup</span>
                <span style="font-weight: bold; font-size: 1.2rem;">Big Tech</span>
                <span style="font-weight: bold; font-size: 1.2rem;">FinTech Inc</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Problem Agitation
        st.markdown("""
        <div style="text-align: center; margin: 4rem 0;">
            <p style="font-size: 0.8rem; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; background: linear-gradient(45deg, #8A4FFF 0%, #C777FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 1rem;">LE MUR DU POC</p>
            <h2 style="font-size: 2.5rem; font-weight: bold; margin-bottom: 3rem; line-height: 1.2;">Votre application Streamlit stagne à 80% ?</h2>
        </div>
        """, unsafe_allow_html=True)

        # Problem Cards
        col_a, col_b = st.columns(2)

        with col_a:
            st.markdown("""
            <div class="feature-card" style="border-left: 4px solid #8A4FFF;">
                <h3>📝 Code "Plat de Spaghettis"</h3>
                <p>Votre app.py fait 1000 lignes. Ajouter une feature devient un cauchemar de maintenance.</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="feature-card" style="border-left: 4px solid #8A4FFF;">
                <h3>🔒 Sécurité Inexistante</h3>
                <p>Aucune authentification. N'importe qui peut accéder aux données. Impensable en production.</p>
            </div>
            """, unsafe_allow_html=True)

        with col_b:
            st.markdown("""
            <div class="feature-card" style="border-left: 4px solid #8A4FFF;">
                <h3>🐌 Performance en Chute Libre</h3>
                <p>L'application est lente avec plus de 1000 lignes de données. Le cache par défaut ne suffit plus.</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="feature-card" style="border-left: 4px solid #8A4FFF;">
                <h3>🚀 Déploiement Artisanal</h3>
                <p>Vous déployez encore à la main ? La moindre mise à jour est un processus manuel, lent et risqué.</p>
            </div>
            """, unsafe_allow_html=True)

        # Program Section
        st.markdown("""
        <div style="text-align: center; margin: 6rem 0 4rem 0;">
            <p style="font-size: 0.8rem; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; background: linear-gradient(45deg, #8A4FFF 0%, #C777FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 1rem;">L'ARSENAL PRO</p>
            <h2 style="font-size: 2.5rem; font-weight: bold; margin-bottom: 1rem; line-height: 1.2;">La méthode pour passer de l'expérimentation à l'excellence</h2>
            <p style="font-size: 1.1rem; color: #b3b3b3; max-width: 600px; margin: 0 auto;">Chaque module est conçu pour vous faire franchir une étape clé vers une application de calibre "entreprise".</p>
        </div>
        """, unsafe_allow_html=True)

        # Modules
        st.markdown("""
        <div class="feature-card" style="background: linear-gradient(135deg, rgba(138, 79, 255, 0.1) 0%, rgba(138, 79, 255, 0.05) 100%); border: 1px solid rgba(138, 79, 255, 0.3); margin-bottom: 2rem;">
            <span style="font-weight: bold; background: linear-gradient(45deg, #8A4FFF 0%, #C777FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">Module 1 & 2</span>
            <h3 style="font-size: 1.8rem; margin: 1rem 0;">🏗️ Architecture & Design System</h3>
            <p>Arrêtez de coder dans un seul fichier. Nous implémentons une structure de projet modulaire, un design system digne d'une startup (CSS, thèmes) et une navigation multi-pages intelligente qui scale.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card" style="background: linear-gradient(135deg, rgba(138, 79, 255, 0.1) 0%, rgba(138, 79, 255, 0.05) 100%); border: 1px solid rgba(138, 79, 255, 0.3); margin-bottom: 2rem;">
            <span style="font-weight: bold; background: linear-gradient(45deg, #8A4FFF 0%, #C777FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">Module 3 & 4</span>
            <h3 style="font-size: 1.8rem; margin: 1rem 0;">⚡ Performance & Sécurité</h3>
            <p>Chargez 100k+ lignes de données en un clin d'œil avec des stratégies de cache avancées. Implémentez une authentification robuste (OAuth2, JWT) et un contrôle d'accès basé sur les rôles (RBAC).</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card" style="background: linear-gradient(135deg, rgba(138, 79, 255, 0.1) 0%, rgba(138, 79, 255, 0.05) 100%); border: 1px solid rgba(138, 79, 255, 0.3);">
            <span style="font-weight: bold; background: linear-gradient(45deg, #8A4FFF 0%, #C777FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">Module 5 & 6</span>
            <h3 style="font-size: 1.8rem; margin: 1rem 0;">🔄 DevOps & Stratégie</h3>
            <p>Passez au niveau supérieur avec un pipeline CI/CD complet sur GitHub Actions qui déploie automatiquement votre app conteneurisée (Docker) sur le cloud en moins de 5 minutes. Apprenez à documenter et justifier le ROI de votre projet à vos décideurs.</p>
        </div>
        """, unsafe_allow_html=True)

        # Final Project
        st.markdown("""
        <div style="background: rgba(138, 79, 255, 0.1); border: 1px solid #8A4FFF; border-radius: 12px; padding: 2rem; margin: 2rem 0; text-align: center;">
            <h3 style="color: #8A4FFF; font-size: 1.5rem; margin-bottom: 1rem;">💎 Projet Final : Application de Production Complète</h3>
            <p>Nous assemblons toutes ces briques pour construire une application multi-pages, sécurisée, performante et avec un déploiement automatisé. Le projet parfait pour votre portfolio.</p>
        </div>
        """, unsafe_allow_html=True)

        # Testimonials
        st.markdown("""
        <div style="text-align: center; margin: 6rem 0 4rem 0;">
            <p style="font-size: 0.8rem; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; background: linear-gradient(45deg, #8A4FFF 0%, #C777FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 1rem;">RÉSULTATS CONCRETS</p>
            <h2 style="font-size: 2.5rem; font-weight: bold; margin-bottom: 3rem; line-height: 1.2;">Ils ont transformé leurs POCs en succès.</h2>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div class="feature-card">
                <h4 style="font-size: 1.3rem; margin-bottom: 1rem;">"Mon app est enfin scalable."</h4>
                <p style="margin-bottom: 1.5rem;">"Mon POC fonctionnait pour 10 utilisateurs, mais s'effondrait sous la charge. Grâce au module sur la performance et l'architecture, l'app est maintenant utilisée par toute la boîte."</p>
                <div style="display: flex; align-items: center;">
                    <div style="width: 40px; height: 40px; background: #8A4FFF; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 1rem; color: white; font-weight: bold;">A</div>
                    <div>
                        <p style="font-weight: bold; margin: 0;">Alex</p>
                        <p style="font-size: 0.9rem; opacity: 0.7; margin: 0;">Data Scientist Senior</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="feature-card">
                <h4 style="font-size: 1.3rem; margin-bottom: 1rem;">"J'ai pu sécuriser les données."</h4>
                <p style="margin-bottom: 1.5rem;">"L'IT refusait de valider mon projet à cause des failles de sécurité. J'ai implémenté l'authentification OAuth2 et le RBAC. L'application est maintenant validée et déployée sur l'infra de l'entreprise."</p>
                <div style="display: flex; align-items: center;">
                    <div style="width: 40px; height: 40px; background: #C777FF; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 1rem; color: white; font-weight: bold;">S</div>
                    <div>
                        <p style="font-weight: bold; margin: 0;">Sophie</p>
                        <p style="font-size: 0.9rem; opacity: 0.7; margin: 0;">BI Developer</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class="feature-card">
                <h4 style="font-size: 1.3rem; margin-bottom: 1rem;">"La CI/CD a tout changé."</h4>
                <p style="margin-bottom: 1.5rem;">"Je passais des heures à déployer manuellement. Mettre en place le pipeline avec GitHub Actions a été une révélation. Je peux livrer de nouvelles features en quelques minutes, sans stress."</p>
                <div style="display: flex; align-items: center;">
                    <div style="width: 40px; height: 40px; background: #667eea; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 1rem; color: white; font-weight: bold;">J</div>
                    <div>
                        <p style="font-weight: bold; margin: 0;">Julien</p>
                        <p style="font-size: 0.9rem; opacity: 0.7; margin: 0;">Analytics Engineer</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Pricing Section
        st.markdown("""
        <div id="pricing" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(138, 79, 255, 0.2); border-radius: 12px; padding: 3rem; margin: 4rem 0;">
            <h2 style="font-size: 2rem; font-weight: bold; margin-bottom: 2rem;">L'arsenal complet pour la production</h2>
            <p style="color: #b3b3b3; margin-bottom: 2rem;">Recevez un accès à vie à toutes les compétences pour devenir un expert des applications Streamlit professionnelles.</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown("""
            **6 Modules de formation avancée** (Design System, Archi, Perf, Sécu, DevOps...)

            **Tous les templates de code** (Docker, CI/CD, config.toml...)

            **Le projet final complet** pour votre portfolio

            ---

            **3 bonus pour aller plus vite :**
            - 🎁 **Bibliothèque de Composants Pro**
            - 🎁 **Accès au Groupe Privé Discord**
            - 🎁 **Template de Business Case ROI**
            """)

        with col2:
            st.markdown("""
            <div style="background: rgba(0,0,0,0.3); padding: 2rem; border-radius: 12px; text-align: center; border: 1px solid rgba(138, 79, 255, 0.2);">
                <div style="background: linear-gradient(45deg, #ff6b6b, #ee5a24); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: bold; margin-bottom: 1rem; display: inline-block;">
                    🔥 EARLY BIRD - Jusqu'au 1er octobre
                </div>
                <p style="color: #b3b3b3; font-size: 0.9rem;">Votre montée en compétence</p>
                <div style="display: flex; align-items: center; justify-content: center; gap: 1rem; margin: 1rem 0;">
                    <span style="font-size: 1.5rem; text-decoration: line-through; opacity: 0.5; color: #666;">147€</span>
                    <h3 style="font-size: 3rem; font-weight: 900; margin: 0; background: linear-gradient(45deg, #8A4FFF 0%, #C777FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">97€</h3>
                </div>
                <p style="font-size: 0.9rem; margin-bottom: 1rem; color: #b3b3b3;">Accès complet et à vie</p>
                <p style="font-size: 0.8rem; color: #ff6b6b; font-weight: bold;">Prix normal: 147€ dès le 1er octobre</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <a href="https://www.mes-formations-data.fr/formation/streamlit-unleashed" class="cta-button" style="display: block; text-align: center; text-decoration: none; margin-top: 1rem; color: white;">
                Rejoindre la formation
            </a>
            """, unsafe_allow_html=True)

            st.markdown("""
            <p style="text-align: center; font-size: 0.8rem; opacity: 0.6; margin-top: 1rem;">Paiement 100% sécurisé</p>
            """, unsafe_allow_html=True)

        # FAQ
        st.markdown("""
        <div style="text-align: center; margin: 6rem 0 3rem 0;">
            <h2 style="font-size: 2.5rem; font-weight: bold;">Vous avez des questions ?</h2>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("🎯 À qui s'adresse cette formation ?"):
            st.markdown("""
            Cette formation est pour les **Data Scientists**, **Analysts**, **BI Developers** et **Développeurs Python** qui ont déjà créé au moins un POC avec Streamlit et qui se sentent limités pour le passer en production de manière professionnelle.
            """)

        with st.expander("❌ Ce n'est pas pour les débutants complets ?"):
            st.markdown("""
            Non. Nous ne revenons pas sur les bases de `st.write()` ou `st.slider()`. Nous partons du principe que vous connaissez déjà les **fondamentaux de Streamlit et de Python/Pandas**.
            """)

        with st.expander("🛠️ Quels outils allons-nous utiliser ?"):
            st.markdown("""
            En plus de Streamlit, nous utiliserons des outils standards de l'industrie comme **Docker**, **GitHub Actions**, **Pydantic**, ainsi que des services de déploiement cloud comme **HuggingFace Spaces** ou **Railway**.
            """)

        # Final CTA
        st.markdown(
            """
<div style="text-align: center; margin: 6rem 0; padding: 4rem 2rem; background: linear-gradient(135deg, rgba(138, 79, 255, 0.1) 0%, rgba(138, 79, 255, 0.05) 100%); border-radius: 16px;">
    <h2 style="font-size: 2.5rem; font-weight: bold; margin-bottom: 1rem;">Passez au niveau supérieur.</h2>
    <p style="font-size: 1.1rem; color: #b3b3b3; max-width: 600px; margin: 0 auto 2rem auto;">Arrêtez de bricoler. Devenez l'expert qui livre des applications data professionnelles, robustes et appréciées.</p>
    <a href="https://www.mes-formations-data.fr/formation/streamlit-unleashed" class="cta-button" style="display: inline-block; text-decoration: none; font-size: 1.1rem; padding: 1rem 2rem; color: white;">
        Je professionnalise mes apps
    </a>
    <div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid rgba(138, 79, 255, 0.2);">
        <div style="font-size: 2rem; margin-bottom: 1rem;">🛡️</div>
        <h3 style="font-weight: bold; margin-bottom: 1rem;">Garantie 100% sans risque</h3>
        <p style="font-size: 0.9rem; opacity: 0.7; max-width: 400px; margin: 0 auto;">Testez la formation pendant 14 jours. Si vous n'êtes pas convaincu que ces compétences vont transformer votre façon de travailler, je vous rembourse intégralement.</p>
    </div>
</div>
            """,
            unsafe_allow_html=True
        )

page = st.navigation([
    st.Page(cheat_sheet, title="Cheat Sheet", default=True),
    st.Page(formation, title="Devenez un pro"),
], position="top")

page.run()