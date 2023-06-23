from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView
from members.views import PasswordsChangeView
# from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove',
         DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cat>/', CategoryView, name='category'),
    path('category-list', CategoryListView, name='category_list'),
    # the url below had to be used here because the members/urls.py doesn't register it for some reason. This is a bit of a wonky fix because I wanted to have things for the member section to be in the members app.
    path('<int:pk>/password/', PasswordsChangeView.as_view(
        template_name='registration/change-password.html')),
]
