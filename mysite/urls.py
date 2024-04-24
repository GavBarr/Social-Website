"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from socialapp import views
from django.contrib import admin
from django.urls import path, include
from socialapp import views as user_views
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/<int:profile_id>', views.profile, name='profile'),
    path('view_profile/<int:profile_id>', user_views.view_profile, name='view_profile'),
    path('search/', user_views.search, name='search'),
    path('welcome_page/', user_views.welcome_page, name='welcome_page'),
    path('follow_profile/<int:follow_profile_id>/<str:follow_profile_name>', user_views.follow_profile, name='follow_profile'),
    path('unfollow_profile/<int:follow_profile_id>/<str:follow_profile_name>', user_views.unfollow_profile, name='unfollow_profile'),
    path('add_post/<int:profile_id>', user_views.add_post, name='add_post'),
    path('delete_post/<int:post_id>/<int:profile_id>', views.delete_post, name='delete_post'),
    path('like_post/<int:post_id>/<int:profile_id>', views.like_post, name='like_post'),
    path('dislike_post/<int:post_id>/<int:profile_id>', views.dislike_post, name='dislike_post'),
    path('like_post_profile/<int:post_id>/<int:profile_id>', views.like_post_profile, name='like_post_profile'),
    path('dislike_post_profile/<int:post_id>/<int:profile_id>', views.dislike_post_profile, name='dislike_post_profile'),
    path('register/', user_views.register, name='register'),
    path('explore/<int:profile_id>', views.explore_page, name='explore'),
    path('post_feed/<int:profile_id>', views.post_feed, name='post_feed'),
    path('delete_note/<int:note_id>/<int:profile_id>', views.delete_note, name='delete_note'),
    path('login/', authentication_views.LoginView.as_view(template_name='socialapp/login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='socialapp/logout.html'), name='logout'),
    path('add_note/<int:profile_id>', user_views.add_note, name='add_note'),
    path('edit_note/<int:note_id>/<int:profile_id>', user_views.edit_note, name='edit_note'),
    path('profile_settings/<int:profile_id>', user_views.profile_settings, name='profile_settings'),
]
urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

