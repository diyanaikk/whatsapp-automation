# 📲 WhatsApp Message Automation

This project automates the process of sending WhatsApp messages using Python, `pywhatkit`, and Streamlit. Users can upload a `.txt` file containing phone numbers and custom messages, and the app will schedule and send them automatically.

## 💡 Project Overview

- `main.py`: The **Streamlit-based UI app** for uploading `.txt` files and automating message delivery.
- `app.py`: A **minimal testing version** for sending a single message directly through the terminal.
- `whatsappnum.txt`: A **dummy dataset** containing sample phone numbers and messages.

## 🧪 Features

- Upload `.txt` file with phone numbers and messages
- Schedule messages for specific hours and minutes
- Automate sending via WhatsApp Web
- Clean, user-friendly Streamlit interface

## ⚠️ Requirements & Setup

- Python 3.8 or higher
- WhatsApp Web must be **open and logged in**
- Your system must **stay active and unlocked** while sending messages

### 📦 Install Dependencies

```bash
pip install streamlit pywhatkit pyautogui pandas

📝 Sample File Format (whatsappnum.txt)
Each line should follow this format:

kotlin
Copy
Edit
+91xxxxxxxxxx,Hello there! This is a test message.,15,30
+91xxxxxxxxxx,Reminder: class at 6 PM.,18,00

🚀 How to Use
1. Run the Streamlit App
Copy
Edit
streamlit run main.py
Upload whatsappnum.txt
View the parsed data
Click Send Messages

2. Use the Simple Script
To test with one message manually, run:
Copy
Edit
python app.py
Edit the phone number and message inside app.py.

📌 Important Notes
WhatsApp Web must remain open and logged in

Do not minimize or lock your screen

Avoid interacting with the mouse/keyboard during message automation

🧑‍💻 Author
Diya J Naik
GitHub: @diyanaikk
Copy
Edit