# calendar_api
simple backend on django_rest_framework for reminding about events

Python version: 3.6
[Required modules](../master/req.txt).

Launch: docker-compose up

API:

Authorisation from django-rest-auth
^/rest-auth/login  - email/username + password
^/rest-auth/logout - token
^/rest-auth/registration/ email + username + password1 + password2

^calendar/event/ - POST: add event , GET: get all events
^calendar/event/day/' - GET: all events for a day
^calendar/event/month/'- GET: all events for a month

^holydays/admin/updateholydays/ - run parser - update country list (Admin only).
^holydays/getcountrys/ - get country list  (access without authorisation)
^holydays/getholydays/ - get list of holidays for user for a month
