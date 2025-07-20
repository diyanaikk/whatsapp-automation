import pandas as pd
import pywhatkit as kit
import datetime
import time
import pyautogui  # <-- Make sure this is imported

# Load your dataset
df = pd.read_csv("whatsappnum.txt")
df = df.head(3)  # For testing
df['phone number'] = df['phone number'].astype(str).apply(lambda x: '+91' + x.strip())

# Set starting time
now = datetime.datetime.now()
hour = now.hour
minute = (now.minute + 2) % 60
if now.minute + 2 >= 60:
    hour = (hour + 1) % 24

# Loop through each message
for index, row in df.iterrows():
    phone = row['phone number']
    message = row['message']
    print(f"Scheduling message to {phone} at {hour}:{minute:02d}")

    try:
        # Schedule the message
        kit.sendwhatmsg(phone, message, hour, minute, wait_time=10, tab_close=False)

        # Wait until the message is loaded
        time.sleep(15)

        # Automatically press Enter to send
        pyautogui.press("enter")

    except Exception as e:
        print(f"Failed to send to {phone}: {e}")

    # Move time forward
    minute = (minute + 1) % 60
    if minute == 0:
        hour = (hour + 1) % 24

    # Short delay before next message
    time.sleep(5)
