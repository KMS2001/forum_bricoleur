from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil
    path('publications/', views.liste_publications, name='liste_publications'),
    path('publication/<int:publication_id>/', views.detail_publication, name='detail_publication'),
    path('creer/', views.creer_publication, name='creer_publication'),

    # URLs d'authentification
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # URL pour l'inscription
    path('signup/', views.signup_view, name='signup'),
]
