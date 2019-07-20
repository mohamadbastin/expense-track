from django.db import models
from django.contrib.auth.admin import User

# Create your models here
# .

make = {0: 'income', 1: 'outcome'}


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    # counter = models.IntegerField(default=0)
    # is_output = models.BooleanField(default=1)

    def __str__(self):
        return self.name


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    income = models.BooleanField(default=False)

    def __str__(self):
        return str(self.category) + ': ' + str(self.amount) + ' from ' + str(self.budget)

