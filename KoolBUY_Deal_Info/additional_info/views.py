from django.shortcuts import render, redirect
from django.contrib import messages
from Bio_Data.models import BioData
from koolAssembly_billing_model.models import SalesAgent

from rest_framework import viewsets
from .models import OtherDetails
from .serializers import OtherDetailsSerializer
from rest_framework.permissions import IsAuthenticated

class OtherDetailsViewSet(viewsets.ModelViewSet):
    queryset = OtherDetails.objects.all()
    serializer_class = OtherDetailsSerializer
    permission_classes = [IsAuthenticated]  # Ensure only logged-in users can access this


def other_info(request):
    return render(request, 'other_details_success.html')



def create_other_details(request):
    if request.method == 'POST':
        # Collecting the form data
        client_id = request.POST.get('client')
        sales_agent_id = request.POST.get('sales_agent')
        guarantor_fullname = request.POST.get('guarantor_fullname')
        guarantor_phone_number = request.POST.get('guarantor_phone')  # Updated
        guarantor_nin = request.POST.get('guarantor_nin')
        guarantor_nin_image = request.FILES.get('guarantor_nin_image')
        reason_for_purchase = request.POST.get('reason_for_purchase')
        referee_fullname = request.POST.get('referee_fullname')
        referee_phone_number = request.POST.get('referee_phone')  # Updated
        second_referee_fullname = request.POST.get('second_referee_fullname')
        second_referee_phone_number = request.POST.get('second_referee_phone')  # Updated
        product_photo = request.FILES.get('product_photo')
        client_photo = request.FILES.get('client_photo')
        client_nin_image = request.FILES.get('client_nin_image')
        bank_statements_image = request.FILES.get('bank_statements')  # Updated
        home_utility_bill_image = request.FILES.get('home_utility_bill')  # Updated
        business_utility_bill_image = request.FILES.get('business_utility_bill')  # Updated

        # Getting the related instances from ForeignKey fields
        try:
            client = BioData.objects.get(id=client_id)
            sales_agent = SalesAgent.objects.get(id=sales_agent_id)
        except (BioData.DoesNotExist, SalesAgent.DoesNotExist):
            messages.error(request, "Client or Sales Agent not found.")
            return redirect('create_other_details')  # Replace with your actual form URL

        # Save the form data to the database
        OtherDetails.objects.create(
            client=client,
            sales_agent=sales_agent,
            guarantor_fullname=guarantor_fullname,
            guarantor_phone_number=guarantor_phone_number,  # Updated
            guarantor_nin=guarantor_nin,
            guarantor_nin_image=guarantor_nin_image,
            reason_for_purchase=reason_for_purchase,
            referee_fullname=referee_fullname,
            referee_phone_number=referee_phone_number,  # Updated
            second_referee_fullname=second_referee_fullname,
            second_referee_phone_number=second_referee_phone_number,  # Updated
            product_photo=product_photo,
            client_photo=client_photo,
            client_nin_image=client_nin_image,
            bank_statements_image=bank_statements_image,  # Updated
            home_utility_bill_image=home_utility_bill_image,  # Updated
            business_utility_bill_image=business_utility_bill_image,  # Updated
        )

        # Redirect after successful form submission
        messages.success(request, "Other details submitted successfully!")
        return redirect('other_success')

    # If GET request, render the form
    clients = BioData.objects.all()
    agents = SalesAgent.objects.all()

    return render(request, 'other_details_form.html', {'clients': clients, 'agents': agents})
