# Django MailChimp OAuth
## Description:
The purpose of the project is to implement Mailchimp OAuth with django application.

## Pre reqs:
1. Python
2. pip

## How to run application:
1. install required packages using requirements.txt  
`pip install -r requirements.txt`
2. migrate models to database using  
`python manage.py migrate` or  
`python3 manage.py migrate` (in case you have multiple versions of python installed)
3. add superuser using  
`python manage.py createsuperuser` or  
`python3 manage.py createsuperuser` (in case you have multiple versions of python installed)
4. run application using command  
`python manage.py runserver` or  
`python3 manage.py runserver` (in case you have multiple versions of python installed)
5. Create a mailchimp app
6. Visit django admin at "\admin"
7. log in to admin 
8. In mail chimp credentials model create a new entry with client id, client secret and callback
9. visit application main page while user is logged in.
10. follow steps to and add mailchimp credentials.
11. a new entry in MainChimpToken model will be created with access token and server.
12. access_token and server can be used in further requests to mailchimp api.

# Resources
For details on mailchimp OAuth visit [Link](https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/)