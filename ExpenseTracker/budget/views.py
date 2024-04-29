from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Semester, Income, Expense

def home(request):
    return render(request, 'budget/home.html', {})

def login_user(request):
    return render(request, 'budget/login.html', {})

def logout_user(request):
    return redirect('home')

class CreateIncome(CreateView):
    model = Income
    fields = ['semester', 'amount', 'is_recurring', 'recurring_period', 'memo']
    template_name = 'budget/income_form.html'
    success_url = reverse_lazy('home')

class UpdateIncome(UpdateView):
    model = Income
    fields = ['amount', 'is_recurring', 'recurring_period', 'memo']
    template_name = 'budget/income_form.html'
    success_url = reverse_lazy('home')

class DeleteIncome(DeleteView):
    model = Income
    template_name = 'budget/income_confirm_delete.html'
    success_url = reverse_lazy('home')

class CreateExpense(CreateView):
    model = Expense
    fields = ['semester', 'amount', 'is_recurring', 'recurring_period', 'memo']
    template_name = 'budget/expense_form.html'
    success_url = reverse_lazy('home')

class UpdateExpense(UpdateView):
    model = Expense
    fields = ['amount', 'is_recurring', 'recurring_period', 'memo']
    template_name = 'budget/expense_form.html'
    success_url = reverse_lazy('home')

class DeleteExpense(DeleteView):
    model = Expense
    template_name = 'budget/expense_confirm_delete.html'
    success_url = reverse_lazy('home')

class CreateSemester(CreateView):
    model = Semester
    fields = ['student', 'semester_name', 'start_date', 'end_date', 'starting_balance', 'semester_tuition', 'current_balance']
    template_name = 'budget/semester_form.html'
    success_url = reverse_lazy('home')

class DeleteSemester(DeleteView):
    model = Semester
    template_name = 'budget/semester_confirm_delete.html'
    success_url = reverse_lazy('home')
