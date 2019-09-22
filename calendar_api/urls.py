
from django.conf.urls import url
from django.urls import path, include
from rest_auth.registration.views import VerifyEmailView
from django.views.generic import TemplateView
from allauth.account.views import ConfirmEmailView

urlpatterns = [

    path('calendar/', include('mainapp.urls')),
    path('holydays/', include('holydays.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/registration/verify-email/', VerifyEmailView.as_view(),
         name='account_email_verification_sent'),
    url(r'^rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
          name='account_confirm_email'),
]


