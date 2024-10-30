from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .models import StoreDetail, BioData 

from rest_framework import viewsets
#from rest_framework.response import Response
from .models import StoreDetail
from .serializers import StoreDetailSerializer
from rest_framework.permissions import IsAuthenticated
from .models import StoreDetail



def storeDetailSubmit(requests):
    
    return render(requests, 'storeDetailSuccess.html')


class StoreDetailViewSet(viewsets.ModelViewSet):
    queryset = StoreDetail.objects.all()
    serializer_class = StoreDetailSerializer









class StoreDetailViewSet(viewsets.ModelViewSet):
    queryset = StoreDetail.objects.all()
    serializer_class = StoreDetailSerializer
    permission_classes = [IsAuthenticated]  








from django.shortcuts import render, redirect
from .models import StoreDetail, BioData  # Import BioData model
from rest_framework.permissions import IsAuthenticated

def store_detail_view(request):
    bio_data_list = BioData.objects.all()  # Get all BioData instances

    if request.method == 'POST':
        # Collect form data from POST request
        bio_data_id = request.POST.get('bio_data')  # Get selected bio_data id
        sales_agent_name = request.POST.get('sales_agent')
        product_usage = request.POST.get('product_usage')
        store_name = request.POST.get('store_name')
        product_brand = request.POST.get('brand')
        freezer_size = request.POST.get('freezer_size')
        reference_kb_number = request.POST.get('reference_kb')
        category = request.POST.get('category')
        selling_for = request.POST.get('selling_for')

        # Validate if required fields are filled
        if not (bio_data_id and sales_agent_name and product_usage and store_name and product_brand and freezer_size and reference_kb_number and category and selling_for):
            error_message = "All fields are required. Please fill out the form completely."
            return render(request, 'store_detail_form.html', {'error': error_message, 'bio_data_list': bio_data_list})

        # Get the BioData instance
        bio_data = BioData.objects.get(id=bio_data_id)

        # Save the collected data into the database
        StoreDetail.objects.create(
            bio_data=bio_data,  # Include the bio_data instance
            sales_agent_name=sales_agent_name,
            product_usage=product_usage,
            store_name=store_name,
            product_brand=product_brand,
            freezer_size=freezer_size,
            reference_kb_number=reference_kb_number,
            category=category,
            selling_for=selling_for
        )

        # Redirect to a success page or show a success message
        return redirect('billing_model')  # Replace 'success_page' with your actual URL name for success

    return render(request, 'store_detail_form.html', {'bio_data_list': bio_data_list})  # Pass bio_data_list to the template



    # # Optionally, customize the create/update methods if needed
    # def create(self, request, *args, **kwargs):
    #     # You can add additional logic before saving the data
    #     return super().create(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #     # Add logic for updates if necessary
    #     return super().update(request, *args, **kwargs)

