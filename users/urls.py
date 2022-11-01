from django.urls import path
from .views import CreateUserView, ListUpdateUSerView

urlpatterns=[
    path('accounts/', CreateUserView.as_view()),
    path('accounts/<str:id>/', ListUpdateUSerView.as_view()),
]