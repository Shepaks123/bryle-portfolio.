import streamlit as st
import pandas as pd
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------
# PERSONALIZE THESE DETAILS BEFORE SUBMITTING
# ---------------------------------------------------------
NAME = "Bryle Anthony G. Dinapo"
PROGRAM = "Bachelor of Science in Information Technology"
YEAR_LEVEL = "4th Year"
SCHOOL = "Cebu Institute of Technology – University"
SECTION = "EDIT THIS: Enter your CSIT 349 section"
EMAIL = "EDIT THIS: Add your email address"
LOCATION = "Cebu City, Philippines"

st.set_page_config(
    page_title=f"{NAME} | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
    .stApp { background: #0b1020; color: #edf2ff; }
    [data-testid="stSidebar"] { background: #111a30; border-right: 1px solid #263452; }
    h1, h2, h3 { font-family: 'Space Grotesk', sans-serif !important; color: #f4f7ff; }
    .hero {
        padding: 2.2rem 2.4rem; border-radius: 24px;
        background: linear-gradient(120deg, #172b50 0%, #243e68 55%, #315b78 100%);
        border: 1px solid #3a5479; margin-bottom: 1.3rem;
    }
    .eyebrow { color: #9fd8e9; text-transform: uppercase; letter-spacing: 2px;
               font-size: .75rem; font-weight: 700; }
    .hero h1 { font-size: 2.8rem; margin: .35rem 0; }
    .hero p { color: #d5e4f7; font-size: 1.05rem; max-width: 780px; }
    .pill {
        display: inline-block; padding: .35rem .75rem; margin: .2rem .25rem .2rem 0;
        border-radius: 30px; background: #203a5e; color: #c7e9f2;
        border: 1px solid #3d6285; font-size: .82rem;
    }
    .panel {
        background: #121d33; border: 1px solid #293a59; border-radius: 18px;
        padding: 1.15rem 1.25rem; height: 100%;
    }
    .muted { color: #aab8d0; }
    .project-tag { color: #9fd8e9; font-size: .8rem; font-weight: 700; }
    div[data-testid="stMetric"] {
        background: #121d33; border: 1px solid #293a59;
        padding: 14px 16px; border-radius: 16px;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        background: #121d33; border-radius: 10px 10px 0 0; padding: 10px 18px;
    }
    .footer { color: #8292ad; text-align: center; padding: 2rem 0 1rem; font-size: .85rem; }
    a { color: #8bd7eb !important; }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation and profile
with st.sidebar:
    st.markdown("## 💻 BRYLE'S PORTFOLIO")
    st.caption("PERSONAL WEBSITE")
    page = st.radio(
        "Navigate",
        ["Overview", "Autobiography", "Skills", "Projects", "Contact"],
        index=0,
    )
    st.divider()
    st.markdown("### Quick profile")
    st.markdown(f"**{NAME}**")
    st.caption(f"{YEAR_LEVEL} · BSIT")
    st.caption(SCHOOL)
    st.caption(f"📍 {LOCATION}")
    st.divider()
    st.caption("CSIT 349 · Applied AI")
    st.caption(SECTION)

# Header
st.markdown(f"""
<div class="hero">
  <div class="eyebrow">Student • Aspiring Web Developer • Creative Learner</div>
  <h1>Hi, I'm {NAME.split()[0]} 👋</h1>
  <p>I'm a {YEAR_LEVEL.lower()} Information Technology student who enjoys building things with technology,
  learning new skills, and exploring creative ideas. I'm working toward a future in web development
  and graphic design.</p>
  <span class="pill">Web Development</span>
  <span class="pill">Graphic Design</span>
  <span class="pill">Gaming</span>
  <span class="pill">Hiking</span>
</div>
""", unsafe_allow_html=True)

# Profile photo: place "Dinapo, Bryle Anthony.jpg" beside app.py
# OR place it inside an "images" folder.
if page == "Overview":
    left, right = st.columns([1, 2], gap="large")
    with left:
        photo_options = [
            Path("Dinapo, Bryle Anthony.jpg"),
            Path("images") / "Dinapo, Bryle Anthony.jpg",
        ]
        profile_photo = next((photo for photo in photo_options if photo.is_file()), None)

        if profile_photo:
            st.image(
                str(profile_photo),
                caption="Bryle Anthony G. Dinapo",
                use_container_width=True,
            )
        else:
            st.warning(
                'Profile photo not found. Add "Dinapo, Bryle Anthony.jpg" '
                'beside app.py or inside the images folder.'
            )
            st.markdown("<div style='font-size:5rem; text-align:center;'>🧑‍💻</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="panel" style="text-align:center;">
          <h3 style="margin-bottom:0;">Bryle Dinapo</h3>
          <p class="muted">4th Year BSIT Student</p>
          <hr style="border-color:#293a59;">
          <p><b>Program</b><br><span class="muted">BS Information Technology</span></p>
          <p><b>School</b><br><span class="muted">Cebu Institute of Technology – University</span></p>
          <p><b>Year</b><br><span class="muted">4th Year</span></p>
        </div>
        """, unsafe_allow_html=True)
    with right:
        st.subheader("A little about me")
        st.write(
            "I'm Bryle, an IT student from Cebu. I enjoy learning how technology works "
            "and using what I learn in school to create useful digital projects. I am especially "
            "interested in web development and graphic design because they combine problem-solving "
            "with creativity."
        )
        st.write(
            "Outside academics, I enjoy playing games and going hiking. I like exploring new "
            "things, improving my skills, and challenging myself to learn something different."
        )
        st.info("My goal is to keep improving as a developer, gain real-world experience, and build projects that solve practical problems.")
    st.subheader("At a glance")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Study level", "4th Year")
    m2.metric("Program", "BSIT")
    m3.metric("Main interest", "Web Dev")
    m4.metric("Creative interest", "Design")
    st.subheader("What I enjoy")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="panel"><h3>🎮 Gaming</h3><p class="muted">I enjoy games for entertainment, teamwork, and the challenge of learning game mechanics.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="panel"><h3>🥾 Hiking</h3><p class="muted">I like getting outdoors, exploring places, and taking a break from the screen.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="panel"><h3>🎨 Creativity</h3><p class="muted">I enjoy exploring visual design and finding ways to make digital experiences look better.</p></div>', unsafe_allow_html=True)

elif page == "Autobiography":
    st.header("My Autobiography")
    st.write("A short story about my background, education, interests, and learning journey.")
    with st.expander("My background", expanded=True):
        st.write(
            "My name is Bryle Anthony G. Dinapo, and I am from Cebu City, Philippines. "
            "I am currently pursuing a Bachelor of Science in Information Technology. "
            "I chose this field because I am interested in computers, software, and the ways "
            "technology can help people in their everyday lives."
        )
    with st.expander("Education"):
        st.write(f"I am a {YEAR_LEVEL} BSIT student at {SCHOOL}. Throughout my studies, I have been exposed to programming, web technologies, troubleshooting, and software development concepts.")
        st.write("My coursework has helped me practice logical thinking, debugging, teamwork, and solving technical problems.")
    with st.expander("Interests and goals"):
        st.write("I enjoy playing games and hiking. In technology, I am interested in web development and graphic design. My goal is to continue improving my technical and creative skills and eventually work on projects that are useful to real users.")
    st.subheader("Learning milestones")
    milestones = [
        ("Started learning programming", "Built foundations in programming and problem-solving."),
        ("Explored web technologies", "Practiced HTML, CSS, and JavaScript."),
        ("Worked on academic projects", "Collaborated on projects that apply IT concepts to practical problems."),
        ("Focused on my future direction", "Set goals to pursue web development or graphic design.")
    ]
    for i, (heading, detail) in enumerate(milestones, 1):
        st.markdown(f"**{i}. {heading}**")
        st.caption(detail)

elif page == "Skills":
    st.header("Skills & Tools")
    st.write("These are my current self-assessed skill levels. They represent my learning progress, not professional certifications.")
    skills = pd.DataFrame({
        "Skill": ["HTML", "CSS", "JavaScript", "Java", "Python", "C", "DaVinci Resolve"],
        "Level (%)": [70, 65, 55, 50, 50, 55, 70],
        "Category": ["Web", "Web", "Web", "Programming", "Programming", "Programming", "Creative"]
    })
    st.dataframe(
        skills,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Level (%)": st.column_config.ProgressColumn("Self-assessed level", min_value=0, max_value=100, format="%d%%")
        }
    )
    st.subheader("Skill overview")
    chart_data = skills.set_index("Skill")[["Level (%)"]]
    st.bar_chart(chart_data, use_container_width=True, horizontal=True)
    st.subheader("Tools and strengths")
    a, b = st.columns(2)
    with a:
        st.markdown('<div class="panel"><h3>🧰 Technical skills</h3><p class="muted">HTML · CSS · JavaScript · Java · Python · C</p><p class="muted">Basic web development, debugging, troubleshooting, and problem-solving.</p></div>', unsafe_allow_html=True)
    with b:
        st.markdown('<div class="panel"><h3>✨ Other strengths</h3><p class="muted">Creative editing with DaVinci Resolve, willingness to learn, attention to detail, and teamwork.</p></div>', unsafe_allow_html=True)
    st.caption("Tip: Update the percentages to match your actual confidence and experience before submitting.")

elif page == "Projects":
    st.header("My Projects")
    st.write("A selection of academic and learning projects. Add screenshots or live links when available.")
    tab1, tab2, tab3 = st.tabs(["CATalyst", "Community Safety System", "Python Coursework"])
    with tab1:
        st.markdown("### CATalyst – Research Assistance Platform")
        st.markdown('<span class="project-tag">CAPSTONE / WEB APPLICATION</span>', unsafe_allow_html=True)
        st.write("**My role:** Student developer working on the frontend and user-facing features.")
        st.write("**Tools:** React, JavaScript, HTML, CSS, and Supabase (project environment).")
        st.write("**Description / outcome:** A research-support platform concept designed to help users work with research documents, assess related literature, identify research gaps, and develop SMART research objectives.")
        st.info("Add your team's repository or deployed application link here if your instructor allows it.")
    with tab2:
        st.markdown("### Web-Based Community Safety and Incident Reporting System")
        st.markdown('<span class="project-tag">ACADEMIC GROUP PROJECT</span>', unsafe_allow_html=True)
        st.write("**My role:** Student project team member. Update this line to describe your exact assigned responsibilities.")
        st.write("**Tools:** Web technologies and the tools selected by your group (edit to list the exact stack).")
        st.write("**Description / outcome:** A proposed web-based system focused on community safety and incident reporting. The project applies software development concepts to a practical community need.")
        st.warning("Personalize your role, technology stack, and actual project outcome before submitting.")
    with tab3:
        st.markdown("### Python Programming Coursework")
        st.markdown('<span class="project-tag">PROGRAMMING / COURSEWORK</span>', unsafe_allow_html=True)
        st.write("**My role:** Student programmer completing Python laboratory exercises.")
        st.write("**Tools:** Python.")
        st.write("**Description / outcome:** Practiced programming fundamentals, writing and testing code, and improving logical problem-solving through hands-on exercises.")
        st.warning("Replace this with a more substantial third project if you have one, and add a GitHub link or screenshot if available.")
    st.subheader("Project reflection")
    st.write("These projects help me connect classroom lessons with practical development work. I want to keep improving my ability to plan, build, test, and present useful applications.")

elif page == "Contact":
    st.header("Contact & Feedback")
    st.write("Have a question, suggestion, or opportunity? Send a message using the form below.")
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your name")
        email = st.text_input("Your email")
        reason = st.selectbox("What is this about?", ["General message", "Project feedback", "Collaboration", "Opportunity"])
        rating = st.slider("How would you rate this portfolio?", 1, 5, 5)
        message = st.text_area("Your message", placeholder="Write your message here...")
        permission = st.checkbox("I agree that this message can be used for this class activity.")
        submitted = st.form_submit_button("Submit message", type="primary")
    if submitted:
        if not name.strip() or not email.strip() or not message.strip():
            st.error("Please complete your name, email, and message before submitting.")
        elif "@" not in email:
            st.error("Please enter a valid email address.")
        elif not permission:
            st.warning("Please check the consent box before submitting.")
        else:
            st.success(f"Thank you, {name}! Your feedback has been received in this demo.")
            st.write(f"**Topic:** {reason} · **Portfolio rating:** {rating}/5")
            st.caption("Demo form: this app displays a confirmation but does not send or store messages online.")
    st.divider()
    st.subheader("My contact details")
    st.write(f"📧 **Email:** {EMAIL}")
    st.write(f"📍 **Location:** {LOCATION}")
    st.caption("Replace the email placeholder with an address you are comfortable sharing.")

# Downloadable short profile
profile_text = f"""PORTFOLIO PROFILE
Name: {NAME}
Program: {PROGRAM}
Year: {YEAR_LEVEL}
School: {SCHOOL}
Section: {SECTION}

ABOUT
I am an Information Technology student interested in web development and graphic design.
I enjoy gaming, hiking, and learning new technology skills.

SKILLS
HTML, CSS, JavaScript, Java, Python, C, DaVinci Resolve.

PROJECTS
1. CATalyst – Research Assistance Platform
2. Web-Based Community Safety and Incident Reporting System
3. Python Programming Coursework

Note: Please personalize the section, contact details, project roles, and outcomes before submission.
"""
st.sidebar.download_button(
    "⬇ Download profile text",
    data=profile_text,
    file_name="Bryle_Dinapo_Portfolio_Profile.txt",
    mime="text/plain",
    use_container_width=True,
)

st.markdown('<div class="footer">Built with Streamlit · CSIT 349 Applied AI · Bryle Dinapo</div>', unsafe_allow_html=True)
