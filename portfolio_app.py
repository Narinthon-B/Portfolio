import streamlit as st
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Portfolio", layout="wide", initial_sidebar_state="collapsed")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@600;700&family=Outfit:wght@400;700&display=swap');

    /* Force Light Theme */
    .stApp {
        background-color: #E6E6FA; 
        color: #000000;
        font-family: 'Outfit', sans-serif;
    }

    header, footer {visibility: hidden;}

    /* Centered Layout */
    .main .block-container {
        max-width: 1100px;
        padding-top: 2rem;
    }

    /* TITLE STYLE (No Box, Thick Border, Shadow) */
    .header-title {
        font-family: 'Fredoka', cursive;
        font-size: 100px !important;
        text-align: center;
        margin: 0 0 40px 0;
        color: white;
        -webkit-text-stroke: 3px black; /* ตัวหนังสือขอบหนา */
        text-shadow: 6px 6px 0px #A29BFE; /* เงาสไตล์ Scrapbook */
        text-transform: uppercase;
    }

    /* CARD STYLE (Uniform Spacing) */
    .scrapbook-card {
        background-color: #F8F9FA;
        border: 2px solid #000000;
        border-radius: 25px;
        padding: 25px;
        box-shadow: 6px 6px 0px 0px rgba(162, 155, 254, 0.8);
        margin-bottom: 25px; /* จัดระยะห่างให้เท่ากันทุกกรอบ */
    }

    /* PROFILE CARD - Aligned with Right Column */
    .profile-card {
        background: #F8F9FA;
        border: 2px solid black;
        border-radius: 25px;
        padding: 12px;
        box-shadow: 8px 8px 0px 0px #A29BFE;
        margin-bottom: 25px;
    }

    .profile-img-placeholder {
        background: #DCDDE1;
        border: 2px dashed black;
        border-radius: 20px;
        height: 380px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        color: #636e72;
        text-align: center;
    }

    .section-title {
        font-family: 'Fredoka', cursive;
        text-transform: uppercase;
        font-size: 1.5rem;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .tag {
        display: inline-block;
        background: #A29BFE;
        color: white;
        border: 1px solid black;
        border-radius: 50px;
        padding: 4px 12px;
        font-size: 0.75rem;
        font-weight: bold;
        margin-right: 5px;
        margin-bottom: 5px;
    }

    .project-img {
        background: #f1f2f6;
        border: 1px solid black;
        border-radius: 15px;
        height: 180px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #95a5a6;
    }

    /* GITHUB BUTTON CUSTOM STYLE */
    div.stLinkButton > a {
        background-color: #000000 !important;
        color: white !important;
        border: 2px solid #000000 !important;
        border-radius: 15px !important;
        padding: 0.6rem 1.2rem !important;
        font-weight: 700 !important;
        text-decoration: none !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        box-shadow: 4px 4px 0px #A29BFE !important;
    }
    
    div.stLinkButton > a:hover {
        transform: translate(-2px, -2px) !important;
        box-shadow: 7px 7px 0px #A29BFE !important;
        background-color: #1a1a1a !important;
    }

    div.stLinkButton > a:active {
        transform: translate(2px, 2px) !important;
        box-shadow: 0px 0px 0px #A29BFE !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER TITLE ---
st.markdown('<h1 class="header-title">PORTFOLIO</h1>', unsafe_allow_html=True)

# --- MAIN COLUMNS ---
col_left, col_right = st.columns([1, 1.8], gap="large")

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = get_base64_image("RapidMiner_MuchroomProj.jpg")
img_finance = get_base64_image("Finance.jpg")
img_phofile = get_base64_image("IMG_7598 (1).JPG")

with col_left:
    # 1. PROFILE IMAGE CARD
    st.markdown(f"""
        <div class="profile-card">
            <div style="display: flex; justify-content: center; align-items: center;">
                <img src="data:image/jpeg;base64,{img_phofile}" 
                     style="width:100%; height:50%; border-radius:20px; border:2px solid black;">
            </div>
            <div style="padding: 15px; text-align: center;">
                <h2 style="margin:0; font-family:'Fredoka'; letter-spacing: 1px;">NARINTHON TANWIBOON</h2>
                <p style="opacity:0.8; font-weight: 500;">Aspiring Data Engineer 🚀</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 2. EDUCATION
    st.markdown("""
        <div class="scrapbook-card">
            <div class="section-title">EDUCATION</div>
            <p style="font-size: 0.95rem;">
                <b>Computer and Robotics Engineering</b><br>
                <i>Bangkok University | 2023 - Present</i>
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 3. SKILLS
    st.markdown("""
        <div class="scrapbook-card">
            <div class="section-title">SKILLS</div>
            <div style="line-height: 2;">
                <span class="tag">Python</span><span class="tag">Pandas</span><span class="tag">SQL</span>
                <span class="tag">RapidMiner</span><span class="tag">Data Analytics</span><span class="tag">ELT</span>
                <span class="tag">Data Modeling</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- 4. CONTACT SECTION (Insert after Skills) ---
    st.markdown("""
        <style>
        .contact-container {
            display: flex;
            flex-direction: column;
            gap: 15px;
            margin-top: 10px;
        }
        
        /* Specific Lavender Pill Styling */
        .contact-pill {
            background-color: #F0E6FF !important; /* Soft Lavender */
            border: 2px solid #000000 !important;
            border-radius: 50px !important;
            padding: 12px 20px !important;
            color: black !important;
            font-family: 'Fredoka', cursive;
            font-weight: 700;
            text-align: center;
            text-decoration: none !important;
            display: block;
            box-shadow: 4px 4px 0px #000000;
            transition: all 0.2s ease-in-out;
            font-size: 0.9rem;
            letter-spacing: 1px;
        }

        .contact-pill:hover {
            transform: translateY(-3px) rotate(-1deg);
            background-color: #E6E6FA !important; /* Slightly darker lavender */
            box-shadow: 6px 6px 0px #A29BFE;
            color: #000000;
        }
        </style>

        <div class="scrapbook-card">
            <div class="section-title">CONTACT</div>
            <div class="contact-container">
                <a href="https://github.com/Narinthon-B" target="_blank" class="contact-pill">🔗 GITHUB</a>
                <a href="https://www.linkedin.com/in/narinthon-tanwiboon-ab1b25366/" target="_blank" class="contact-pill">💼 LINKEDIN</a>
                <a class="contact-pill">narinthon.tanwi@gmail.com</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_right:
    # 4. ABOUT ME
    st.markdown("""
        <div class="scrapbook-card">
            <div class="section-title">ABOUT ME</div>
            <p>I am a Computer Engineering and Robotics student interested in Data Engineering and data systems. I enjoy working with data from raw input to structured output, including cleaning, transforming, and organizing data for practical use.  I’m currently building my skills in SQL and data processing while working on projects that reflect real-world data workflows. My goal is to continue learning and gradually develop strong foundations in designing reliable and maintainable data systems.</p>
        </div>
    """, unsafe_allow_html=True)

    # 5. PROJECTS
    st.markdown('<div class="section-title" style="margin-left:10px;">FEATURED PROJECTS</div>', unsafe_allow_html=True)

    # Project 1: Financial Sentiment
    with st.container():
        st.markdown(f"""
            <div class="scrapbook-card">
                <div class="project-img"><img src="data:image/jpeg;base64,{img_finance}" style="width:100%; height:100%; object-fit:cover; border-radius:15px;"></div>
                <h3 style="margin-bottom:10px;">Finance market</h3>
                <p style="font-size: 0.9rem; margin-bottom:15px;">Built an end-to-end data pipeline to analyze the correlation between financial news sentiment and asset price movements, aiming to evaluate whether sentiment can serve as a leading indicator for market trends.

Automated data ingestion using yfinance and news scraping/APIs

Applied VADER Sentiment Analysis (NLTK) to quantify news headlines

Performed time-series alignment and data transformation with Pandas

Conducted correlation analysis and visualized insights using Matplotlib</p>
                <div style="margin-bottom: 20px;">
                    <span class="tag">Python</span><span class="tag">Pandas</span><span class="tag">ELT</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        # GitHub Button with Material Icon (GitHub-like icon)
        st.link_button("View on GitHub", "https://github.com/Narinthon-B/Finance-market", icon=":material/terminal:")

    st.markdown("<br>", unsafe_allow_html=True)

    # Project 2: Parquet Optimization
    with st.container():
        st.markdown(f"""
            <div class="scrapbook-card">
                <div class="project-img">
            <img src="data:image/jpeg;base64,{img_base64}" style="width:100%; height:100%; object-fit:cover; border-radius:15px;">
        </div>
                <h3 style="margin-bottom:10px;">Classification Toxicity Analysis</h3>
                <p style="font-size: 0.9rem; margin-bottom:15px;">This project focuses on applying Data Analytics techniques to classify mushrooms as either toxic or non-toxic using a Decision Tree classification model. The objective was to predict toxicity based on various physical characteristics of mushrooms.

The workflow included data preprocessing, data cleaning, feature analysis, model training, and performance evaluation using RapidMiner. The Decision Tree model was implemented to identify key attributes that influence toxicity classification and to generate interpretable prediction rules.

Through this project, I gained hands-on experience in classification modeling, data preprocessing, model evaluation, and translating analytical results into meaningful insights.</p>
                <div style="margin-bottom: 20px;">
                    <span class="tag">RapidMiner</span><span class="tag">Data Analytics</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("View on GitHub", "https://github.com/Narinthon-B/Mushroom-Classification-Toxicity-Analysis", icon=":material/terminal:")

# --- FOOTER ---
st.markdown("""

""", unsafe_allow_html=True)