from django.urls import path
from .views import CreateUserView

urlpatterns=[
    path('accounts/', CreateUserView.as_view()),
]