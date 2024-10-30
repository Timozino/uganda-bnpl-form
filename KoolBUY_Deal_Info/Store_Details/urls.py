from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Store_Details.views import StoreDetailViewSet
from .views import store_detail_view
from . import views

router = DefaultRouter()
router.register(r'store-details', StoreDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('store-detail/', store_detail_view, name='store_detail'),
    path('storeDetail-submit/', views.storeDetailSubmit, name='store_detail_submit')
]
