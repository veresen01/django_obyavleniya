from django.urls import path
from .views import index, rubric_post, PostCreateView

urlpatterns = [
path('add/', PostCreateView.as_view(), name='add'),
path('<int:rubric_id>/', rubric_post, name='rubric_post'),
    path('', index, name='index'),
]
