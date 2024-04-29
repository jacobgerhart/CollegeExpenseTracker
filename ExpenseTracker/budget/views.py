from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Semester, Income, Expense

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        user_pk = request.user.pk
        semesters = Semester.objects.filter(student_id = user_pk)
        context = {
           'semester_list': semesters
        }
        return render(request, 'budget/home.html', context=context)
    
    return render(request, 'budget/home.html', {})

def semester(request, pk):
    if not(request.user.is_authenticated):
        return redirect('home')
    else:
        user_pk = request.user.pk
        semesters = Semester.objects.filter(student_id = user_pk)
        incomes = Income.objects.filter(semester_id=pk)
        expenses = Expense.objects.filter(semester_id=pk)
        starting_balance = semesters[0].starting_balance


        current_balance = semesters[0].starting_balance
        end_balance = 1000.00

        context = {
           'semester_list': semesters,
           'incomes': incomes,
            'expenses': expenses,
            'start_bal': starting_balance,
            'current_bal': current_balance,
            'end_bal': end_balance
        }
        return render(request, 'budget/semester_view.html', context=context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, 'Username and password do not match, try again.')
            return redirect('home')
    else:
        return render(request, 'budget/home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')