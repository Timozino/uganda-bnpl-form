from django.contrib import admin
from django.urls import path, include
from Bio_Data import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Bio_Data.urls')),  
    path('api/', include('Store_Details.urls')),
    path('api/', include('koolAssembly_billing_model.urls')),
    path('api/', include('Account_Detail.urls')),
    path('api/', include('additional_info.urls')),
    path('', views.index, name='index')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




admin.site.site_title = 'KoolBUY Administration'
admin.site.site_header = 'KoolBUY Form UGANDA'
admin.site.index_title = 'KoolBUY Form UGANDA'