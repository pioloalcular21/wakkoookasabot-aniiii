import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="SSGMIS Data Visualization",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- CUSTOM PAGE STYLE ----
st.markdown("""
<style>
/* Global Background and Font */
body, .stApp {
    background-color: #f9fafc;
    font-family: 'Segoe UI', sans-serif;
    color: #1f2937;
}

/* Title Styles */
.title {
    font-size: 2.2rem;
    font-weight: bold;
    color: #1e40af;
    text-align: center;
    margin-bottom: 0.2rem;
}
.subtitle {
    text-align: center;
    color: #475569;
    font-size: 1.1rem;
    margin-bottom: 1.5rem;
}

/* Card container */
.block-container {
    padding-top: 1rem;
}
.card {
    background-color: #f1f5f9;
    padding: 1rem 1.5rem;
    border-radius: 10px;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
    margin-bottom: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

# ---- PAGE HEADER ----
st.markdown('<div class="title">📊 SSGMIS TAM & UAT Visualization Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Technology Transfer and Implementation of the Supreme Student Government Management Information System</div>', unsafe_allow_html=True)
st.divider()

# ---- SIDEBAR ----
st.sidebar.header("📂 Dashboard Navigation")
section = st.sidebar.radio(
    "Select Section:",
    ("🏫 TAM Charts", "🧪 UAT Charts", "📘 About")
)

# =============================
# 🏫 TECHNOLOGY ACCEPTANCE MODEL (TAM)
# =============================
if section == "🏫 TAM Charts":
    st.header("🏫 Technology Acceptance Model (TAM)")

    tam_charts = st.selectbox(
        "Select a TAM Construct:",
        ["Perceived Usefulness (PU)", "Perceived Ease of Use (PEOU)",
         "Attitude Toward Using (ATU)", "Behavioral Intention (BI)"]
    )

    # --- Data ---
    tam_data = {
        "Perceived Usefulness (PU)": [0, 0, 80, 120, 180],
        "Perceived Ease of Use (PEOU)": [0, 0, 90, 165, 125],
        "Attitude Toward Using (ATU)": [0, 0, 75, 130, 175],
        "Behavioral Intention (BI)": [0, 0, 90, 165, 135]
    }
    colors_dict = {
        "Perceived Usefulness (PU)": "royalblue",
        "Perceived Ease of Use (PEOU)": "mediumseagreen",
        "Attitude Toward Using (ATU)": "gold",
        "Behavioral Intention (BI)": "lightskyblue"
    }

    # --- Variables ---
    data = tam_data[tam_charts]
    color = colors_dict[tam_charts]
    labels = ["1-Strongly Disagree", "2-Disagree", "3-Neutral", "4-Agree", "5-Strongly Agree"]

    # --- Bar Chart ---
    with st.container():
        st.markdown(f"### 📊 {tam_charts} - Bar Chart")
        fig_bar, ax_bar = plt.subplots(figsize=(7, 5))
        ax_bar.bar(labels, data, color=color, edgecolor="black")
        ax_bar.set_ylabel("Number of Respondents")
        plt.xticks(rotation=20)
        st.pyplot(fig_bar)

    # --- Pie Chart ---
    with st.container():
        st.markdown(f"### 🥧 {tam_charts} - Pie Chart")
        pie_labels = ["5-Strongly Agree", "4-Agree", "3-Neutral", "2-Disagree", "1-Strongly Disagree"]
        pie_values = [data[4], data[3], data[2], data[1], data[0]]
        pie_colors = ["royalblue", "gold", "mediumseagreen", "lightskyblue", "orange"]

        fig_pie, ax_pie = plt.subplots(figsize=(6, 5))
        ax_pie.pie(pie_values, labels=pie_labels, autopct="%1.1f%%", startangle=90, colors=pie_colors)
        ax_pie.set_title(f"{tam_charts} - Pie Chart")
        st.pyplot(fig_pie)

# =============================
# 🧪 USER ACCEPTANCE TESTING (UAT)
# =============================
elif section == "🧪 UAT Charts":
    st.header("🧪 User Acceptance Testing (UAT)")

    uat_charts = st.selectbox(
        "Select a UAT Chart:",
        ["Functionality (Pie Chart)", "Usability (Bar Chart)",
         "Performance (Line Chart)", "Satisfaction & Acceptance (Stacked Bar Chart)"]
    )

    if uat_charts == "Functionality (Pie Chart)":
        pie_labels = ["5-Strongly Agree", "4-Agree", "3-Neutral", "2-Disagree", "1-Strongly Disagree"]
        pie_sizes = [130, 175, 75, 0, 0]
        colors = ["royalblue", "gold", "mediumseagreen", "lightskyblue", "orange"]

        st.markdown("### 🥧 Functionality - Pie Chart")
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.pie(pie_sizes, labels=pie_labels, autopct="%1.1f%%", startangle=90, colors=colors)
        st.pyplot(fig)

    elif uat_charts == "Usability (Bar Chart)":
        labels = ["1-Strongly Disagree", "2-Disagree", "3-Neutral", "4-Agree", "5-Strongly Agree"]
        values = [0, 0, 80, 115, 185]
        st.markdown("### 📊 Usability - Bar Chart")
        fig, ax = plt.subplots(figsize=(7, 5))
        ax.bar(labels, values, color="lightcoral", edgecolor="black")
        ax.set_ylabel("Number of Respondents")
        plt.xticks(rotation=20)
        st.pyplot(fig)

    elif uat_charts == "Performance (Line Chart)":
        labels = ["1-Strongly Disagree", "2-Disagree", "3-Neutral", "4-Agree", "5-Strongly Agree"]
        values = [0, 0, 75, 180, 125]
        st.markdown("### 📈 Performance - Line Chart")
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(labels, values, marker="o", color="darkorange", linewidth=2)
        ax.set_ylabel("Number of Respondents")
        plt.xticks(rotation=20)
        st.pyplot(fig)

    elif uat_charts == "Satisfaction & Acceptance (Stacked Bar Chart)":
        uat_data = {
            "Category": ["Functionality", "Usability", "Performance", "Satisfaction & Acceptance"],
            "3-Neutral": [75, 80, 75, 70],
            "4-Agree": [175, 115, 180, 145],
            "5-Strongly Agree": [130, 185, 125, 165]
        }
        df = pd.DataFrame(uat_data)
        st.markdown("### 🧱 Satisfaction & Acceptance - Stacked Bar Chart")

        fig, ax = plt.subplots(figsize=(9, 6))
        bottom = [0] * len(df["Category"])
        colors = ["moccasin", "lightskyblue", "royalblue"]

        for i, scale in enumerate(["3-Neutral", "4-Agree", "5-Strongly Agree"]):
            ax.bar(df["Category"], df[scale], bottom=bottom, label=scale, color=colors[i])
            bottom = [a + b for a, b in zip(bottom, df[scale])]

        ax.set_ylabel("Number of Respondents")
        ax.legend(title="Scale", bbox_to_anchor=(1.05, 1), loc="upper left")
        st.pyplot(fig)

# =============================
# 📘 ABOUT
# =============================
elif section == "📘 About":
    st.header("📘 About this Dashboard")
    st.markdown("""
    **Developer:** Piolo Alcular  
    **Project Title:** *Technology Transfer and Implementation of the SSG Management Information System (SSGMIS)*  
    **Institution:** Agusan del Sur State College of Agriculture and Technology (ASSCAT)*  

    This dashboard visualizes results from:  
    - **Technology Acceptance Model (TAM)** 
    - **User Acceptance Testing (UAT)** 

    💡 *Use the sidebar to navigate and explore each dataset interactively.*
    """)

