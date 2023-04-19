from django.shortcuts import render
from .models import Item, Order
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.

from users.models import User

import json

def homev(request):
    return render(request, 'Home.html')

@login_required
def mainv(request):
    return render(request, 'mainpage.html')

@login_required
def orderv(request):
    if request.method=='POST':
        totalcost=request.POST['orderTotal']
        orderDetails=request.POST['orderedItems']
        try:
            order_id=request.POST['order_id']
            order=Order.objects.get(id=order_id)
            if 'submit' in request.POST:
                # ordered_user=User.objects.get(username=str(request.user))
                t_id=request.POST['transaction_id']
                address_v=request.POST['address']
                order.status='Payment verification pending'
                order.transaction_id=t_id
                order.address=address_v
                order.save()

                return HttpResponseRedirect(reverse_lazy('Mainpage'))
            elif 'cancel' in request.POST:
                order.delete()
                return HttpResponseRedirect(reverse_lazy('Order'))
        except:
           pass

        ordered_user=User.objects.get(username=str(request.user))
        order=Order.objects.create(user=ordered_user, order_details=orderDetails, status= 'Payment transaction-id not submitted', cost=float(totalcost))   
        order_id =  order.id
        order.save()

        orderDetails=json.loads(orderDetails)
        
        for orderItem in orderDetails:
            item_name=orderItem['name']
            item=Item.objects.get(name=item_name)
            item.availability-= int(orderItem['quantity'])
            item.save()

        orderDetails=json.dumps(orderDetails)
        return render(request,'PaymentPage.html', {'orderedItems':orderDetails, 'orderTotal':totalcost, 'order_id':order_id})
    
    items=list(Item.objects.all())

    items_lst=[]
    items_sublist=[]
    for item in items:
        if len(items_sublist)==4:
            items_lst.append(items_sublist)
            items_sublist=[item,]
        else:
            items_sublist.append(item)
            if item== items[-1]:
                items_lst.append(items_sublist)
    items= items_lst
    
    return render(request, 'menu.html', {'items':items})

@login_required
def paymentv(request):
    return render(request,'PaymentPage.html')

@login_required
def items_availv(request):
    items=list(Item.objects.all())
    if request.method=='POST':
        for item in items:
            avail= request.POST[str(item.id)]
            item.availability=int(avail)
            item.save()
    

    items_lst=[]
    items_sublist=[]
    for item in items:
        if len(items_sublist)==4:
            items_lst.append(items_sublist)
            items_sublist=[item,]
        else:
            items_sublist.append(item)
            if item== items[-1]:
                items_lst.append(items_sublist)

    items= items_lst
    return render(request, 'interface.html', {'items': items})

@login_required
def payment_approvalv(request):
    if request.method=='POST':
        order_id=request.POST['order_id']
        order=Order.objects.get(id=order_id)
        order.status='Payment verification done'
        order.save()

    orders=Order.objects.filter(status='Payment verification pending')
    return render(request, 'canteen_approval.html',{'orders':orders})

@login_required
def myordersv(request):
    orders=Order.objects.filter(user=request.user)
    ordersdict={}
    for order in orders:
        orderdetails=json.loads(order.order_details)
        items_str=''
        for item in orderdetails:
              items_str+=item['name']+'--'+str(item['quantity'])+ ', '
        ordersdict[order]=(items_str[:-2])
    ordersdict=dict(reversed(list(ordersdict.items())))
    return render(request, 'orders.html',{'orders':orders, 'ordersdict':ordersdict})

@login_required
def orders_canteenv(request):
    if request.method == 'POST':
        order_id=request.POST['order_id']
        order=Order.objects.get(id=order_id)
        order.status='Delivered'
        order.save()
    orders=Order.objects.filter(status='Payment verification done')
    ordersdict={}
    for order in orders:
        orderdetails=json.loads(order.order_details)
        items_str=''
        for item in orderdetails:
              items_str+=item['name']+'--'+str(item['quantity'])+ ', '
        ordersdict[order]=(items_str[:-2])
    ordersdict=dict(reversed(list(ordersdict.items())))
    return render(request, 'Orders_Canteen.html',{'ordersdict': ordersdict})
