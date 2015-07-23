from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Borrower, Business, Loan

import const

@login_required
def index(request):
    return render(request, 'loan/index.html')

@login_required
def apply_loan(request):
    if request.method == 'POST':
        data = request.POST
        user = User.objects.get(id=request.user.id)
        borrower = Borrower(user=user, name=user.username,
                            email=user.email, phone=data['phone'])
        borrower.save()
        business_sector = const.BUSINESS_SECTOR[data['business_sector']]
        business = Business(owner=borrower, company_name=data['company'],
                            address=data['address'], registered_number=data['reg_num'],
                            business_sector=business_sector)
        business.save()
        loan = Loan(business=business, amount=data['amount'],
                    days=data['days'], reason=data['reason'])
        loan.save()
        return HttpResponseRedirect('/apply_complete')
    else:
        return render(request, 'loan/apply_loan.html')

@login_required
def apply_complete(request):
    return render(request, 'loan/apply_complete.html')

@login_required
def display_loan(request):
    user = User.objects.get(id=request.user.id)
    loan_list = Loan.objects.filter(business__owner__user__id=user.id)
    context = {'loan_list': loan_list}
    return render(request, 'loan/display_loan.html', context)
