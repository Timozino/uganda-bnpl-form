from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BillingModelViewSet, PaygoConfigViewSet, SalesAgentViewSet, OutrightConfigViewSet
from .views import billing_model_form
from .views import confirmSubmission 


router = DefaultRouter()
router.register(r'billing-models', BillingModelViewSet)
router.register(r'paygo-configs', PaygoConfigViewSet)
router.register(r'sales-agents', SalesAgentViewSet)
router.register(r'outright-configs', OutrightConfigViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('billing-model-form/', billing_model_form, name='billing_model'),
    
    #path('success/', lambda request: HttpResponse('Form submitted successfully!'), name='success_page')
    path('success/', confirmSubmission, name='mySuccess_page')
]
