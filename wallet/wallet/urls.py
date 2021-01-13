from django.contrib import admin
from django.urls import path
from balance import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup1, name="signup"),
    path('', views.user_login, name="login"),
    path('home/', views.home, name="home"),
    path('Logout/', views.Logout, name="Logout"),
    path('delete_history/<int:pid>/', views.delete_history, name="delete_history"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
