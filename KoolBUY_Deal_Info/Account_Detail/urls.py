from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountDetailViewSet
from . import views

router = DefaultRouter()
router.register(r'account-details', AccountDetailViewSet, basename='accountdetail')

urlpatterns = [
    path('', include(router.urls)),
    path('create-account/', views.create_account_detail, name='create_account'), 
    path('successPage/', views.accountDetailSuccess, name='account_success'),
]

