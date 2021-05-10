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

To send notification: (POST) http://127.0.0.1:8000/api/v1/notification/send/
Note: Postman > boday > form-data
notification: Notification1
notification: Quick brown fox jumps over the lazy dog!
access_token:eURcBgsSckRFrYhgE-O7yo:APA91bF64RceddvQLvzOmUAqmp88PrneQN5m38L2ImSiLeQhdrT7k1qkDoea3v6nQx7tdJ3PJ6aJhKfvBlF_MZ01zkwF1AsVcYJft5ERaTVKRpBl3l_cCpJtiunO98gS__-aAcsh3CFM

Postman collection link: https://www.getpostman.com/collections/b06160de7411f328a7a4