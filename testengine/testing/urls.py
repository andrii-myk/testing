from django.urls import path

from . import views

app_name = 'testing'

urlpatterns = [
    path('', views.index, name='tests_index'),
    path('<str:slug>/', views.test_detail, name='test_detail_url')
    # path('add_post', views.add_post, name= 'add_post'),
    # path('<int:post_id>', views.post_detail, name = 'post_detail'),
    
    #path('add_post', views.add_post, name = 'add_post'),
]