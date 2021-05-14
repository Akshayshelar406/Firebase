import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
fileName = credentials.Certificate('json_file.json')
firebase_admin.initialize_app(fileName, {
              'databaseURL': 'https://demoproject1-c22c6-default-rtdb.europe-west1.firebasedatabase.app/'
})
ref = db.reference('/')
ref.set({
           'user':
            {
               'subUser1': {
                     'name': 'Akshay',
                     'lname': 'Shelar',
                     'age': 24
              },
               'subUser2': {
                     'name': 'Akshay',
                     'lname': 'Shelar',
                     'age': 24
              }
            }
     })