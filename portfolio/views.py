from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer


def home(request):
    projects = [
        {"title": "Gastromi Job Board", "description": "A Django-based job board for gastronomy professionals.",
         "image": "/static/portfolio/images/jobboard.png", "link": "#"},
        {"title": "Weather App", "description": "A real-time weather forecast web app using Python APIs.",
         "image": "/static/portfolio/images/weatherapp.png", "link": "#"},
        {"title": "Portfolio Website", "description": "This very site showcasing my work and skills.",
         "image": "/static/portfolio/images/portfolio.png", "link": "#"},
    ]
    return render(request, "portfolio/home.html", {"projects": projects})


@api_view(['GET'])
def project_list(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True, context={"request": request})
    return Response(serializer.data)


@api_view(['GET'])
def api_overview(request):
    return Response({"message": "Welcome to Dlivingstone Portfolio API!"})


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_serializer_context(self):
        return {"request": self.request}


class ProjectDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_serializer_context(self):
        return {"request": self.request}
