# Django - Password Manager

Description:

Password Manager is an application that serves as a wallet of passwords.   
You can store login credentials for web accounts and services to keep those in one place.


How to install and run:

1. Download the project
2. Make sure to install requirements.txt (you can use pip install -r requirements.txt)
3. Go to the folder django_pwdManager and use command: "python manage.py runserver"
4. Ctrl+click on link and go to: http://127.0.0.1:8000/


How to use:

Create your user account and log in. Click "Go to the list of passwords" and you will be redirected to the list of passwords added to your account.

# Password list:

Create new entry - you will be redirected to a form. To create a new entry fill out the form, which consists of the following fields:
1. Service name (required, 1-50 characters)
2. User name (required, 3-30 characters)
3. E-mail (optional)
4. Password (required, 3-30 characters)
5. Comment (optional)

Filter by service name field:
- Case insensitive
- User can provide only part of the service name to show a record
- Leave the field blank and hit SEARCH to remove all filters

You can modify and delete your entries at any time.

### Application account password reset:

You can change your password if you are logged in. If not, you can reset it by providing e-mail address used during the signup process, you will receive a link with further instructions (link is generated in the Terminal)
