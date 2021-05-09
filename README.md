#If you want to use notification API, customadmin and django templating follow below steps!

Step1: Create your virtual env and install the requirements (pip install -r requirements/notification.txt).
Step2: Replace the FIREBASE_API_KEY in .env file with your firebase api key.
Step3: Change the database settings.
step4: Copy environment.txt's data and create .env file at root and paste.
step5: Now create superuser
Step6: While creating new user you need credential that you can get from credentials.txt
Note: We have only one credential you can use this same for all users.
Step7: Now migrate the migration (python manage.py migrate)

Note: To test send notification API for single user you can test directly, but for multi user cred2 and multi credential list and comment the single credential list.  

save and send at the same time
new notification without reload 