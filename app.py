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

if page == "Dashboard":
    st.title("📊 Smart City Overview Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🚦 Traffic Status", "Moderate")

    with col2:
        st.metric("🅿️ Parking Availability", "65%")

    with col3:
        st.metric("🕳️ Road Issues", "Low")


elif page == "Traffic":
    st.title("🚦 Traffic Intelligence System")

    city = st.text_input("Enter City", "Hyderabad")
    question = st.text_input("Ask Question", "Reduce traffic congestion")

    if st.button("Analyze Traffic"):
        try:
            res = requests.post(
                f"{backend_url}/analyze",
                json={
                    "city": city,
                    "module": "traffic",
                    "question": question
                },
                timeout=30
            )

            if res.status_code == 200:
                data = res.json()

                st.subheader("🤖 AI Analysis")
                st.success(data["analysis"])
            else:
                st.error(res.text)

        except Exception as e:
            st.error(f"Request failed: {str(e)}")


elif page == "Parking":
    st.title("🅿️ Smart Parking System")

    city = st.text_input("Enter City", "Hyderabad")
    question = st.text_input("Ask Question", "Optimize parking system")

    if st.button("Check Parking"):
        try:
            res = requests.post(
                f"{backend_url}/analyze",
                json={
                    "city": city,
                    "module": "parking",
                    "question": question
                },
                timeout=30
            )

            if res.status_code == 200:
                data = res.json()

                st.subheader("🤖 AI Analysis")
                st.info(data["analysis"])
            else:
                st.error(res.text)

        except Exception as e:
            st.error(f"Request failed: {str(e)}")


elif page == "Potholes":
    st.title("🕳️ Road Damage System")

    city = st.text_input("Enter City", "Hyderabad")
    question = st.text_input("Ask Question", "Detect road damage severity")

    if st.button("Detect Road Issues"):
        try:
            res = requests.post(
                f"{backend_url}/analyze",
                json={
                    "city": city,
                    "module": "potholes",
                    "question": question
                },
                timeout=30
            )

            if res.status_code == 200:
                data = res.json()

                st.subheader("🤖 AI Analysis")
                st.warning(data["analysis"])
            else:
                st.error(res.text)

        except Exception as e:
            st.error(f"Request failed: {str(e)}")

st.markdown("---")
st.caption("Smart City AI System 🚀")