from django.urls import path

from . import views

app_name = 'testing'

urlpatterns = [
    path('list/', views.index, name='tests_index'),
    path('list/<str:slug>/', views.TestDetail.as_view(), name='test_detail_url'),
    path('questions/', views.QuestionsView.as_view(), name='questions_url'),
    path('questions/create/', views.QuestionCreate.as_view(), name='question_create_url'),
    path('questions/update/<int:id>/', views.QuestionUpdate.as_view(), name='question_update_url'),
    path('questions/delete/<int:id>/', views.QuestionDelete.as_view(), name='question_delete_url'),

]