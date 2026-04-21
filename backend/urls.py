from django.urls import path
from .views import  UserView,UserDetailView

urlpatterns =[
    path('api/users', UserView.as_view(), name='users'),
    path('api/users/<int:id>', UserDetailView.as_view(), name='user-detail')
]