from pprint import pprint

from django.shortcuts import render
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpResponse
from django.contrib.auth.admin import User
from .serializers import *
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


# class Boz(GenericAPIView):
#     permission_classes = [IsAuthenticated,]
#
#     def get(self, request):
#
#         return HttpResponse(str(request.user))

class SignUpView(CreateAPIView):
    serializer_class = UserSerializer
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):
        try:
            User.objects.create_user(username=request.data.get('username', None),
                                     password=request.data.get('password', None))
            return HttpResponse({"status": 200})

        except:
            return HttpResponse({"status": 400})


class BudgetCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BudgetSerializer
    allowed_methods = ['POST']

    # def perform_create(self, serializer):
    #     serializer.save(data=self.request.data)

    def post(self, request, *args, **kwargs):
        try:
            Budget.objects.create(user=request.user,
                                  name=request.data.get('name', None),
                                  counter=request.data.get('counter', None))
            return Response({'status': 200})

        except:
            return Response({"status": 400})


class BudgetListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BudgetSerializer
    queryset = Budget.objects.filter()


class CategoryCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):
        try:
            Category.objects.create(user=request.user,
                                    name=request.data.get('name'))
            return Response({"status": 200})
        except:

            return Response({"status": 400})


class CategoryListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ExpenseCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExpenseSerializer
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):

        def maker(s):
            if s == 'true' or s == True:
                return True
            elif s == 'false' or s == False:
                return False
            else:
                return None

        tmp = Expense(
            user=request.user,
            amount=int(request.data.get('amount')),
            category=Category.objects.get(pk=request.data.get('category')),
            description=request.data.get('description', None),
            budget=Budget.objects.get(pk=request.data.get('budget')),
            income=maker(request.data.get('income', False))
        )
        tmp.save()

        if tmp.income:
            tmp.budget.counter += tmp.amount
            tmp.budget.save()
        else:
            bgt = Budget.objects.get(pk=tmp.budget.pk)
            # print(type(tmp.amount))
            bgt.counter = (bgt.counter - tmp.amount)
            bgt.save()

        return Response({"status": 200})
        # except:
        #     return Response({"status": 400})


class ExpenseListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()


class CategorySpentListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']

        try:
            cr = Category.objects.get(pk=pk)
            return Expense.objects.filter(category=cr)
        except:
            return None


class BudgetSpentListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']

        try:
            cr = Budget.objects.get(pk=pk)
            return Expense.objects.filter(budget=cr)
        except:
            return None


class TokenValidate(GenericAPIView):
    allowed_methods = ['POST', ]
    print(Token.objects.all())

    def post(self, request, *args, **kwargs):
        # print(request.data.get("token"))

        for i in Token.objects.all():
            if i.pk == request.data.get("token"):
                return Response({'status': 200})
        return Response({'status': 400})
