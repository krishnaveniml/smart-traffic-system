import streamlit as st
from ultralytics import YOLO
import PIL.Image
import pandas as pd
import serial
import serial.tools.list_ports
import time

# --- 1. Page Configuration ---
st.set_page_config(page_title="AI Smart Traffic System", layout="wide", page_icon="🚦")
st.title("🚦 AI Smart Traffic Control Dashboard")
st.markdown("---")

# --- 2. Serial Connection Management ---
# We use session_state to keep the USB connection alive between website refreshes
if 'ser' not in st.session_state:
    st.session_state.ser = None

def get_available_ports():
    return [p.device for p in serial.tools.list_ports.comports()]

# Sidebar Hardware Settings
st.sidebar.header("🔌 Hardware Connection")
ports = get_available_ports()
selected_port = st.sidebar.selectbox("Select ESP32 Port", ports if ports else ["No Ports Found"])

if st.sidebar.button("Connect to ESP32"):
    try:
        if st.session_state.ser:
            st.session_state.ser.close() # Close old connection if it exists
        st.session_state.ser = serial.Serial(selected_port, 115200, timeout=1)
        st.sidebar.success(f"Connected to {selected_port}")
    except Exception as e:
        st.sidebar.error(f"Error: {e}")

# --- 3. Load AI Model (Cached for Speed) ---
@st.cache_resource
def load_traffic_model():
    # 'yolo11s.pt' provides high accuracy for small vehicles
    return YOLO("yolo11s.pt")

model = load_traffic_model()
VEHICLE_CLASSES = [2, 3, 5, 7] # car, motorcycle, bus, truck

# --- 4. Sidebar Image Uploads ---
st.sidebar.header("📸 Lane Inputs")
lane_files = {
    "Lane 1": st.sidebar.file_uploader("Upload Lane 1 (.png, .jpg)", type=['jpg', 'png'], key="L1"),
    "Lane 2": st.sidebar.file_uploader("Upload Lane 2 (.png, .jpg)", type=['jpg', 'png'], key="L2"),
    "Lane 3": st.sidebar.file_uploader("Upload Lane 3 (.png, .jpg)", type=['jpg', 'png'], key="L3"),
    "Lane 4": st.sidebar.file_uploader("Upload Lane 4 (.png, .jpg)", type=['jpg', 'png'], key="L4")
}

# --- 5. Main Processing Logic ---
if st.sidebar.button("🚀 Run Traffic Analysis"):
    cols = st.columns(4)
    counts = []

    # Process each lane
    for i, (lane_name, uploaded_file) in enumerate(lane_files.items()):
        if uploaded_file is not None:
            img = PIL.Image.open(uploaded_file)
            
            # High-Accuracy AI Detection
            # imgsz=1280 ensures distant cars are counted accurately
            results = model.predict(source=img, imgsz=1280, conf=0.25, classes=VEHICLE_CLASSES, verbose=False)
            
            count = len(results[0].boxes)
            counts.append(count)
            
            # Draw boxes on the image for the website
            annotated_img = results[0].plot()
            with cols[i]:
                st.subheader(lane_name)
                st.image(annotated_img, caption=f"Count: {count}", use_container_width=True)
        else:
            counts.append(0) # Default to 0 if no image uploaded
            with cols[i]:
                st.warning(f"{lane_name} Empty")

    # --- 6. Analytics & Hardware Communication ---
    st.divider()
    c1, c2 = st.columns([2, 1])

    with c1:
        st.header("📊 Lane Density Chart")
        chart_df = pd.DataFrame({"Lanes": list(lane_files.keys()), "Vehicles": counts})
        st.bar_chart(chart_df.set_index("Lanes"))

    with c2:
        st.header("📡 ESP32 Data Link")
        if sum(counts) > 0:
            # Find which lane gets priority
            max_val = max(counts)
            priority_idx = counts.index(max_val)
            st.success(f"**PRIORITY:** Lane {priority_idx + 1}")
            
            # Format string for your ESP32: "a,b,c,d\n"
            data_to_send = f"{counts[0]},{counts[1]},{counts[2]},{counts[3]}\n"
            st.code(f"Sending: {data_to_send.strip()}", language="bash")
            
            # Send to Physical Hardware
            if st.session_state.ser and st.session_state.ser.is_open:
                st.session_state.ser.write(data_to_send.encode())
                st.info("✅ Data sent to ESP32 successfully!")
            else:
                st.error("❌ ESP32 not connected. Data not sent.")
        else:
            st.info("Upload images to see lane priority.")

# Footer note
st.sidebar.markdown("---")
st.sidebar.caption("AI Model: YOLOv11s | Communication: PySerial 115200")