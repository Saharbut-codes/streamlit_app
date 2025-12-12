import streamlit as st
import time

st.set_page_config(page_title="Real-Time Picture Animation", page_icon="🎥", layout="wide")

# ---------------------------------- GLOW CINEMATIC SPLASH ----------------------------------
glow_css = """
<style>

#splash-container {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: #3a1e1e;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    z-index: 9999;
    animation: fadeOut 2s ease-in-out 3.2s forwards;
}

.glow-circle {
    position: absolute;
    width: 260px;
    height: 260px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(255,255,255,0.35), rgba(0,0,0,0));
    filter: blur(35px);
    animation: glowPulse 3s ease-in-out infinite;
}

@keyframes glowPulse {
    0% { transform: scale(0.9); opacity: 0.55; }
    50% { transform: scale(1.15); opacity: 0.85; }
    100% { transform: scale(0.9); opacity: 0.55; }
}

.splash-logo {
    width: 150px;
    z-index: 10;
    opacity: 0;
    animation: logoFade 2s ease-in-out forwards;
}

@keyframes logoFade {
    0% { opacity: 0; transform: scale(1.3); }
    60% { opacity: 1; transform: scale(1); }
    100% { opacity: 1; }
}

.splash-title {
    margin-top: 20px;
    font-size: 40px;
    font-weight: 600;
    color: white;
    opacity: 0;
    z-index: 10;
    animation: titleFade 2s ease-in-out 0.8s forwards;
}

@keyframes titleFade {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}

@keyframes fadeOut {
    to { opacity: 0; visibility: hidden; }
}

</style>
"""

glow_html = """
<div id="splash-container">
    <div class="glow-circle"></div>
    <img class="splash-logo" src="https://cdn-icons-png.flaticon.com/512/5124/5124620.png">
    <div class="splash-title">Real-Time Picture Animation</div>
</div>
"""

st.markdown(glow_css, unsafe_allow_html=True)
st.markdown(glow_html, unsafe_allow_html=True)

time.sleep(3.3)

# ----------------------------------------------------------------------
# ------------------------ GLOBAL UI STYLING ------------------------

st.markdown("""
<style>

.header-container {
    text-align: center;
    width: 100%;
    margin-top: -80px;
}

.main-title {
    font-size: 48px;
    font-weight: 700;
    color: #f1f1f1;
    margin-bottom: -5px;
}

.sub-title {
    font-size: 20px;
    color: #d0d0d0;
    margin-bottom: 25px;
}

.desc-box {
    background: transparent;
    padding: 20px 0;
    width: 140%;
}

.desc-title {
    font-size: 32px;
    font-weight: 700;
    color: white;
    margin-bottom: 10px;
}

.desc-text {
    font-size: 18px;
    color: #e6e6e6;
    line-height: 1.6;
    max-width: 750px;
    text-align: left;
}

/* ------------ AESTHETIC VIBRANT UPLOAD CARDS ------------- */

.upload-card {
    background: linear-gradient(145deg, #1f1f26, #14141a);
    border-radius: 22px;
    padding: 28px;
    box-shadow: 0px 6px 16px rgba(0,0,0,0.35);
    border: 1px solid rgba(255,255,255,0.06);
    transition: 0.25s ease;
}

.upload-card:hover {
    transform: translateY(-4px);
    box-shadow: 0px 10px 26px rgba(0,0,0,0.45);
}

/* ------------ Section Title ------------- */

.section-title {
    font-size: 22px !important;
    font-weight: 700;
    margin-bottom: 10px;
    background: linear-gradient(90deg, #ff7ae4, #7aa3ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* ------------ Vibrant Buttons ------------- */

.stButton>button, .stCameraInput > div > div > button {
    background: linear-gradient(135deg, #ff7ae4, #7aa3ff);
    color: white;
    border: none;
    padding: 14px 26px;
    border-radius: 18px;
    font-size: 16px;
    font-weight: 600;
    transition: 0.2s ease;
}

.stButton>button:hover, .stCameraInput > div > div > button:hover {
    transform: scale(1.06);
    box-shadow: 0px 6px 16px rgba(0,0,0,0.4);
}

/* ------------ Center Generate Button ------------- */

.center-gen-btn {
    display: flex;
    justify-content: center;
    margin-top: 25px;
}

/* ------------ Wider Upload Boxes Alignment ------------- */

.custom-grid {
    display: flex;
    flex-direction: column;
    gap: 25px;
}

.top-row {
    display: flex;
    gap: 25px;
}
.top-row > div {
    flex: 1;
}

.center-row {
    display: flex;
    justify-content: center;
}
.center-row > div {
    width: 50%;
}

/* ------------ REMOVE STREAMLIT BOXES ------------- */

div[data-testid="stFileUploader"],
div[data-testid="stCameraInput"],
div[data-testid="stFileUploader"] * ,
div[data-testid="stCameraInput"] * {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
}

div[data-testid="stFileUploader"] label,
div[data-testid="stCameraInput"] label {
    display: none !important;
}

.stButton > div {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    box-shadow: none !important;
}
            

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# ------------------------ HEADER ------------------------

st.markdown("""
<div class='header-container'>
    <h1 class='main-title'>🎨 Real-Time Picture Animation</h1>
    <p class='sub-title'>Upload your image, audio, or record video — and let AI animate it.</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# ------------------------ DESCRIPTION ------------------------

left, right = st.columns([1.2, 2])

with left:
    st.markdown("""
        <div class='desc-box'>
            <div class='desc-title'>✨ Project Description</div>
            <div class='desc-text'>
                Our Real-Time Picture Animation system transforms static images 
                into lifelike animations using AI-driven motion generation.  
                <br><br>
                Upload an image, audio, or record a short video — and the system 
                intelligently animates the face with lip-sync, expressions, 
                and head movements in real time.  
                <br><br>
                This tool is designed for creators, educators, and storytellers 
                who want to bring photos to life instantly.
            </div>
        </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------------------------------
# ------------------------ UPLOAD COMPONENTS ------------------------

st.markdown("<div class='custom-grid'>", unsafe_allow_html=True)

# ---------- TOP ROW (IMAGE + AUDIO) ----------
st.markdown("<div class='top-row'>", unsafe_allow_html=True)

# IMAGE
# IMAGE
with st.container():
    st.markdown("<div class='upload-card'>", unsafe_allow_html=True)
    st.markdown("<p class='section-title'>📸 Upload Image</p>", unsafe_allow_html=True)
    image_file = st.file_uploader("", type=["jpg", "jpeg", "png"], key="upload_image")
    if image_file:
        # Use container width and limit maximum width
        st.image(image_file, caption="Uploaded Image", width=200)
    st.markdown("</div>", unsafe_allow_html=True)


# AUDIO
with st.container():
    st.markdown("<div class='upload-card'>", unsafe_allow_html=True)
    st.markdown("<p class='section-title'>🎤 Upload Audio</p>", unsafe_allow_html=True)
    audio_file = st.file_uploader("", type=["mp3", "wav", "aac"], key="upload_audio")
    if audio_file:
        st.audio(audio_file)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------- CENTER ROW (WEBCAM) ----------
st.markdown("<div class='center-row'>", unsafe_allow_html=True)
with st.container():
    st.markdown("<div class='upload-card'>", unsafe_allow_html=True)
    st.markdown("<p class='section-title'>📹 Record Video (Webcam)</p>", unsafe_allow_html=True)
    webcam_video = st.camera_input(" ", key="webcam_input")
    if webcam_video:
        st.video(webcam_video)
    st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ---------- GENERATE BUTTON ----------
st.markdown("<div class='center-gen-btn'>", unsafe_allow_html=True)
generate = st.button("🚀 Generate Animation", key="generate_btn", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# ------------------------ OUTPUT PREVIEW ------------------------
st.markdown("---")
st.markdown("<h3 style='text-align:center;'>🎬 Output Preview</h3>", unsafe_allow_html=True)

if generate:
    st.info("⚙️ Processing… (backend integration required)")
    st.warning("This is frontend only — connect your AI model here later.")
    st.video("https://samplelib.com/lib/preview/mp4/sample-5s.mp4")

# ----------------------------------------------------------------------
# ------------------------ FOOTER ------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#777;'>Made with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
