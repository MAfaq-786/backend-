from django.shortcuts import render
# from django.http import HttpResponse
# from .utils import get_ga_metrics
# from django.shortcuts import render
# from .models import AnalyticsFilter

# def analytics_view(request):
#     # Fetch all records from the AnalyticsFilter model
#     filters = AnalyticsFilter.objects.all()
#     return render(request, 'analytics.html', {'filters': filters})


from rest_framework import viewsets
from .models import Dashboard, ReferenceBook, Keyword, Imam, Catalogue, Index
from .serializers import DashboardSerializer, ReferenceBookSerializer, KeywordSerializer, ImamSerializer, CatalogueSerializer, IndexSerializer

class DashboardViewSet(viewsets.ModelViewSet):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer

class ReferenceBookViewSet(viewsets.ModelViewSet):
    queryset = ReferenceBook.objects.all()
    serializer_class = ReferenceBookSerializer

class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

class ImamViewSet(viewsets.ModelViewSet):
    queryset = Imam.objects.all()
    serializer_class = ImamSerializer

class CatalogueViewSet(viewsets.ModelViewSet):
    queryset = Catalogue.objects.all()
    serializer_class = CatalogueSerializer

class IndexViewSet(viewsets.ModelViewSet):
    queryset = Index.objects.all()
    serializer_class = IndexSerializer


