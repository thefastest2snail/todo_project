from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/todo/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/todo/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(), name='task-retrieve-update-delete'),
    path('api/login/', user_login, name='get_token'),
    path('api/logout/', user_logout, name='logout'),
    # path('api/password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/todo/<int:pk>/execute/', TaskExecuteView.as_view(), name='task-execute'),
]