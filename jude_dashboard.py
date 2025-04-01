import streamlit as st
from datetime import datetime
import random
import time

# ---------- App Branding ---------- #
APP_NAME = "FieldFocus"
APP_TAGLINE = "Train. Think. Thrive."

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

# ---------- Alert Logic ---------- #
def generate_alerts(sleep, hydrate, stretch, nutrition):
    alerts = []
    if sleep < 6:
        alerts.append("⚠️ Low sleep detected. Prioritize rest tonight.")
    if not hydrate:
        alerts.append("⚠️ Hydration goal not met. Drink more water.")
    if not stretch:
        alerts.append("⚠️ Stretching missed. Consider a short mobility session.")
    if nutrition and any(x in nutrition.lower() for x in ["pizza", "chips", "fried"]):
        alerts.append("⚠️ Junk food logged. Try cleaner options tomorrow.")
    return alerts

# ---------- Streamlit Setup ---------- #
st.set_page_config(page_title=f"{APP_NAME} Dashboard", layout="centered")
st.markdown(f"""
    <h1 style='text-align: center; font-size: 3rem;'>⚽ {APP_NAME}</h1>
    <p style='text-align: center; font-size: 1.1rem; color: gray;'>{APP_TAGLINE}</p>
    <hr style='margin-top: -10px;'>
""", unsafe_allow_html=True)

# ---------- Tabs ---------- #
tabs = st.tabs([
    "Daily Info", "Routine", "Chat", "Tactics",
    "Nutrition", "Calendar", "Mental Prep", "Emotion Check", "Recovery"
])

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

# ---------- Tab 2: Routine ---------- #
with tabs[1]:
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

# ---------- Tab 3: Chat ---------- #
with tabs[2]:
    st.subheader("💬 Chat with Coach")
    user_msg = st.text_input("Message the AI Assistant or Coach:")
    if st.button("Send", key="chat"):
        st.info("You: " + user_msg)
        st.success(get_ai_reply(user_msg))

# ---------- Tab 4: Tactics ---------- #
with tabs[3]:
    st.subheader("🎮 Tactical Insight")
    st.info("Keep your body open when receiving under pressure.")

    st.subheader("📹 Tactical Player Video")
    link, cap = get_youtube_suggestion()
    st.video(link)
    st.caption(cap)

    st.subheader("🧠 Player Notes")
    player_notes = st.text_area("Your thoughts on this tactic or video (for your own or staff reference):")
    if player_notes:
        st.success("✅ Notes saved. Use this space to reflect or discuss with coaching staff.")

# ---------- Tab 5: Nutrition ---------- #
with tabs[4]:
    st.subheader("🍽️ Smart Nutrition Tracker")
    meal = st.text_input("What did you eat today (e.g. cereal, chicken, chips, smoothie)?")
    if meal:
        if any(x in meal.lower() for x in ["chips", "pizza", "fried"]):
            st.warning("⚠️ High-fat foods detected — try switching to grilled options and whole carbs.")
        elif any(x in meal.lower() for x in ["chicken", "eggs", "smoothie", "salad", "oats"]):
            st.success("✅ Great choice! Balanced nutrition fuels top performance.")
        else:
            st.info("🍴 Nutrition logged. Keep variety and hydration in check!")

# ---------- Tab 6: Calendar ---------- #
with tabs[5]:
    st.subheader("🗓️ Weekly Calendar")
    st.markdown("Enter your key weekly events")
    monday = st.text_input("Monday", "Training")
    tuesday = st.text_input("Tuesday", "Gym + Recovery")
    wednesday = st.text_input("Wednesday", "Tactical Drills")
    st.markdown(f"**Your Week:**\n- Monday: {monday}\n- Tuesday: {tuesday}\n- Wednesday: {wednesday}")

# ---------- Tab 7: Mental Prep ---------- #
with tabs[6]:
    st.subheader("🧘 Guided Mental Preparation")
    st.markdown("Take a breath. Visualize yourself owning the pitch.")
    focus_type = st.selectbox("Pick your focus today:", ["Visualization", "Breathing", "Gratitude"])
    if focus_type == "Visualization":
        st.info("Picture your perfect pass, tackle, or goal. Replay it mentally with calmness.")
    elif focus_type == "Breathing":
        st.info("Try box breathing: inhale 4s, hold 4s, exhale 4s, hold 4s. Repeat 4x.")
    else:
        st.info("Think of 3 things you’re grateful for — gratitude strengthens mindset.")

# ---------- Tab 8: Emotion Check ---------- #
with tabs[7]:
    st.subheader("😌 Emotional Check-In")
    mood = st.radio("How are you feeling?", ["🔥 On fire", "🙂 Focused", "😴 Tired", "😟 Nervous", "😢 Low"])
    if mood == "😟 Nervous":
        st.info("Reach out to family or teammates for support. Confidence comes from routine.")
    elif mood == "😢 Low":
        st.warning("It's okay to not feel 100%. Reflect, rest, and reset. You're still elite.")
    elif mood == "😴 Tired":
        st.warning("Energy seems low. Prioritize hydration, stretching, and early sleep.")
    else:
        st.success("You're in a good headspace. Keep it up!")

# ---------- Tab 9: Recovery ---------- #
with tabs[8]:
    st.subheader("🛌 Personalized Recovery Tracker")
    hours_slept = st.slider("How many hours did you sleep last night?", 0, 12, 8)
    did_stretch = st.checkbox("Did you stretch today?")
    did_hydrate = st.checkbox("Have you drunk 2L+ of water today?")

    alerts = generate_alerts(hours_slept, did_hydrate, did_stretch, meal if 'meal' in locals() else "")
    if alerts:
        for a in alerts:
            st.warning(a)
    else:
        st.success("✅ You’re recovering like a pro. Stay consistent!")

st.caption(f"Made with ⚽ by {APP_NAME} – {APP_TAGLINE}")
