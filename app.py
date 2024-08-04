from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Aliyan Sayani | Portfolio"
PAGE_ICON = ":wave:"
NAME = "Aliyan Sayani"
DESCRIPTION = """
As a Computer Science student with a deep interest in Artificial Intelligence and Data Science, I am a curious and analytical individual who is constantly fascinated by the possibilities of technology. I have always been passionate about programming and have honed my skills in Java, SQL, python, and C++ through various semester projects of Management Systems, Data Science, Data Mining and Machine Learning, always pushing myself to excel in my field of study."""
EMAIL = "alisayani03@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/aliyan-sayani-91a1471b9/",
    "GitHub": "https://github.com/aliyan08",
}
PROJECTS = {
    "🏆 Performence Based Cricket-IX selector - Data Mining Approach": "https://github.com/aliyan08/Perfomence-Based-Cricket-11-Selector-Using-Assoiciastion-Rule-Mining",
    "🏆 Property Price Pridiction systems - Advance Regression Technique": "https://github.com/aliyan08/house-prices-advanced-regression-techniques",
    "🏆 Leaf Classification - Image Processing": "https://github.com/aliyan08/leaf-classification"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, ANN, CNN, decition trees, Rule Mining
- 🗄️ Databases: SAP, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Engineer Intern | Habib Bank AG Zurich**")
st.write("07/2024 - Present")


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")