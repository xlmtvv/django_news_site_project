from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('', cache_page(60)(HomeNews.as_view()), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news')
]
