from django.urls import path
from .views import AllBlogsView

urlpatterns = [
    path('blogs/', AllBlogsView.as_view())
]
