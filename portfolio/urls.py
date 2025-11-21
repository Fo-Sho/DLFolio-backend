from django.urls import path
from .views import api_overview, ProjectList, ProjectDetail
from . import views
urlpatterns =[
    path('api/projects/', views.project_list),
    path('api/', api_overview, name='api-overview'),
    path('api/projects/', ProjectList.as_view(), name='project-list'),
    path('api/projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
]
