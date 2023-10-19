
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('comment_page',views.comment_page,name="comment_page"),
]
