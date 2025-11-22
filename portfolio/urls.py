from django.urls import path
from .views import api_overview, ProjectList, ProjectDetail

urlpatterns = [
    path('api/', api_overview, name='api-overview'),
    path('api/projects/', ProjectList.as_view(), name='project-list'),
    path('api/projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
]


