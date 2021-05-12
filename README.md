#If you want to use Social Media Login API and Django Templating follow the below steps!

Step1: Create your virtual env and install the requirements (pip install -r requirements/socialmedia.txt).
Step2: Change the database settings.
step3: Copy environment.txt's data and create .env file at root and paste.
step4: Now create superuser
Step5: Now migrate the migration (python manage.py migrate)

# FACEBOOK

Step6: Now go to the admin panel and add Site by filling these detail:
Domain name: localhost:8000/
Display name: localhost:8000/
Step7: Go to the admin panel and add Social Application from Social Accounts by filling these detail:
Provider: Facebook
Name: FACEBOOK
Client id: _take it from credentials.txt_
Secret key: _take it from credentials.txt_
Key: _leave empty_
Sites: localhost:8000/

NOTE: Use this url (http://127.0.0.1:8000/api/v1/rest-auth/facebook/) with postman or browser.
NOTE: For Facebook API Testing create a test user (account details are given in credentials.txt)
NOTE: For Facebook Templating use url localhost:8000/ insted of 127.0.0.1:8000/

# GOOGLE

For Testing GOOGLE DJANGO TEMPLATE follow these steps:
Step1: Go to the admin panel and add Site by filling these detail:
Domain name: localhost:8000/
Display name: localhost:8000/
Step2: Go to the admin panel and add Social Application from Social Accounts by filling these detail:
Provider: Google
Name: GOOGLE TEMPLATE
Client id: _take it from credentials.txt_
Secret key: _take it from credentials.txt_
Key: _leave empty_
Sites: localhost:8000/

# APPLE API

Step1: Go to admin anel and create a new user and give this user a apple_token of your choice.
Step2: Go to postman > Body > row > JSON
Step3: {
"access_token":"<your token>"
}
Step4: Send

Postman collection link: https://www.getpostman.com/collections/8f12d6444c075405d671
