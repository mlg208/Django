from django.urls import path
from .views import (index)
# , by_rubric,
    # BbCreateView, BbIndexView)

app_name = 'testapp'
urlpatterns = [
    path('', index, name='index'),
]