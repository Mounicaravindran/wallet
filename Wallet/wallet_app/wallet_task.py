from http.client import ResponseNotReady
from urllib import response
from .models import wallet
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.response import Response

def create_wallet(data):
    # To create wallet and push data to DB
    print(data)
    wallet_obj = wallet()
    wallet_obj.id = data["id"]
    wallet_obj.name = data["name"]
    print("---------")
    wallet_obj.save()
    print("Test")

def get_wallets():
    # Returns the list of wallets
    objects = wallet.objects.all()
    wallet_details=[]
    for i in objects:
        temp={}
        temp["id"]=i.id
        temp["name"]=i.name
        temp["balance"]=i.balance
        temp["activated"]=i.activated
        wallet_details.append(temp)
    return Response(wallet_details)


def validate_gmail(value):
    if "@gmail.com" not in value:
        raise ValidationError("This email must be from Gmail domain only.")
    
def validate_phone_no(value):
    if not value.isdigit():
        raise ValidationError("Phone number can only contain digits")
    if len(value) != 10:
        raise ValidationError("Phone number must be 10 digits long")
    

def create_customer(request):
    # get the user object
    user = User.objects.get(username='myuser')
    # create a new customer object and link it to the user object
    customer = customer.objects.create(user=user, name='Mouni', email='mouni@gmail.com', phone_no='1234567890')
    # render a success message
    return render(request, 'customer_created.html', {'customer': customer})

def activate_wallet(data):
    id= data["id"]
    try:
        wallet_object = wallet.objects.get(id=id)
    except Exception:
        return Response({"status": "Failed"})

    wallet_object.activated = True
    wallet_object.save()
    return Response({"status": "Success"})

def add_money(data):
    amount=data["amount"]
    id=data["id"]
    try:
        wallet_object = wallet.objects.get(id=id)
    except Exception:
        return Response({"status": "Failed"})
    wallet_object.balance += amount
    wallet_object.transacations.append("added_money RS"+str(amount))

    wallet_object.save()
    return Response({"status": "Success"})

def withdrawal(data):
    amount=data["amount"]
    id=data["id"]
    try:
        wallet_object = wallet.objects.get(id=id)
    except Exception:
        return Response({"status": "Failed"})
    balance=wallet_object.balance
    if balance < amount:
        return Response({"status": "Insufficient balance"})
    else:
        wallet_object.balance -= amount
        wallet_object.transacations.append("withdraw RS"+str(amount))
        wallet_object.save()
        #saved
    return Response({"status": "Success"})

def get_transactions(data):
    id=data["id"]
    try:
        wallet_object = wallet.objects.get(id=id)
    except Exception:
        return Response({"status": "Failed"})
    transactions=wallet_object.transacations
    return Response({"list of transactions": transactions})


    

    

    

