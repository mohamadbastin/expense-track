from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['pk', 'user', 'name', 'counter']

    # def create(self, validated_data):
    #     # validated_data.pop('data')
    #     # ct = validated_data.pop('context')
    #     new_tr = BudgetSerializer(**validated_data)
    #     # new_tr.profile = ct['profile']
    #     new_tr.save()
    #     return new_tr


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'user', 'name', ]


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['pk', 'user', 'amount', 'category', 'description', 'budget', 'income', 'date']
