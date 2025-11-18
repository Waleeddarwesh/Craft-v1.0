from django import forms
from django.contrib import admin, messages
from django.shortcuts import render
from django.utils.html import format_html

from .models import BalanceWithdrawRequest, ReturnRequest, Transaction
from .services import BalanceService

@admin.register(ReturnRequest)
class ReturnRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'reason', 'status', 'amount', 'created_at')
    list_filter = ('status', 'reason', 'created_at')
    search_fields = ('user__username', 'order__order_number', 'product__name', 'supplier__user__username')
    readonly_fields = ('id', 'image_thumbnail', 'created_at', 'updated_at', 'amount')
    autocomplete_fields = ['user', 'order', 'product', 'supplier']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Core Info', {
            'fields': ('user', 'order', 'product', 'supplier', 'quantity', 'status', 'reason', 'amount')
        }),
        ('User Evidence', {
            'fields': ('image', 'image_thumbnail')
        }),
    )

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<a href="{0}"><img src="{0}" style="max-width: 150px; max-height: 150px;" /></a>', obj.image.url)
        return "No Image"
    image_thumbnail.short_description = 'Image Thumbnail'

class RejectForm(forms.Form):
    """A form to collect admin notes for rejection."""
    admin_notes = forms.CharField(widget=forms.Textarea, required=True)

@admin.register(BalanceWithdrawRequest)
class BalanceWithdrawRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_user_balance', 'amount', 'transfer_type', 'transfer_number','risk_score')
    list_filter = ('transfer_status', 'transfer_type', 'created_at')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'transfer_number')
    readonly_fields = ('id', 'user', 'related_transaction', 'created_at', 'updated_at')
    autocomplete_fields = ['user']
    list_select_related = ['user']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Request Details', {
            'fields': ('user', 'amount', 'transfer_status', 'transfer_type', 'transfer_number', 'notes')
        }),
        ('Admin Section', {
            'fields': ('admin_notes',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        })
    )

    actions = ['approve_requests', 'reject_requests_with_notes']
    
    @admin.display(description="Available Balance")
    def get_user_balance(self, obj):
       available_balance = obj.user.Balance + obj.amount
       return f"EGP {available_balance:.2f}"

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.transfer_status != BalanceWithdrawRequest.TransferStatus.REQUESTED:
            return [field.name for field in self.model._meta.fields]
        return self.readonly_fields

    @admin.action(description="Approve selected withdrawal requests")
    def approve_requests(self, request, queryset):        
        pending_requests = queryset.filter(transfer_status=BalanceWithdrawRequest.TransferStatus.REQUESTED)
        for withdrawal_request in pending_requests:
            try:
                BalanceService.approve_withdrawal(withdrawal_request, request.user)
            except Exception as e:
                self.message_user(request, f"Error approving request {withdrawal_request.id}: {e}", messages.ERROR)
        
        if pending_requests.exists():
            self.message_user(request, "Selected pending requests have been approved.", messages.SUCCESS)

    @admin.action(description="Reject selected requests with notes")
    def reject_requests_with_notes(self, request, queryset):
        pending_requests = queryset.filter(transfer_status=BalanceWithdrawRequest.TransferStatus.REQUESTED)

        if 'apply' in request.POST:
            form = RejectForm(request.POST)
            if form.is_valid():
                admin_notes = form.cleaned_data['admin_notes']
                for req in pending_requests:
                    try:
                        BalanceService.reject_withdrawal(req, request.user, admin_notes)
                    except Exception as e:
                        self.message_user(request, f"Error rejecting request {req.id}: {e}", messages.ERROR)
                
                self.message_user(request, "Selected requests have been rejected.", messages.SUCCESS)
                return
        
        form = RejectForm()
        return render(request, 'admin/reject_intermediate.html', context={
            'requests': pending_requests, 
            'form': form
        })

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'transaction_type', 'amount', 'created_at', 'related_object')
    list_filter = ('transaction_type', 'created_at')
    search_fields = ('user__username',)
    readonly_fields = ('id', 'created_at')
    autocomplete_fields = ['user']
    date_hierarchy = 'created_at'