from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
import user.views as user_views
from django.conf.urls.static import static
from django.conf import settings
from chat import views as chat_views

urlpatterns = [
    path('', include('blog.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('chat/', include('chat.urls'), name='chat')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
