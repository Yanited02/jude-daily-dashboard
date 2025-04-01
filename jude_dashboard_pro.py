import streamlit as st
from datetime import datetime
import random
import time

# ---------- Simulated Modules ---------- #
def get_wearable_data():
    return {
        "Heart Rate": random.randint(58, 125),
        "Body Temp": round(random.uniform(36.1, 37.3), 1),
        "Steps Today": random.randint(3000, 12000),
        "Readiness Score": random.randint(60, 100),
        "Sleep Duration (hrs)": round(random.uniform(6.5, 9.2), 1)
    }

def analyze_heart_rate(hr, planned_schedule):
    if hr > 110 and "rest" in planned_schedule.lower():
        return "⚠️ Elevated heart rate on a rest day. Consider taking it easy or checking in with recovery tools."
    elif hr > 120:
        return "⚠️ Dangerously high heart rate detected. Make sure you're not overexerting or missing recovery."
    return None

def evaluate_schedule_text(text):
    feedback = []
    if "no breakfast" in text.lower() or "skipped breakfast" in text.lower():
        feedback.append("🥣 Skipping breakfast can reduce energy levels — try oats, eggs or a fruit smoothie.")
    if "rest day" in text.lower() and "gym" in text.lower():
        feedback.append("💤 Rest day detected — reduce physical load unless active recovery is planned.")
    if "late night" in text.lower() or "sleep" in text.lower() and "<6" in text:
        feedback.append("😴 Less than 6 hours of sleep might affect performance. Try winding down earlier.")
    if "no lunch" in text.lower():
        feedback.append("🍗 You skipped lunch — consider a balanced protein + carb meal post-training.")
    if not feedback:
        feedback.append("✅ Looks good. Stay sharp today!")
    return feedback

chat_log = []

def send_message(user, msg):
    chat_log.append((datetime.now().strftime("%H:%M"), user, msg))
    return True

def get_chat_history():
    return chat_log[-5:]

def get_ai_reply(message):
    if "defend" in message.lower():
        return "Coach: Stay tighter on the second ball and watch your positioning."
    elif "press" in message.lower():
        return "Coach: Initiate the press from the striker and close the midfield passing lanes."
    else:
        return "Coach: Good question — let's look at footage later."

def get_youtube_suggestion():
    return "https://www.youtube.com/watch?v=1XnBzZsLJXA", "Bellingham's midfield positioning and awareness."

def evaluate_routine(routine_items):
    feedback = []
    for item in routine_items:
        if "carb" in item.lower() or "pasta" in item.lower():
            feedback.append("⚠️ You've had high carbs before training — try eggs or lean protein for better energy balance.")
        if "skip" in item.lower() or "none" in item.lower():
            feedback.append("⚠️ Missed meal or session detected — this could impact your readiness score.")
    return feedback

# ---------- UI Styling ---------- #
st.markdown("""
    <style>
        body { background-color: #121212; color: #ffffff; }
        .main, .block-container { padding: 1rem 0.5rem; background-color: #121212; }
        .card { background-color: #1e1e1e; border-radius: 14px; padding: 1.2rem; margin-bottom: 1rem; box-shadow: 0 2px 6px rgba(0,0,0,0.2); }
        .stButton > button { background-color: #007aff; color: white; border-radius: 10px; padding: 10px 20px; font-size: 16px; border: none; }
        .stProgress > div > div { background-color: #34c759; }
        h1, h2, h3, h4, h5, h6 { color: #ffffff; }
        .stTextInput > div > input, .stSelectbox > div > div, .stTextArea textarea {
            background-color: #2c2c2e !important;
            color: white !important;
            border-radius: 10px;
            border: 1px solid #3a3a3c;
        }
        .stMarkdown hr, .stMarkdown div:empty {
            display: none !important;
        }
        .block-container > div > div > div > div[data-testid="stVerticalBlock"]:not(:has(.st-expander)) {
            padding: 0 !important;
            margin: 0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Intro Splash ---------- #
st.markdown("<h1 style='text-align: center; font-size: 40px;'>👟 PulsePoint</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Where performance meets lifestyle</p>", unsafe_allow_html=True)
with st.spinner("Warming up..."):
    time.sleep(2.5)

# ---------- Daily Overview Input ---------- #
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### 📆 Daily Schedule Input")
schedule_input = st.text_area("What does your day look like today? (Training, meetings, rest?)")
if schedule_input:
    suggestions = evaluate_schedule_text(schedule_input)
    for tip in suggestions:
        st.info(tip)
st.markdown("</div>", unsafe_allow_html=True)

# ---------- Tabs ---------- #
st.title("Jude’s Daily Dashboard")
st.subheader("🗓️ " + datetime.now().strftime("%A, %d %B %Y"))
matchday = st.checkbox("Matchday Mode", value=False)

wearables = get_wearable_data()
hr_warning = analyze_heart_rate(wearables['Heart Rate'], schedule_input or "")
if hr_warning:
    st.warning(hr_warning)

vest_metrics = {
    "Daily Vest": {"Hydration": random.randint(70, 100), "Heart Rate": random.randint(60, 90), "Body Temp": round(random.uniform(36.5, 37.5), 1)},
    "Night Vest": {"REM Sleep %": random.randint(20, 35), "Sleep Duration": random.randint(6, 9), "Resting HR": random.randint(50, 65)},
    "Relax Vest": {"Stress Level": random.randint(1, 10), "Breathing Rate": random.randint(12, 18), "Recovery Score": random.randint(60, 100)}
}

# ---------- Tabs ---------- #
tabs = st.tabs(["Fitness", "Routine", "Chat", "Tactics"])

# -- Tab 1: Fitness -- #
with tabs[0]:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🔗 Wearable Fitness Insights")
    for key, val in wearables.items():
        st.write(f"**{key}:** {val}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🦾 Tri-Vest Metrics")
    for vest, data in vest_metrics.items():
        with st.expander(vest):
            for k, v in data.items():
                st.write(f"**{k}:** {v}")
    st.markdown("</div>", unsafe_allow_html=True)

# -- Tab 2: Routine -- #
with tabs[1]:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 📋 Daily Routine (Editable)")
    user_routine = st.text_area("List your current routine items (one per line):", """Wake up 7:30AM, hydration + mobility
Breakfast: eggs, avocado toast, smoothie
Team training 10AM - 12PM
Lunch + Recovery Nap
Gym: Mobility & core work
Film review session (30 mins)
Dinner: lean protein + complex carbs
Spanish practice (Duolingo or app)
10 mins meditation + Sleep by 10:30PM""")
    routine_lines = [line.strip() for line in user_routine.split("\n") if line.strip()]
    for item in routine_lines:
        st.write(f"- {item}")
    feedback = evaluate_routine(routine_lines)
    if feedback:
        st.warning("\n".join(feedback))
    st.markdown("</div>", unsafe_allow_html=True)

# -- Tab 3: Chat -- #
with tabs[2]:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 💬 Pulse Chat")
    user_input = st.text_input("Message Coach or AI Assistant:")
    if st.button("Send"):
        send_message("Jude", user_input)
        reply = get_ai_reply(user_input)
        send_message("Coach", reply)
    for timestamp, user, msg in get_chat_history():
        st.markdown(f"`{timestamp}` **{user}**: {msg}")
    st.markdown("</div>", unsafe_allow_html=True)

# -- Tab 4: Tactics -- #
with tabs[3]:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🎮 Tactical Tip")
    st.info(random.choice([
        "Stay compact in midfield and press as a unit.",
        "Watch for overlapping runs on the left wing.",
        "Keep your body open when receiving under pressure.",
        "Switch play quickly to exploit space.",
        "Anticipate second balls and stay alert."
    ]))
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 📹 Player Comparison Video")
    yt_link, caption = get_youtube_suggestion()
    st.video(yt_link)
    st.caption(caption)
    st.markdown("</div>", unsafe_allow_html=True)

st.caption("⚽ PulsePoint – Elite lifestyle tracking inspired by Jude.")
