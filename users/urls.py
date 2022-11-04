from django.urls import path
from .views import CreateUserView, ListDetailUSerView
from rest_framework.authtoken.views import obtain_auth_token

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

urlpatterns=[
    path('accounts/', CreateUserView.as_view()),
    path('accounts/<str:id>/', ListDetailUSerView.as_view()),
    path("login/", obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularRedocView.as_view(url_name='schema'), name='redoc')
]
