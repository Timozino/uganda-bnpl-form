from django.shortcuts import render, redirect

from rest_framework import viewsets
from .models import BillingModel, PaygoConfig, SalesAgent, OutrightConfig, BioData
from .serializers import BillingModelSerializer, PaygoConfigSerializer, SalesAgentSerializer, OutrightConfigSerializer
from rest_framework.permissions import IsAuthenticated


from .models import LoanCalculation
from decimal import Decimal




def confirmSubmission(requests):
    return render(requests, "billingSuccess.html")



class BillingModelViewSet(viewsets.ModelViewSet):
    queryset = BillingModel.objects.all()
    serializer_class = BillingModelSerializer
    permission_classes = [IsAuthenticated]  


class PaygoConfigViewSet(viewsets.ModelViewSet):
    queryset = PaygoConfig.objects.all()
    serializer_class = PaygoConfigSerializer
    permission_classes = [IsAuthenticated]  


class SalesAgentViewSet(viewsets.ModelViewSet):
    queryset = SalesAgent.objects.all()
    serializer_class = SalesAgentSerializer
    permission_classes = [IsAuthenticated]  


class OutrightConfigViewSet(viewsets.ModelViewSet):
    queryset = OutrightConfig.objects.all()
    serializer_class = OutrightConfigSerializer
    permission_classes = [IsAuthenticated]  









# def billing_model_form(request):
#     bio_data_list = BioData.objects.all()
#     if request.method == 'POST':
#         bio_data_id = request.POST.get('bio_data')
#         billing_model = request.POST.get('billing_model')

#         # Create the BillingModel instance and assign the appropriate fields
#         billing_instance = BillingModel(
#             billing_model=billing_model,
#             client=request.user.bio_data  # Assuming the user has BioData linked
#         )

#         if billing_model == 'Paygo':
#             billing_instance.paygo_config_id = request.POST.get('paygo_config')
#             billing_instance.paygo_freezer_price = request.POST.get('paygo_freezer_price')
#             billing_instance.repayment_plan = request.POST.get('repayment_plan')
#             billing_instance.down_payment = request.POST.get('down_payment')
#             billing_instance.monthly_instalment = request.POST.get('monthly_instalment')
        
#         elif billing_model == 'Outright':
#             billing_instance.sales_agent_id = request.POST.get('sales_agent')
#             billing_instance.outright_config_id = request.POST.get('outright_config')
#             billing_instance.outright_freezer_price = request.POST.get('outright_freezer_price')

#         billing_instance.save()
#         return redirect('success_page')  # Redirect to a success page after saving

#     paygo_configs = PaygoConfig.objects.all()
#     outright_configs = OutrightConfig.objects.all()
#     sales_agents = SalesAgent.objects.all()
    



#     return render(request, 'billingModelForm.html', {
#         'paygo_configs': paygo_configs,
#         'outright_configs': outright_configs,
#         'sales_agents': sales_agents
#     })


# def billing_model_form(request):
#     bio_data_list = BioData.objects.all()  # Retrieve all BioData instances
#     if request.method == 'POST':
#         bio_data_id = request.POST.get('bio_data')  # Fetch selected bio_data
#         billing_model = request.POST.get('billing_model')

#         # Find the selected BioData instance using the bio_data_id
#         bio_data_instance = BioData.objects.get(id=bio_data_id)

#         # Create the BillingModel instance and assign the appropriate fields
#         billing_instance = BillingModel(
#             billing_model=billing_model,
#             client=bio_data_instance  # Link the selected BioData to the billing
#         )

#         if billing_model == 'Paygo':
#             billing_instance.paygo_config_id = request.POST.get('paygo_config')
#             billing_instance.paygo_freezer_price = request.POST.get('paygo_freezer_price')
#             billing_instance.repayment_plan = request.POST.get('repayment_plan')
#             billing_instance.down_payment = request.POST.get('down_payment')
#             billing_instance.monthly_instalment = request.POST.get('monthly_instalment')

#         elif billing_model == 'Outright':
#             billing_instance.sales_agent_id = request.POST.get('sales_agent')
#             billing_instance.outright_config_id = request.POST.get('outright_config')
#             billing_instance.outright_freezer_price = request.POST.get('outright_freezer_price')

#         billing_instance.save()
#         return redirect('mySuccess_page')  # Redirect to a success page after saving

#     paygo_configs = PaygoConfig.objects.all()
#     outright_configs = OutrightConfig.objects.all()
#     sales_agents = SalesAgent.objects.all()

#     # Pass the bio_data_list to the template
#     return render(request, 'billingModelForm.html', {
#         'bio_data_list': bio_data_list,
#         'paygo_configs': paygo_configs,
#         'outright_configs': outright_configs,
#         'sales_agents': sales_agents
#     })




def calculate_loan_values(paygo_freezer_price, down_payment_percentage, management_fee_percentage, recurrent_percentage, repayment_plan):
    # Down Payment Calculation
    down_payment_value = (paygo_freezer_price * down_payment_percentage / 100) + (paygo_freezer_price * management_fee_percentage / 100)

    # Subtract down payment value from freezer price
    remaining_price = paygo_freezer_price - (paygo_freezer_price * down_payment_percentage / 100)

    # Map repayment plan choices to numeric values
    repayment_plan_mapping = {
        '2_months': 2,
        '5_months': 5,
        '11_months': 11,
        '17_months': 17,
    }
    repayment_plan_value = repayment_plan_mapping.get(repayment_plan, 1)

    # Calculate the recurrent cost over the repayment plan
    recurrent_cost = remaining_price * (recurrent_percentage / 100) * repayment_plan_value

    # Add recurrent cost to remaining price and divide by repayment plan to get monthly installment
    monthly_instalment_value = (remaining_price + recurrent_cost) / repayment_plan_value

    return down_payment_value, monthly_instalment_value



# # Updated view to incorporate LoanCalculation model
# def billing_model_form(request):
#     bio_data_list = BioData.objects.all()  # Retrieve all BioData instances

#     if request.method == 'POST':
#         bio_data_id = request.POST.get('bio_data')  # Fetch selected bio_data
#         billing_model = request.POST.get('billing_model')

#         # Find the selected BioData instance using the bio_data_id
#         bio_data_instance = BioData.objects.get(id=bio_data_id)

#         # Create the BillingModel instance and assign the appropriate fields
#         billing_instance = BillingModel(
#             billing_model=billing_model,
#             client=bio_data_instance  # Link the selected BioData to the billing
#         )

#         if billing_model == 'Paygo':
#             # Fetch the relevant loan calculation settings
#             loan_calculation = LoanCalculation.objects.get(id=request.POST.get('loan_calculation_id'))

#             paygo_freezer_price = Decimal(request.POST.get('paygo_freezer_price'))
#             repayment_plan = request.POST.get('repayment_plan')

#             # Use LoanCalculation instance to calculate values
#             down_payment_value, monthly_instalment_value = calculate_loan_values(
#                 paygo_freezer_price,
#                 loan_calculation.down_payment_percentage,
#                 loan_calculation.management_fee_percentage,
#                 loan_calculation.recurrent_percentage,
#                 repayment_plan
#             )

#             # Set the calculated values in the BillingModel instance
#             billing_instance.paygo_config_id = request.POST.get('paygo_config')
#             billing_instance.paygo_freezer_price = paygo_freezer_price
#             billing_instance.repayment_plan = repayment_plan
#             billing_instance.down_payment = down_payment_value
#             billing_instance.monthly_instalment = monthly_instalment_value

#         elif billing_model == 'Outright':
#             billing_instance.sales_agent_id = request.POST.get('sales_agent')
#             billing_instance.outright_config_id = request.POST.get('outright_config')
#             billing_instance.outright_freezer_price = request.POST.get('outright_freezer_price')

#         billing_instance.save()
#         return redirect('mySuccess_page')  # Redirect to a success page after saving

#     paygo_configs = PaygoConfig.objects.all()
#     outright_configs = OutrightConfig.objects.all()
#     sales_agents = SalesAgent.objects.all()

#     # Pass the bio_data_list and other required data to the template
#     return render(request, 'billingModelForm.html', {
#         'bio_data_list': bio_data_list,
#         'paygo_configs': paygo_configs,
#         'outright_configs': outright_configs,
#         'sales_agents': sales_agents,
#         'loan_calculations': LoanCalculation.objects.all()  # Fetch all loan calculations for selection
#     })







# def billing_model_form(request):
#     bio_data_list = BioData.objects.all()
#     paygo_configs = PaygoConfig.objects.all()
#     outright_configs = OutrightConfig.objects.all()
#     sales_agents = SalesAgent.objects.all()

#     paygo_freezer_price = 0
#     down_payment = 0
#     monthly_instalment = 0
#     repayment_plan = None
#     billing_model = None
#     paygo_config_id = None

#     if request.method == 'POST':
#         bio_data_id = request.POST.get('bio_data')
#         billing_model = request.POST.get('billing_model')

#         # Find the selected BioData instance
#         bio_data_instance = BioData.objects.get(id=bio_data_id)

#         # Create the BillingModel instance
#         billing_instance = BillingModel(billing_model=billing_model, client=bio_data_instance)

#         if billing_model == 'Paygo':
#             paygo_config_id = request.POST.get('paygo_config')
#             paygo_config = PaygoConfig.objects.get(id=paygo_config_id)

#             # Set the freezer price from the selected configuration
#             paygo_freezer_price = paygo_config.freezer_price

#             repayment_plan = request.POST.get('repayment_plan')

#             # Fetch the loan calculation settings
#             loan_calculation = LoanCalculation.objects.first()  # Replace with the appropriate query

#             # Calculate loan values
#             down_payment, monthly_instalment = calculate_loan_values(
#                 paygo_freezer_price,
#                 loan_calculation.down_payment_percentage,
#                 loan_calculation.management_fee_percentage,
#                 loan_calculation.recurrent_percentage,
#                 repayment_plan
#             )

#             # Save the billing instance
#             billing_instance.paygo_config_id = paygo_config_id
#             billing_instance.paygo_freezer_price = paygo_freezer_price
#             billing_instance.repayment_plan = repayment_plan
#             billing_instance.down_payment = down_payment
#             billing_instance.monthly_instalment = monthly_instalment
#             billing_instance.save()
#             return redirect('mySuccess_page')

#         elif billing_model == 'Outright':
#             sales_agent_id = request.POST.get('sales_agent')
#             outright_config_id = request.POST.get('outright_config')
#             outright_freezer_price = request.POST.get('outright_freezer_price')

#             billing_instance.sales_agent_id = sales_agent_id
#             billing_instance.outright_config_id = outright_config_id
#             billing_instance.outright_freezer_price = outright_freezer_price
#             billing_instance.save()
#             return redirect('mySuccess_page')

#     return render(request, 'billingModelForm.html', {
#         'bio_data_list': bio_data_list,
#         'paygo_configs': paygo_configs,
#         'outright_configs': outright_configs,
#         'sales_agents': sales_agents,
#         'paygo_freezer_price': paygo_freezer_price,
#         'down_payment': down_payment,
#         'monthly_instalment': monthly_instalment,
#         'billing_model': billing_model,
#         'paygo_config_id': paygo_config_id,
#         'repayment_plan': repayment_plan,
#     })









# def billing_model_form(request):
#     bio_data_list = BioData.objects.all()
#     paygo_configs = PaygoConfig.objects.all()
#     outright_configs = OutrightConfig.objects.all()
#     sales_agents = SalesAgent.objects.all()

#     paygo_freezer_price = 0
#     down_payment = 0
#     monthly_instalment = 0
#     repayment_plan = None
#     billing_model = None
#     paygo_config_id = None

#     # Fetch the loan calculation settings
#     loan_calculation = LoanCalculation.objects.first()  # Replace with the appropriate query
#     down_payment_percentage = loan_calculation.down_payment_percentage
#     management_fee_percentage = loan_calculation.management_fee_percentage
#     recurrent_percentage = loan_calculation.recurrent_percentage

#     if request.method == 'POST':
#         bio_data_id = request.POST.get('bio_data')
#         billing_model = request.POST.get('billing_model')

#         # Find the selected BioData instance
#         bio_data_instance = BioData.objects.get(id=bio_data_id)

#         # Create the BillingModel instance
#         billing_instance = BillingModel(billing_model=billing_model, client=bio_data_instance)

#         if billing_model == 'Paygo':
#             paygo_config_id = request.POST.get('paygo_config')
#             paygo_config = PaygoConfig.objects.get(id=paygo_config_id)
           

#             # Set the freezer price from the selected configuration
#             paygo_freezer_price = paygo_config.freezer_price

#             repayment_plan = request.POST.get('repayment_plan')

#             # Calculate loan values
#             down_payment, monthly_instalment = calculate_loan_values(
#                 paygo_freezer_price,
#                 down_payment_percentage,
#                 management_fee_percentage,
#                 recurrent_percentage,
#                 repayment_plan
#             )

#             # Save the billing instance
#             billing_instance.paygo_config_id = paygo_config_id
#             billing_instance.paygo_freezer_price = paygo_freezer_price
#             billing_instance.repayment_plan = repayment_plan
#             billing_instance.down_payment = down_payment
#             billing_instance.monthly_instalment = monthly_instalment
#             billing_instance.save()
#             return redirect('mySuccess_page')

#         elif billing_model == 'Outright':
#             sales_agent_id = request.POST.get('sales_agent')
#             outright_config_id = request.POST.get('outright_config')
#             outright_freezer_price = request.POST.get('outright_freezer_price')

#             billing_instance.sales_agent_id = sales_agent_id
#             billing_instance.outright_config_id = outright_config_id
#             billing_instance.outright_freezer_price = outright_freezer_price
#             billing_instance.save()
#             return redirect('mySuccess_page')

#     return render(request, 'billingModelForm.html', {
#         'bio_data_list': bio_data_list,
#         'paygo_configs': paygo_configs,
#         'outright_configs': outright_configs,
#         'sales_agents': sales_agents,
#         'paygo_freezer_price': paygo_freezer_price,
#         'down_payment': down_payment,
#         'monthly_instalment': monthly_instalment,
#         'billing_model': billing_model,
#         'paygo_config_id': paygo_config_id,
#         'repayment_plan': repayment_plan,
#         'down_payment_percentage': down_payment_percentage,
#         'management_fee_percentage': management_fee_percentage,
#         'recurrent_percentage': recurrent_percentage,
#     })











def billing_model_form(request):
    bio_data_list = BioData.objects.all()
    paygo_configs = PaygoConfig.objects.all()
    outright_configs = OutrightConfig.objects.all()
    sales_agents = SalesAgent.objects.all()

    paygo_freezer_price = 0
    down_payment = 0
    monthly_instalment = 0
    repayment_plan = None
    billing_model = None
    paygo_config_id = None

    # Fetch the loan calculation settings
    loan_calculation = LoanCalculation.objects.first()  # Replace with the appropriate query
    down_payment_percentage = loan_calculation.down_payment_percentage
    management_fee_percentage = loan_calculation.management_fee_percentage
    recurrent_percentage = loan_calculation.recurrent_percentage

    if request.method == 'POST':
        bio_data_id = request.POST.get('bio_data')
        billing_model = request.POST.get('billing_model')

        # Find the selected BioData instance
        bio_data_instance = BioData.objects.get(id=bio_data_id)

        # Create the BillingModel instance
        billing_instance = BillingModel(billing_model=billing_model, client=bio_data_instance)

        if billing_model == 'Paygo':
            paygo_config_info = request.POST.get('paygo_config')

            # Extracting the price using the selected string
            paygo_config = PaygoConfig.objects.get(configuration=paygo_config_info.split(' - ₦')[0])  # Get the config instance using its name
            paygo_freezer_price = paygo_config.price

            repayment_plan = request.POST.get('repayment_plan')

            # Calculate loan values
            down_payment, monthly_instalment = calculate_loan_values(
                paygo_freezer_price,
                down_payment_percentage,
                management_fee_percentage,
                recurrent_percentage,
                repayment_plan
            )

            # Save the billing instance
            billing_instance.paygo_config = paygo_config  # Assign the actual config instance
            billing_instance.paygo_freezer_price = paygo_freezer_price
            billing_instance.repayment_plan = repayment_plan
            billing_instance.down_payment = down_payment
            billing_instance.monthly_instalment = monthly_instalment
            billing_instance.save()
            return redirect('create_account')

        elif billing_model == 'Outright':
            sales_agent_id = request.POST.get('sales_agent')
            outright_config_id = request.POST.get('outright_config')
            outright_freezer_price = request.POST.get('outright_freezer_price')

            # Set billing instance fields for Outright model
            billing_instance.sales_agent_id = sales_agent_id
            billing_instance.outright_config_id = outright_config_id
            billing_instance.outright_freezer_price = outright_freezer_price
            billing_instance.save()
            return redirect('create_account')

    # Prepare the paygo_configs list for the template
    paygo_configs_list = [
        f"{config.configuration} - ₦{config.price}" for config in paygo_configs
    ]

    return render(request, 'billingModelForm.html', {
        'bio_data_list': bio_data_list,
        'paygo_configs': paygo_configs_list,  # Pass the formatted strings to the template
        'outright_configs': outright_configs,
        'sales_agents': sales_agents,
        'paygo_freezer_price': paygo_freezer_price,
        'down_payment': down_payment,
        'monthly_instalment': monthly_instalment,
        'billing_model': billing_model,
        'repayment_plan': repayment_plan,
        'down_payment_percentage': down_payment_percentage,
        'management_fee_percentage': management_fee_percentage,
        'recurrent_percentage': recurrent_percentage,
    })
