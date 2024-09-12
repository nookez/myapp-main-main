from django.contrib import admin
from django.urls import path, include
from myapp import views
from .views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Changed 'home' to 'index'
    path('login/', login_view, name='login'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),

    # เส้นทางของหน้า Coming Soon
    path('coming-soon/<int:id>/', views.coming_soon_detail, name='coming_soon_detail'),
    # เส้นทางของหน้า Celebrity Detail
    path('celebrity/<int:id>/', views.celebrity_detail, name='celebrity_detail'),

    # เส้นทางของหน้า News Detail
    path('news/<int:id>/', views.news_detail, name='news_detail'),

]
