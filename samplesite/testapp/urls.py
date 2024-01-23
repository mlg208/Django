from django.urls import path
from bboard.views import (#index, by_rubric,
    BbCreateView, BbIndexView)

app_name = 'testapp'

urlpatterns = [
    path('', BbIndexView.as_view(), name='index'),
]