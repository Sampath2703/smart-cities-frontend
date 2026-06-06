import streamlit as st
import requests

backend_url = st.secrets["backend_url"]

st.set_page_config(
    page_title="Smart City AI Dashboard",
    layout="wide"
)

st.sidebar.title("🏙️ Smart City Menu")

page = st.sidebar.radio(
    "Select Module",
    ["Dashboard", "Traffic", "Parking", "Potholes"]
)

st.write("Backend:", backend_url)


# ✅ Reusable function (IMPORTANT FIX)
def call_backend(city, module, question):
    try:
        with st.spinner("Analyzing data..."):
            res = requests.post(
                f"{backend_url}/analyze",
                json={
                    "city": city,
                    "module": module,
                    "question": question
                },
                timeout=30
            )

        try:
            data = res.json()
        except:
            return False, "Invalid JSON response from backend"

        if res.status_code == 200:
            return True, data.get("analysis", "No analysis returned")
        else:
            return False, data.get("detail", res.text)

    except Exception as e:
        return False, str(e)


# ---------------- DASHBOARD ----------------
if page == "Dashboard":
    st.title("📊 Smart City Overview Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🚦 Traffic Status", "Moderate")

    with col2:
        st.metric("🅿️ Parking Availability", "65%")

    with col3:
        st.metric("🕳️ Road Issues", "Low")


# ---------------- TRAFFIC ----------------
elif page == "Traffic":
    st.title("🚦 Traffic Intelligence System")

    city = st.text_input("Enter City", "Hyderabad")
    question = st.text_input("Ask Question", "Reduce traffic congestion")

    if st.button("Analyze Traffic"):
        success, result = call_backend(city, "traffic", question)

        if success:
            st.success(result)
        else:
            st.error(result)


# ---------------- PARKING ----------------
elif page == "Parking":
    st.title("🅿️ Smart Parking System")

    city = st.text_input("Enter City", "Hyderabad")
    question = st.text_input("Ask Question", "Optimize parking system")

    if st.button("Check Parking"):
        success, result = call_backend(city, "parking", question)

        if success:
            st.info(result)
        else:
            st.error(result)


# ---------------- POTHOLES ----------------
elif page == "Potholes":
    st.title("🕳️ Road Damage System")

    city = st.text_input("Enter City", "Hyderabad")
    question = st.text_input("Ask Question", "Detect road damage severity")

    if st.button("Detect Road Issues"):
        success, result = call_backend(city, "potholes", question)

        if success:
            st.warning(result)
        else:
            st.error(result)


st.markdown("---")
st.caption("Smart City AI System 🚀")