import streamlit as st
import random

# पेज सेटअप
st.set_page_config(page_title="For Navya ❤️", page_icon="🌹")

# सेशन स्टेट्स (बटन्स और एनीमेशन ट्रैक करने के लिए)
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'is_forgiven' not in st.session_state:
    st.session_state.is_forgiven = False

# आपके बताए गए 'No' ऑप्शंस की लिस्ट
no_messages = [
    "No 😠", 
    "Sach mai? 🥺", 
    "Phir soch lo... 🤔", 
    "Phir ek bar phir se... 🧐", 
    "Sorry na bebe... Plzzz? 🎀", 
    "Otheeeeee... ❤️"
]

# --- CSS: बैकग्राउंड और हार्ट एनीमेशन ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #ffdde1, #ee9ca7); }
    .stButton>button { border-radius: 30px; border: 2px solid #ff4b4b; background-color: white; color: #ff4b4b; font-weight: bold; width: 100%; }
    
    @keyframes fall {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    .heart {
        position: fixed; top: -10%; user-select: none; pointer-events: none; z-index: 9999;
        animation: fall 3s linear forwards;
    }
    .love-text {
        text-align: center; color: white; font-size: 40px; font-weight: bold; text-shadow: 2px 2px #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

# हार्ट्स जेनरेट करने का फंक्शन
def get_heart_html(heart_symbol):
    heart_html = ""
    for _ in range(30):
        left = random.randint(0, 100)
        duration = random.uniform(2, 4)
        delay = random.uniform(0, 2)
        size = random.randint(20, 45)
        heart_html += f'<div class="heart" style="left:{left}%; animation-duration:{duration}s; animation-delay:{delay}s; font-size:{size}px;">{heart_symbol}</div>'
    return heart_html

# --- UI लॉजिक ---

if not st.session_state.is_forgiven:
    # 'No' पर क्लिक करने पर टूटे हुए दिल गिराना
    if st.session_state.no_count > 0:
        st.markdown(get_heart_html("💔"), unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: white;'>Hi Navya... ❤️</h1>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes, Maaf kiya! 😍"):
            st.session_state.is_forgiven = True
            st.rerun()

    with col2:
        if st.session_state.no_count < len(no_messages):
            current_text = no_messages[st.session_state.no_count]
            if st.button(current_text):
                if "Otheeeeee" in current_text:
                    st.session_state.is_forgiven = True
                else:
                    st.session_state.no_count += 1
                st.rerun()
        else:
            st.write("Please maaf kar do... 🥺")

else:
    # --- माफ़ी के बाद का सरप्राइज ---
    st.markdown(get_heart_html("❤️"), unsafe_allow_html=True)
    st.balloons()
    
    st.markdown("<div class='love-text'>I LOVE U NAVYA SO MUCH ❤️</div>", unsafe_allow_html=True)
    
    # Bear Hug वाला प्यारा सा GIF
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZ4bmZ4bmZ4bmZ4/l4pTfx2qLs35wMSWk/giphy.gif", use_container_width=True)
    
    # आपका एनिमेटेड वीडियो (Autoplay enabled)
    try:
        video_file = open('navya_video.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes, autoplay=True, loop=True)
    except FileNotFoundError:
        st.error("GitHub पर 'navya_video.mp4' नाम की फाइल अपलोड करना न भूलें!")

    st.markdown("<h3 style='text-align: center; color: white;'>Aryan ❤️ Navya</h3>", unsafe_allow_html=True)
