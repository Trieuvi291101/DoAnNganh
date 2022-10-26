from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import cloudinary
from flask_login import LoginManager
from twilio.rest import Client

app = Flask(__name__)

app.secret_key = "super key" #akj+fg823762531341=2901r-9sd-7g2f98r3sa8d1-2751849
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Trieuvi2911@localhost/phongkhamdb?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

cloudinary.config(
    cloud_name='i-h-c-m',
    api_key='482771674861723',
    api_secret='UcuyEfGi4mWdqTG2f1F1e_jfJUE'
)


#twilio infomation
keys = {
    'account_sid': 'AC205cfd2eb535ffb9ed06233d7a370545',
    'auth_token': 'f5a23510c1f180cbd4c821de4e30cf4a',
    'twilio_number': '+14255377447'
}


#client = Client(account_sid, auth_token)
client = Client(keys['account_sid'], keys['auth_token'])
#
# const firebaseConfig = {
#   apiKey: "AIzaSyC3Mk8KPfPRP8L3NVbfX-8qUW60wfNAtW8",
#   authDomain: "chat-clinic-75bdf.firebaseapp.com",
#   projectId: "chat-clinic-75bdf",
#   storageBucket: "chat-clinic-75bdf.appspot.com",
#   messagingSenderId: "778252912400",
#   appId: "1:778252912400:web:c443563ed25326f52e8795",
#   measurementId: "G-92Y3E8P0ZM"
# };
#
# // Initialize Firebase
# const app = initializeApp(firebaseConfig);
# const analytics = getAnalytics(app);

db = SQLAlchemy(app=app)
login = LoginManager(app=app)
