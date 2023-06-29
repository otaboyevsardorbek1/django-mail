# django-mail
### Sending Emails in Django Python web framework

#### You have to follow these steps:-
* First of all you have to create a django project and an app.
* settings.py
(add some line of code in this file)
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_USE_TLS =True

EMAIL_PORT = 587

EMAIL_HOST_USER = 'your email id'

EMAIL_HOST_PASSWORD = 'password'
```
* settings in your Gmail Account
```
* Open your email account in Browser
* go to 'Manage your google account'
* go to 'Security' tab in left side bar
* Turn ON the Toggle Button in 'Less Secure App Access' option in Security tab.
```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/unyxpommfcl9jt1eymdo.PNG)

* After doing these settings you can download repo

* TEST
