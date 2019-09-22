# calendar_api
simple backend on django_rest_framework for reminding about events

## Python *version: 3.6*
[Required modules](../master/req.txt).

## Launch: *docker-compose up*

## API:

Authorisation from django-rest-auth<br/>

^/rest-auth/login  - email/username + password<br/>
^/rest-auth/logout - token<br/>
^/rest-auth/registration/ email + username + password1 + password2<br/>

^calendar/event/ - POST: add event , GET: get all events<br/>
^calendar/event/day/' - GET: all events for a day<br/>
^calendar/event/month/'- GET: all events for a month<br/>

^holydays/admin/updateholydays/ - run parser - update country list (Admin only).<br/>
^holydays/getcountrys/ - get country list  (access without authorisation)<br/>
^holydays/getholydays/ - get list of holidays for user for a month<br/>