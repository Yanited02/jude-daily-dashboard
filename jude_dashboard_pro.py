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
    planned_schedule = planned_schedule.lower()
    if hr > 110 and "rest" in planned_schedule:
        return "⚠️ Elevated heart rate on a rest day. Consider taking it easy or checking in with recovery tools."
    elif hr > 120:
        return "⚠️ Dangerously high heart rate detected. Make sure you're not overexerting or missing recovery."
    return None

def evaluate_schedule_text(text):
    feedback = []
    text = text.lower()
    triggers = {
        "no breakfast": "🥣 Skipping breakfast can reduce energy levels — try oats, eggs or a fruit smoothie.",
        "skipped breakfast": "🥣 Skipping breakfast can reduce energy levels — try oats, eggs or a fruit smoothie.",
        "rest day and gym": "💤 Rest day detected — reduce physical load unless active recovery is planned.",
        "late night": "😴 Late night can reduce sleep quality — consider winding down earlier.",
        "sleep <6": "😴 Less than 6 hours of sleep might affect performance. Try winding down earlier.",
        "no lunch": "🍗 You skipped lunch — consider a balanced protein + carb meal post-training.",
        "junk food": "🍟 Junk food detected — swap for whole foods like grilled chicken, rice and greens.",
        "takeaway": "🍟 Takeaway food detected — opt for home-cooked meals to stay sharp.",
        "energy drink": "⚡ Consider limiting energy drinks. Hydrate with water or electrolytes instead.",
        "no sleep": "🛌 Lack of sleep detected — aim for at least 7-8 hours for optimal recovery.",
        "4 hours": "🛌 Only 4 hours sleep? Try to extend to 7-8 hours for better cognitive and physical performance."
    }
    for trigger, message in triggers.items():
        if trigger in text:
            feedback.append(message)
    if not feedback:
        feedback.append("✅ Looks good. Stay sharp today!")
    return feedback

# ---------- Streamlit UI ---------- #
st.set_page_config(page_title="PulsePoint Dashboard", layout="centered")

st.title("👟 PulsePoint: Jude's Daily Companion")
st.markdown("<hr>", unsafe_allow_html=True)

# Daily Plan Input
st.subheader("📅 What's your day look like?")
schedule_input = st.text_area("Enter your daily plan here (e.g. rest, gym, lunch, sleep...)")
if schedule_input:
    st.markdown("#### AI Review of Your Plan:")
    for line in evaluate_schedule_text(schedule_input):
        st.info(line)

# Wearable Metrics & Check
st.subheader("🩺 Wearable Check-In")
wearables = get_wearable_data()
for k, v in wearables.items():
    st.write(f"**{k}:** {v}")
hr_warning = analyze_heart_rate(wearables['Heart Rate'], schedule_input or "")
if hr_warning:
    st.warning(hr_warning)

st.caption("Built for elite performance. Stay ahead with PulsePoint.")
