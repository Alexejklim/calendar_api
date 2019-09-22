# calendar_api
simple backend on django_rest_framework for reminding about events

Python version: 3.6
[Required modules](../master/req.txt).

Launch: docker-compose up

API:

Authorisation from django-rest-auth\n
^/rest-auth/login  - email/username + password\n
^/rest-auth/logout - token\n
^/rest-auth/registration/ email + username + password1 + password2\n

^calendar/event/ - POST: add event , GET: get all events\n
^calendar/event/day/' - GET: all events for a day\n
^calendar/event/month/'- GET: all events for a month\n

^holydays/admin/updateholydays/ - run parser - update country list (Admin only).\n
^holydays/getcountrys/ - get country list  (access without authorisation)\n
^holydays/getholydays/ - get list of holidays for user for a month\n
