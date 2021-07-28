from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # first slug in angle brckts is called a path converter, second slug is a keyword name
    # the keyword name matches the "slug" parameter in the get method (the scond slug can be named anything)
]