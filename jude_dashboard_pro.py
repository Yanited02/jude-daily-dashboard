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
    text = text.lower()
    if "no breakfast" in text or "skipped breakfast" in text:
        feedback.append("🥣 Skipping breakfast can reduce energy levels — try oats, eggs or a fruit smoothie.")
    if "rest day" in text and "gym" in text:
        feedback.append("💤 Rest day detected — reduce physical load unless active recovery is planned.")
    if "late night" in text or ("sleep" in text and "<6" in text):
        feedback.append("😴 Less than 6 hours of sleep might affect performance. Try winding down earlier.")
    if "no lunch" in text:
        feedback.append("🍗 You skipped lunch — consider a balanced protein + carb meal post-training.")
    if "junk food" in text or "takeaway" in text:
        feedback.append("🍟 Junk food detected — swap for whole foods like grilled chicken, rice and greens.")
    if "energy drink" in text:
        feedback.append("⚡ Consider limiting energy drinks. Hydrate with water or electrolytes instead.")
    if "no sleep" in text or "4 hours" in text:
        feedback.append("🛌 Lack of sleep detected — aim for at least 7-8 hours for optimal recovery.")
    if not feedback:
        feedback.append("✅ Looks good. Stay sharp today!")
    return feedback

# (The rest of the code remains unchanged)
