import pyautogui, time
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r"firebase-key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

clicks = 0
for i in range(5):
    pyautogui.click()
    clicks += 1
    print("Clicked:", clicks)

    doc_ref = db.collection("clicks").document()
    doc_ref.set({
        "count": clicks,
        "time": time.strftime("%Y-%m-%d %H:%M:%S")
    })

    time.sleep(0.5)

print("Total clicks:", clicks)