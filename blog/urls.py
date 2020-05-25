from django.contrib import admin
from django.urls import path, include
import blog.views as views
import user.views as user_views
from django.conf.urls.static import static
from django.conf import settings
from .views import (PostListView, CreateNewView, PostDetailView,
                    UserPostListView, PostUpdateView, PostDeleteView)

urlpatterns = [
    path('',
         PostListView.as_view(template_name='blog/home.html'),
         name='blog-home'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-post'),
    path('change-profile/', user_views.changeProfile, name='change-profile'),
    path('new/',
         CreateNewView.as_view(template_name='blog/post_form.html'),
         name='new-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/update/<int:pk>',
         PostUpdateView.as_view(template_name='blog/post_update.html'),
         name='post-update'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post-delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
