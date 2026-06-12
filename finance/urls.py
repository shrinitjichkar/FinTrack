from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='root'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('transaction/add/', views.add_transaction, name='add_transaction'),
    path('transaction/edit/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),
    path('transaction/delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('goal/add/', views.add_goal, name='add_goal'),
    path('goal/complete/<int:goal_id>/', views.complete_goal, name='complete_goal'),
    path('goal/delete/<int:goal_id>/', views.delete_goal, name='delete_goal'),
    path('report/', views.report_view, name='report'),
    path('export/', views.export_transactions_csv, name='export_csv'),
]
