from django.urls import path
from accounts.api.views import users_list


urlpatterns = [
    path('', users_list, name='users_list'),
]

