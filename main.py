import streamlit as st
import pandas as pd
import pywhatkit as kit
import pyautogui
import datetime
import time

st.set_page_config(page_title="WhatsApp Message Automation", page_icon="📲")
st.title("📲 WhatsApp Message Automation")

# File uploader
uploaded_file = st.file_uploader("Upload your message file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file, sep=",")
    st.success("✅ File uploaded successfully!")
    st.dataframe(df)

    if st.button("Send Messages"):
        st.info("📤 Sending messages... Make sure WhatsApp Web is logged in and browser is ready.")

        # Prefix +91 to phone numbers
        df['phone number'] = df['phone number'].astype(str).apply(lambda x: '+91' + x.strip())

        # Start time: 2 minutes from now
        now = datetime.datetime.now()
        hour = now.hour
        minute = (now.minute + 2) % 60
        if now.minute + 2 >= 60:
            hour = (hour + 1) % 24

        # Loop through rows and send messages
        for index, row in df.iterrows():
            phone = row['phone number']
            message = row['message']
            st.write(f"📨 Scheduling to {phone} at {hour}:{minute:02d}")

            try:
                kit.sendwhatmsg(phone, message, hour, minute, wait_time=10, tab_close=False)
                time.sleep(15)
                pyautogui.press("enter")
            except Exception as e:
                st.error(f"❌ Failed to send to {phone}: {e}")

            # Update time for next message
            minute = (minute + 1) % 60
            if minute == 0:
                hour = (hour + 1) % 24
            time.sleep(5)

        st.success("✅ All messages scheduled!")
