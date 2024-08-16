from django.urls import path
from .views import home_view, chatbot_view, login_view, logout_view, signup_view

urlpatterns = [
    path('', home_view, name='home'),
    path('chat/', chatbot_view, name='chat'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
]