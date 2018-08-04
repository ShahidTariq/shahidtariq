from django.urls import path

from career.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]