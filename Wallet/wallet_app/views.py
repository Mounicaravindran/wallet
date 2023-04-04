from django.shortcuts import render
from .models import wallet
#from rest_framework import viewsets
from .serializers import walletSerializer
from rest_framework.views import APIView  
from rest_framework.response import Response
import wallet_app.wallet_task as wallet_task

# Create your views here.
class create_wallet(APIView):
    def get(self, request, *args, **kwargs): 
        return wallet_task.get_wallets()
        #return Response({"status": "success"})
    def post(self, request):
        data = request.data
        wallet_task.create_wallet(data)
        return Response({"status": "success"})
    
class activate_wallet(APIView):
    def post(self,request):
        data =request.data
        return wallet_task.activate_wallet(data)

class add_money(APIView):
    def post(self,request):
        data=request.data
        return wallet_task.add_money(data)

class withdrawal(APIView):
    def post(self,request):
        data=request.data
        return wallet_task.withdrawal(data)

class transactions(APIView):
    def post(self,request):
        data=request.data
        return wallet_task.get_transactions(data)
        
    
        

    
    

        



'''class Wallet(APIView):
    queryset = wallet.objects.all()
    serializer_class = walletSerializer

    def create(self, request, *args, **kwargs):
        wallet = wallet.objects.create(user=request.user)
        serializer = walletSerializer(wallet)
        return Response(serializer.data)

    def activate(self, request, *args, **kwargs):
        wallet = self.get_object()
        wallet.is_active = True
        wallet.save()
        serializer = walletSerializer(wallet)
        return Response(serializer.data)

    def add_money(self, request, *args, **kwargs):
        wallet = self.get_object()
        amount = float(request.data['amount'])
        wallet.balance += amount
        wallet.save()
        serializer = walletSerializer(wallet)
        return Response(serializer.data)

    def withdraw_money(self, request, *args, **kwargs):
        wallet = self.get_object()
        amount = float(request.data['amount'])
        if amount > wallet.balance:
            return Response({'detail': 'Insufficient balance.'}, status=400)
        wallet.balance -= amount
        wallet.save()
        serializer = walletSerializer(wallet)
        return Response(serializer.data)'''
