from django.urls import path
# from . import views

# urlpatterns = [
#     path('fetch-ga-data/', views.fetch_and_save_ga_data, name='fetch_ga_data'),
# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DashboardViewSet, ReferenceBookViewSet, KeywordViewSet, ImamViewSet, CatalogueViewSet, IndexViewSet

router = DefaultRouter()
router.register('dashboards', DashboardViewSet)
router.register('reference-books', ReferenceBookViewSet)
router.register('keywords', KeywordViewSet)
router.register('imams', ImamViewSet)
router.register('catalogues', CatalogueViewSet)
router.register('indices', IndexViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include the router-generated URLs
]
