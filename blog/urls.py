from django.urls import path
from blog.views import (HomeView,
                        BlogDetailView,
                        BlogCreateView,
                        BlogUpdateView,
                        BlogDeleteView,
                        )

app_name = 'blog'

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("post/<slug:slug>/", BlogDetailView.as_view(), name='detail'),
    path("post/new", BlogCreateView.as_view(), name='new'),
    path("post/<slug:slug>/edit/", BlogUpdateView.as_view(), name='edit'),
    path("post/<slug:slug>/delete/", BlogDeleteView.as_view(), name='delete'),
]
