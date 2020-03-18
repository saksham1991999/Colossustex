from django.urls import path, include
from . import views
app_name = 'employee'


urlpatterns = [
    path('', views.HomeView, name='home'),
    path('profile/', views.ProfileView, name='profile'),

    path('employees/', views.EmployeesView, name='employees'),
    path('employees/add/', views.EmployeeAddView, name='add_employee'),
    path('employees/edit/<int:id>/', views.EmployeeEditView, name='edit_employee'),
    path('employees/delete/<int:id>/', views.EmployeeDeleteView, name='delete_employee'),

    path('suppliers/', views.SuppliersView, name='suppliers'),
    path('suppliers/add/', views.SuppliersAddView, name='add_supplier'),
    path('suppliers/edit/<int:id>/', views.SupplierEditView, name='edit_supplier'),
    path('suppliers/delete/<int:id>/', views.SupplierDeleteView, name='delete_supplier'),

    path('sub_agents/', views.SubAgentView, name='sub_agents'),
    path('sub_agents/add/', views.SubAgentAddView, name='add_sub_agent'),
    path('sub_agents/edit/<int:id>/', views.SubAgentEditView, name='edit_sub_agent'),
    path('sub_agents/delete/<int:id>/', views.SubAgentEditView, name='delete_sub_agent'),

    path('buyers/', views.BuyersView, name='buyers'),
    path('buyers/add/', views.BuyersAddView, name='add_buyer'),
    path('buyers/edit/<int:id>/', views.BuyersEditView, name='edit_buyer'),
    path('buyers/delete/<int:id>/', views.BuyerDeleteView, name='delete_buyer'),

    path('products/', views.ProductsView, name='products'),
    path('products/add/', views.ProductAddView, name='add_product'),
    path('products/edit/<int:id>/', views.ProductEditView, name='edit_product'),
    path('products/delete/<int:id>/', views.ProductDeleteView, name='delete_product'),

    path('enquiries/', views.EnquiriesView, name='enquiries'),
    path('enquiries/add/', views.EnquiryAddView, name='add_enquiry'),
    path('enquiries/edit/', views.EnquiryEditView, name='edit_enquiry'),
    path('enquiries/delete/<int:id>/', views.EnquiryDeleteView, name='delete_enquiry'),

    path('bills/', views.BillsView, name='bills'),
    path('bills/add/', views.BillAddView, name='add_bill'),
    path('bills/edit/<int:id>/', views.BillEditView, name='edit_bill'),
    path('bills/delete/<int:id>/', views.BillDeleteView, name='delete_bill'),

    path('payments/', views.PaymentsView, name='payments'),
    path('payments/add/', views.PaymentAddView, name='add_payment'),
    path('payments/edit/<int:id>/', views.PaymentEditView, name='edit_payment'),
    path('payments/delete/<int:id>/', views.PaymentDeleteView, name='delete_payment'),

    path('shipments/', views.ShipmentsView, name='shipments'),
    path('shipments/add/', views.ShipmentAddView, name='add_shipment'),
    path('shipments/edit/<int:id>/', views.ShipmentEditView, name='edit_shipment'),
    path('shipments/delete/<int:id>/', views.ShipmentDeleteView, name='delete_shipment'),

    path('inspections/', views.ShipmentsView, name='inspections'),
    path('inspections/add/', views.ShipmentAddView, name='add_inspection'),
    path('inspections/edit/<int:id>/', views.ShipmentEditView, name='edit_inspection'),
    path('inspections/delete/<int:id>/', views.ShipmentDeleteView, name='delete_inspection'),

    path('visit-notes/', views.InspectionsView, name='visit-notes'),
    path('visit-notes/add/', views.InspectionsAddView, name='add_visit-note'),
    path('visit-notes/edit/<int:id>/', views.InspectionsEditView, name='edit_visit-note'),
    path('visit-notes/delete/<int:id>/', views.InspectionsDeleteView, name='delete_visit-note'),

    path('suplus-products/', views.SuplusProductsView, name='suplus-products'),
    path('suplus-products/add/', views.SuplusProductsAddView, name='add_suplus-product'),
    path('suplus-products/edit/<int:id>/', views.SuplusProductsEditView, name='edit_suplus-product'),
    path('suplus-products/delete/<int:id>/', views.SuplusProductsDeleteView, name='delete_suplus-product'),

    path('updates-news/', views.UpdatesView, name='updates-news'),
    path('updates-news/add/', views.UpdatesAddView, name='add_updates-news'),
    path('updates-news/edit/<int:id>/', views.UpdatesEditView, name='edit_updates-news'),
    path('updates-news/delete/<int:id>/', views.UpdatesDeleteView, name='delete_updates-news'),

    path('leave-applications/', views.UpdatesView, name='leave_applications'),
    path('submit-leave-applications/add/', views.UpdatesAddView, name='add_leave_application'),
]
