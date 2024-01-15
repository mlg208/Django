from django.urls import path
from .views import login_page, home_page

urlpatterns = [
    path('login/', login_page, name='login'),
    path('home/', home_page, name='home'),
]
