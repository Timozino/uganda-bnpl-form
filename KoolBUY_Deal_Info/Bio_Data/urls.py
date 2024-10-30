from django.urls import path, include # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore
from .views import BioDataViewSet
from . import views



router = DefaultRouter()
router.register(r'biodata', BioDataViewSet)


urlpatterns = [
    path('', include(router.urls)), 
    path('bio-data/', views.bio_data_view, name='bio_data'), 
    path('successPage/', views.formsSuccessFulSubmit, name='success_page'),
]


