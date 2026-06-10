import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://YOUR_PROJECT_ID-default-rtdb.firebaseio.com/"
})

# Reference to database
ref = db.reference("users")

# Add data
ref.push({
    "name": "Brindha",
    "age": 18,
    "city": "Salem"
})

print("Data added successfully!")