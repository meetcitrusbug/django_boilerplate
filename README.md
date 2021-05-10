#If you want to use notification API, customadmin and django templating follow below steps!

Step1: Create your virtual env and install the requirements (pip install -r requirements/notification.txt).
Step2: Replace the FIREBASE_API_KEY in .env file with your firebase api key.
Step3: Change the database settings.
step4: Copy environment.txt's data and create .env file at root and paste.
step5: Now create superuser
Step6: While creating new user you need credential that you can get from credentials.txt
Note: We have only one credential you can use this same for all users.
Step7: Now migrate the migration (python manage.py migrate)

NOTE: To test notification API use these urls with postman.
To get all notifications: (GET) http://127.0.0.1:8000/api/v1/notification/notifications/
To read a notification: (POST) http://127.0.0.1:8000/api/v1/notification/read/1/
To read all notifications: (POST) http://127.0.0.1:8000/api/v1/notification/read/
To remove a notifications: (DELETE) http://127.0.0.1:8000/api/v1/notification/remove/1/
To remove all notifications: (DELETE) http://127.0.0.1:8000/api/v1/notification/remove/

Note: To test send notification API for single user you can test directly, but for multi user, go to the notification.view and uncomment cred2 and multi credential list and do comment the single credential list.  

To send notification: (POST) http://127.0.0.1:8000/api/v1/notification/send/