from django.urls import path
from .views import CreateUserView, ListUpdateUSerView

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('accounts/', CreateUserView.as_view()),
    path('accounts/<str:id>/', ListUpdateUSerView.as_view()),
    path("login/", obtain_auth_token)
]