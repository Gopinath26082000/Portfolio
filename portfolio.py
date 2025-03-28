import streamlit as st
import matplotlib.pyplot as plt

# Set page title and layout
st.set_page_config(page_title="Gopinath Barani | Portfolio", page_icon="📂", layout="wide")

def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://img.freepik.com/free-vector/hexagonal-black-background-modern-design_1017-37442.jpg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function at the beginning of the script
add_bg_from_url()

# Sidebar with Profile Info
st.sidebar.image("D:\Professional pic.jpg", width=200)  # Add your picture here
st.sidebar.title("Gopinath Barani")
st.sidebar.write("Python | Linux | AI | Devops | AWS")
st.sidebar.markdown("[📧 Email Me](mailto:gopinath26082000@gmail.com)")
st.sidebar.markdown("[💼 LinkedIn](https://linkedin.com/in/gopinath-barani-bb7615255)")
st.sidebar.markdown("[🐍 GitHub](https://github.com/Gopinath26082000)")
st.sidebar.markdown("[🚀 Stat Brio - My Freelancing Page]( https://www.instagram.com/statbrio/profilecard/?igsh=aHFzNXV4MzNod3Fz)")

# Home Section
st.title("👨‍💻 Welcome to My Portfolio!")
st.write("MBA graduate with a strong foundation in Finance and Marketing, coupled with expertise in Data Analysis, Linux, AWS, DevOps, and Python. Skilled in leveraging data visualization and analytical techniques to drive strategic decision-making and optimize business performance. Passionate about integrating cloud technologies, automation, and machine learning to enhance operational efficiency. Eager to contribute as a Data Analyst by transforming complex data into actionable insights that fuel growth and innovation.")

# Dashboard Section
st.header("📊 Dashboard Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Experience", "3 Months", "Internship at Shiash Infotech")

with col2:
    st.metric("Projects", "7+", "Data Analytics and Cloud computing")

with col3:
    st.metric("Certifications", "4", "Linux, AWS, DevOps, Python")


# Tools & Technologies Section
st.header("🛠 Tools & Technologies")
st.write("💻 **Programming:** Python, Bash")  
st.write("☁️ **Cloud:** AWS")  
st.write("🛡 **Linux:** Apache, Nmap, OpenVAS")  
st.write("📊 **Data Analytics:** Power BI, Tableau, Pandas, NumPy")  
st.write("📌 **Devops:** Git, Docker, Kubernetes")

# Projects Section
st.header("🚀 My Projects")

projects = [
    {"title": "AI Chatbot", "desc": "A chatbot built using a Bash script that translates basic Linux command-line instructions into normal language.", "link": "https://github.com/Gopinath26082000/Chatbot-Linux/tree/main"},
    {"title": "Quality of wine using ML Model", "desc": "Predicting the best quality of the wine .", "link": "https://github.com/Gopinath26082000/Quality-of-wine"},
    {"title": "Advanced Multi-Target Vulnerability Scanner Project ", "desc": "Security tool integrating Nmap, openvas, Nikto for vulnerability detection.", "link": "https://github.com/Gopinath26082000/Multi-target-vulnerability-scanner/blob/main/README.md"},
    {"title": "Dashboard Creation", "desc": "sales data of the year Using power BI.", "link": "https://github.com/yourproject"}
]

for project in projects:
    st.subheader(f"🔹 {project['title']}")
    st.write(project["desc"])
    st.markdown(f"[🔗 GitHub Repo]({project['link']})")

# Certifications
st.header("🎓 Certifications")
st.write("- Linux Certification")
st.write("- AWS Certification")
st.write("- Power BI & Tableau")
st.write("- SPSS, Python ")

# Contact Section
st.header("📩 Contact Me")
st.write("Feel free to reach out for collaborations or freelance projects!")
st.markdown("[📧 Email](mailto:gopinath26082000@gmail.com) | [💼 LinkedIn](https://linkedin.com/in/gopinath-barani-bb7615255)")
