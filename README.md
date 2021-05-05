#If you want to use Social Media Login API and Django Templating follow the below steps!

Step1: Create your virtual env and install the requirements (pip install -r requirements/socialmedia.txt).
Step2: Change the database settings.
step3: Copy environment.txt's data and create .env file at root and paste.
step4: Now create superuser
Step5: Now migrate the migration (python manage.py migrate)

For Testing FACEBOOK API follow these steps:
Step1: Go to the admin panel and add Site by filling these detail:
Domain name: localhost:8000/
Display name: localhost:8000/
Step2: Go to the admin panel and add Social Application from Social Accounts by filling these detail: 
Provider: Facebook
Name: FACEBOOK API
Client id: *take it from credentials.txt* 
Secret key: *take it from credentials.txt*
Key: *leave empty*
Sites: localhost:8000/
Note: Use access token given in credentials.txt

For Testing FACEBOOK DJANGO TEMPLATE follow these steps:
Note1: We're using different account for testing django template
Note2: You have to change .env credentials accordingly
Note3: Use url localhost:8000/ insted of 127.0.0.1:8000/ 
Step1: Go to the admin panel and add Site by filling these detail:
Domain name: localhost:8000/
Display name: localhost:8000/
Step2: Go to the admin panel and add Social Application from Social Accounts by filling these detail: 
Provider: Facebook
Name: FACEBOOK TEMPLATE
Client id: *take it from credentials.txt* 
Secret key: *take it from credentials.txt*
Key: *leave empty*
Sites: localhost:8000/

For Testing GOOGLE DJANGO TEMPLATE follow these steps:
Step1: Go to the admin panel and add Site by filling these detail:
Domain name: localhost:8000/
Display name: localhost:8000/
Step2: Go to the admin panel and add Social Application from Social Accounts by filling these detail: 
Provider: Google
Name: GOOGLE TEMPLATE
Client id: *take it from credentials.txt* 
Secret key: *take it from credentials.txt*
Key: *leave empty*
Sites: localhost:8000/
