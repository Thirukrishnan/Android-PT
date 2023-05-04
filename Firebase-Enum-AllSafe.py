import pyrebase

config = {
  "apiKey": "AIzaSyDjteCQ0-ElkfBxVZIZmBfCSPNEYUYcK1g",
  "authDomain": "allsafe-8cef0.firebaseapp.com",
  "databaseURL": "https://allsafe-8cef0.firebaseio.com",
  "storageBucket": "allsafe-8cef0.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

# Enumerate all nodes in the Firebase Realtime Database
results = db.get().val()
for key, value in results.items():
    print(f"{key}: {value}")
