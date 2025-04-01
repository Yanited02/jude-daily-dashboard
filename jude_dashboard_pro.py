import streamlit as st
from datetime import datetime
import random
import time

# ---------- Simulated Modules ---------- #
def get_wearable_data():
    return {
        "Heart Rate": random.randint(58, 95),
        "Body Temp": round(random.uniform(36.1, 37.3), 1),
        "Steps Today": random.randint(3000, 12000),
        "Readiness Score": random.randint(60, 100),
        "Sleep Duration (hrs)": round(random.uniform(6.5, 9.2), 1)
    }

def get_ai_reply(message):
    if "defend" in message.lower():
        return "Coach: Stay tighter on the second ball and watch your positioning."
    elif "press" in message.lower():
        return "Coach: Initiate the press from the striker and close the midfield passing lanes."
    else:
        return "Coach: Good question — let's look at footage later."

def get_youtube_suggestion():
    return "https://www.youtube.com/watch?v=1XnBzZsLJXA", "Bellingham's midfield positioning and awareness."

# ---------- Streamlit Setup ---------- #
st.set_page_config(page_title="PulsePoint Dashboard", layout="centered")
st.title("👟 PulsePoint: Jude's Daily Companion")

# ---------- Tabs ---------- #
tabs = st.tabs(["Daily Info", "Chat", "Tactics", "New Features"])

# ---------- Tab 1: Daily Info ---------- #
with tabs[0]:
    matchday = st.checkbox("Matchday Mode", value=False)
    if matchday:
        st.info("You're in Matchday Mode. Stay focused — phone use limited to key reminders.")

    st.subheader("📅 Daily Schedule")
    schedule_input = st.text_area("What does your day look like today? (e.g. rest, gym, nutrition, sleep...)")

    st.subheader("🩺 Wearable Check-In")
    data = get_wearable_data()
    for k, v in data.items():
        st.write(f"**{k}:** {v}")

    if data['Heart Rate'] > 110 and "rest" in schedule_input.lower():
        st.warning("⚠️ High heart rate detected on a rest day. Monitor closely and recover well.")
    elif data['Heart Rate'] > 120:
        st.warning("⚠️ Dangerously high heart rate detected. Hydrate and consider contacting a medical pro if this continues.")

    st.subheader("📋 Daily Routine")
    def get_routine():
        return [
            "Wake up 7:30AM, hydration + mobility",
            "Breakfast: eggs, avocado toast, smoothie",
            "Team training 10AM - 12PM",
            "Lunch + Recovery Nap",
            "Gym: Mobility & core work",
            "Film review session (30 mins)",
            "Dinner: lean protein + complex carbs",
            "Spanish practice (Duolingo or app)",
            "10 mins meditation + Sleep by 10:30PM"
        ]
    for item in get_routine():
        st.write(f"- {item}")

# ---------- Tab 2: Chat ---------- #
with tabs[1]:
    st.subheader("💬 Chat with Coach")
    user_msg = st.text_input("Message the AI Assistant or Coach:")
    if st.button("Send", key="chat"):
        st.info("You: " + user_msg)
        st.success(get_ai_reply(user_msg))

# ---------- Tab 3: Tactics ---------- #
with tabs[2]:
    st.subheader("🎮 Tactical Insight")
    st.info("Keep your body open when receiving under pressure.")

    st.subheader("📹 Tactical Player Video")
    link, cap = get_youtube_suggestion()
    st.video(link)
    st.caption(cap)

# ---------- Tab 4: New Features Placeholder ---------- #
with tabs[3]:
    st.subheader("🚧 More Features Coming Soon")
    st.markdown("Stay tuned for nutrition tracking, calendar views, mental prep tools, and more!")

st.caption("⚽ PulsePoint – Lifestyle dashboard inspired by Jude.")
