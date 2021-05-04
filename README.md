#If you want to use notification API, customadmin and django templating follow below steps!

Step1: Create your virtual env and install the requirements (pip install -r requirements/notification.txt).
Step2: Replace the FIREBASE_API_KEY in .env file with your firebase api key.
Step3: Change the database settings.
Step4: Now migrate the migration (python manage.py migrate)