from django.shortcuts import render, redirect

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import AccountDetail
from .serializers import AccountDetailSerializer

from .models import AccountDetail, BANK_CHOICES
from django.contrib import messages
from Bio_Data.models import BioData

class AccountDetailViewSet(viewsets.ModelViewSet):
    queryset = AccountDetail.objects.all()
    serializer_class = AccountDetailSerializer
    permission_classes = [IsAuthenticated]  
    
    
    


def accountDetailSuccess(request):
    return render(request, 'accountDetailsSuccess.html')


# def create_account_detail(request):
#     if request.method == 'POST':
#         # Collect data from the form (POST data)
#         smart_phone = request.POST.get('smart_phone')
#         product = request.POST.get('product')
#         outstanding_loan = request.POST.get('outstanding_loan')
#         monthly_income = request.POST.get('monthly_income')
#         bank_name = request.POST.get('bank_name')
#         bank_account_name = request.POST.get('bank_account_name')
#         bvn = request.POST.get('bvn')

#         # Validation can be done here if necessary
#         if not bvn or len(bvn) != 11:
#             messages.error(request, 'You must enter BVN with 11 digits.')
#             return render(request, 'account_detail_form.html')  # Replace with your actual template

#         # Save the form data to the database
#         account_detail = AccountDetail.objects.create(
#             client=request.user.biodata,  # Assuming `BioData` has a OneToOne relation with `User`
#             smart_phone=smart_phone,
#             product=product,
#             outstanding_loan=outstanding_loan,
#             monthly_income=monthly_income,
#             bank_name=bank_name,
#             bank_account_name=bank_account_name,
#             bvn=bvn,
#         )

#         # Redirect to a success page or back to the form with a success message
#         messages.success(request, 'Account details saved successfully!')
#         return redirect('account_success')  # Replace with your success page URL

#     return render(request, 'account_detail_form.html')  # Replace with your actual template



def create_account_detail(request):
    if request.method == 'POST':
        # Collect data from the form (POST data)
        client_id = request.POST.get('client')
        smart_phone = request.POST.get('smart_phone')
        product = request.POST.get('product')
        outstanding_loan = request.POST.get('outstanding_loan')
        monthly_income = request.POST.get('monthly_income')
        bank_name = request.POST.get('bank_name')
        bank_account_name = request.POST.get('bank_account_name')
        bvn = request.POST.get('bvn')
        other_bank_name = request.POST.get('other_bank_name')

        # Validation (e.g., BVN length)
        if not bvn or len(bvn) != 11:
            messages.error(request, 'You must enter BVN with 11 digits.')
            return render(request, 'account_detail_form.html', {
                'bank_choices': AccountDetail.BANK_CHOICES,
                'clients': BioData.objects.all()
            })

        # Fetch the selected client
        client = BioData.objects.get(id=client_id)

        # Handle "Other" bank case
        if bank_name == 'others':
            if not other_bank_name:
                messages.error(request, 'Please specify the other bank name.')
                return render(request, 'account_detail_form.html', {
                    'bank_choices': AccountDetail.BANK_CHOICES,
                    'clients': BioData.objects.all()
                })
        
        # Save the form data to the database
        account_detail = AccountDetail.objects.create(
            client=client,
            smart_phone=smart_phone,
            product=product,
            outstanding_loan=outstanding_loan,
            monthly_income=monthly_income,
            bank_name=bank_name,
            bank_account_name=bank_account_name,
            bvn=bvn,
            other_bank_name=other_bank_name if bank_name == 'others' else None
        )

        # Redirect to a success page or back to the form with a success message
        messages.success(request, 'Account details saved successfully!')
        return redirect('info')  
    bank_choices = AccountDetail._meta.get_field('bank_name').choices
    # Pass bank choices and client options to the template
    return render(request, 'account_detail_form.html', {
        # 'bank_choices': AccountDetail.BANK_CHOICES,
        'bank_choices': bank_choices,
        'clients': BioData.objects.all()
    })
