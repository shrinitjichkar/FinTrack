import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import Transaction, Goal
from .forms import TransactionForm, GoalForm
from decimal import Decimal

@login_required
def dashboard_view(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')[:5]
    
    income_agg = Transaction.objects.filter(user=request.user, transaction_type='Income').aggregate(Sum('amount'))
    if income_agg['amount__sum'] is not None:
        total_income = income_agg['amount__sum']
    else:
        total_income = Decimal('0.00')
        
    expense_agg = Transaction.objects.filter(user=request.user, transaction_type='Expense').aggregate(Sum('amount'))
    if expense_agg['amount__sum'] is not None:
        total_expense = expense_agg['amount__sum']
    else:
        total_expense = Decimal('0.00')
        
    net_savings = total_income - total_expense

    goals = Goal.objects.filter(user=request.user)
    
    for goal in goals:
        if goal.target_amount > 0:
            percentage = (goal.current_amount / goal.target_amount) * 100
            goal.progress = round(percentage, 1)
        else:
            goal.progress = 0
    
    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'net_savings': net_savings,
        'goals': goals
    }
    return render(request, 'finance/dashboard.html', context)

@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'finance/transaction_list.html', {'transactions': transactions})

@login_required
def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            messages.success(request, "Transaction added successfully!")
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    
    return render(request, 'finance/transaction_form.html', {'form': form, 'title': 'Add New Transaction'})

@login_required
def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            messages.success(request, "Transaction updated successfully!")
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
        
    return render(request, 'finance/transaction_form.html', {'form': form, 'title': 'Edit Transaction'})

@login_required
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    
    if request.method == "POST":
        transaction.delete()
        messages.success(request, "Transaction deleted successfully!")
        return redirect('transaction_list')
        
    return render(request, 'finance/transaction_confirm_delete.html', {'transaction': transaction})

@login_required
def add_goal(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            messages.success(request, "Goal added successfully!")
            return redirect('dashboard')
    else:
        form = GoalForm()
        
    return render(request, 'finance/goal_form.html', {'form': form})

@login_required
def report_view(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'finance/report.html', {'transactions': transactions})

@login_required
def export_transactions_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transactions_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'Title', 'Category', 'Transaction Type', 'Amount', 'Description'])

    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    for t in transactions:
        writer.writerow([t.date, t.title, t.category, t.transaction_type, t.amount, t.description])

    return response

@login_required
def complete_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)
    goal.is_completed = True
    goal.save()
    messages.success(request, f'Goal "{goal.title}" marked as completed!')
    return redirect('dashboard')

@login_required
def delete_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)
    goal.delete()
    messages.success(request, f'Goal "{goal.title}" has been deleted.')
    return redirect('dashboard')
