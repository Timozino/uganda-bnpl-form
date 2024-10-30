from django.shortcuts import render, redirect # type: ignore
from rest_framework import viewsets # type: ignore
from .models import BioData
from .serializers import BioDataSerializer
from rest_framework.permissions import IsAuthenticated # type: ignore
from django.db import IntegrityError # type: ignore


def index(requests):
    return render(requests, 'index.html')

def formsSuccessFulSubmit(requests):
    
    return render(requests, 'successPage.html')

class BioDataViewSet(viewsets.ModelViewSet):
    queryset = BioData.objects.all()
    serializer_class = BioDataSerializer





class BioDataViewSet(viewsets.ModelViewSet):
    queryset = BioData.objects.all()
    serializer_class = BioDataSerializer
    permission_classes = [IsAuthenticated]  
    
    
    
    

def bio_data_view(request):
    if request.method == 'POST':
        # Collect form data
        data = request.POST

        # Check for uniqueness
        if BioData.objects.filter(email=data['email']).exists():
            return render(request, 'bio_data_form.html', {'error': 'Email already exists.'})
        if BioData.objects.filter(NIN=data['nin']).exists():
            return render(request, 'bio_data_form.html', {'error': 'NIN already exists.'})

        # Try saving the data to the database
        try:
            bio_data = BioData.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                gender=data['gender'],
                date_of_birth=data['date_of_birth'],
                phone_number=data['phone_number'],
                alternate_phone_number=data['alternate_phone_number'],
                email=data['email'],
                street_name=data['street_name'],
                address_line_2=data['address_line_2'],
                city=data['city'],
                state=data['state'],
                postal_code=data['postal_code'],
                country='Uganda',  # Defaulted to Uganda
                marital_status=data['marital_status'],
                product_usage=data['product_usage'],
                business_name=data.get('business_name', None),
                business_type=data.get('business_type', None),
                business_size=data.get('business_size', None),
                business_address=data.get('business_address', None),
                number_of_dependents=data['number_of_dependents'],
                NIN=data['nin'],
                occupation=data['occupation'],
                lead_source=data['lead_source']
            )
            bio_data.save()
            return redirect('store_detail')  # Redirect to a success page after saving
        except IntegrityError:
            return render(request, 'bio_data_form.html', {'error': 'Failed to save data due to uniqueness constraint.'})

    return render(request, 'bio_data_form.html')
