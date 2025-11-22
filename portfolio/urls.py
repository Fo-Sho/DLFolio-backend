from django.urls import path
from .views import api_overview, ProjectList, ProjectDetail

urlpatterns = [
    path('', api_overview, name='api-overview'),
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
]

