from django.urls import path
from .views import *

urlpatterns = [
    path('create-user/', view=RegisterUser.as_view(), name="create_user"),
    path('login/', view=LoginUser.as_view(), name="login"),
    path('profile/', view=UserProfileAPI.as_view(), name="profile"),
]