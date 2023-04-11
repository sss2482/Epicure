from django.shortcuts import render
from .models import Item
# Create your views here.

import json

def mainv(request):
    return render(request, 'Main_page.html')

def orderv(request):
    if request.method=='POST':
        totalcost=request.POST['orderTotal']
        orderDetails=request.POST['orderedItems']
        orderDetails=json.loads(orderDetails)
        for orderItem in orderDetails:
            item_name=orderItem['name']
            item=Item.objects.get(name=item_name)
            item.availability-= int(orderItem['quantity'])
            item.save()
        
        return render(request,'PaymentPage.html', {'orderedItems':orderDetails, 'orderTotal':totalcost})
    
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

def paymentv(request):
    return render(request,'PaymentPage.html')

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