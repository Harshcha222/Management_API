from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from management_api import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Correct the 'api/token/' path
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.login_user, name='login-user'),
    path('clients/register/', views.register_client, name='register-client'),
    path('clients/', views.get_clients, name='get-clients'),
    path('clients/<int:client_id>/', views.modify_client, name='modify-client'),
    path('projects/add/', views.add_project, name='add-project'),
    path('user/projects/', views.get_user_projects, name='user-projects'),
]