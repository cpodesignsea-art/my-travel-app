import streamlit as st
import pandas as pd
from datetime import datetime

# --- APP CONFIG ---
st.set_page_config(page_title="Global Gains", layout="centered")

# --- MOCK DATABASE (We will move this to the cloud later) ---
if 'gyms' not in st.session_state:
    st.session_state.gyms = [
        {"name": "Powerhouse Berlin", "city": "Berlin", "fee": "€15", "sauna": True, "squat_racks": 4},
        {"name": "Muscle Beach", "city": "Venice", "fee": "$10", "sauna": False, "squat_racks": 2}
    ]

# --- UI NAVIGATION ---
menu = ["Gym Finder", "Add/Update Gym", "Progress Tracker", "Healthy Eats"]
choice = st.sidebar.selectbox("Menu", menu)

# --- MODULE 1: GYM FINDER ---
if choice == "Gym Finder":
    st.title("🏋️ Find Your Gains")
    search = st.text_input("Search by City", "Berlin")
    
    results = [g for g in st.session_state.gyms if search.lower() in g['city'].lower()]
    
    for gym in results:
        with st.expander(f"{gym['name']} - {gym['fee']}"):
            st.write(f"📍 Location: {gym['city']}")
            st.write(f"🧖 Sauna: {'✅ Yes' if gym['sauna'] else '❌ No'}")
            st.write(f"🏋️ Squat Racks: {gym['squat_racks']}")
            if st.button(f"Verify Info for {gym['name']}"):
                st.success("Thank you for keeping the data fresh!")

# --- MODULE 2: ADD/UPDATE (Crowdsourcing) ---
elif choice == "Add/Update Gym":
    st.title("➕ Contribute to the Community")
    with st.form("gym_form"):
        name = st.text_input("Gym Name")
        city = st.text_input("City")
        fee = st.text_input("Casual Fee (e.g. $20)")
        sauna = st.checkbox("Has Sauna/Pool?")
        racks = st.number_input("Number of Squat Racks", min_value=0)
        
        if st.form_submit_button("Submit Gym"):
            new_gym = {"name": name, "city": city, "fee": fee, "sauna": sauna, "squat_racks": racks}
            st.session_state.gyms.append(new_gym)
            st.balloons()
            st.success("Gym Added!")

# --- MODULE 3: PROGRESS TRACKER ---
elif choice == "Progress Tracker":
    st.title("📈 Travel Progress")
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Body Weight (kg)", format="%.2f")
    with col2:
        steps = st.number_input("Steps Today", step=1000)
    
    # Simple Logic for Engineers: Volume = Weight * Reps
    st.subheader("Log a Lift")
    lift = st.text_input("Exercise Name (e.g. Bench Press)")
    v_weight = st.number_input("Weight (kg)", key="v_w")
    v_reps = st.number_input("Reps", key="v_r")
    
    volume = v_weight * v_reps
    st.info(f"Set Volume: {volume} kg")