from django.urls import path

from .views import *

urlpatterns = [ 
    # Main Home Page
    path('', HomePage.as_view(), name='index'),
    # Explore Page

    # User Dashboard
    path('dashboard/home/', dashboard, name='dashboard-home'),

    # Posts
    path('dashboard/post/create', PostCreatView.as_view(), name='post-create'),
    path('dashboard/post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

