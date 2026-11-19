import streamlit as st
import pandas as pd

st.title("Arduino LED Monitoring System")

st.write("Control and monitor LED blinking intervals.")

mode = st.selectbox(
    "Select LED Blinking Mode",
    ["Normal (1000 ms)", "Fast (200 ms)", "Slow (3000 ms ON)"]
)

if mode == "Normal (1000 ms)":
    on_time = 1000
    off_time = 1000
elif mode == "Fast (200 ms)":
    on_time = 200
    off_time = 200
else:
    on_time = 3000
    off_time = 1000

st.success("LED BLINKING")
st.metric("ON Duration", f"{on_time} ms")
st.metric("OFF Duration", f"{off_time} ms")

data = pd.DataFrame({
    "Mode": ["Normal", "Fast", "Slow"],
    "ON Duration": [1000, 200, 3000],
    "OFF Duration": [1000, 200, 1000]
})

st.subheader("LED Blinking Comparison")
st.dataframe(data, use_container_width=True)
