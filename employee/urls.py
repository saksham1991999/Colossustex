from django.urls import path, include
from . import views
app_name = 'employee'


urlpatterns = [
    path('', views.HomeView, name='home'),
    path('profile/', views.ProfileView, name='profile'),

    path('employees/', views.EmployeesView, name='employees'),
    path('employees/add/', views.EmployeeAddView, name='add_employee'),
    path('employees/edit/<int:id>/', views.EmployeeEditView, name='edit_employee'),
    path('employees/view/<int:id>/', views.EmployeeViewView, name='view_employee'),
    path('employees/delete/<int:id>/', views.EmployeeDeleteView, name='delete_employee'),

    path('suppliers/', views.SuppliersView, name='suppliers'),
    path('suppliers/add/', views.SuppliersAddView, name='add_supplier'),
    path('suppliers/edit/<int:id>/', views.SupplierEditView, name='edit_supplier'),
    path('suppliers/view/<int:id>/', views.SupplierViewView, name='view_supplier'),
    path('suppliers/delete/<int:id>/', views.SupplierDeleteView, name='delete_supplier'),

    path('sub_agents/', views.SubAgentView, name='sub_agents'),
    path('sub_agents/add/', views.SubAgentAddView, name='add_sub_agent'),
    path('sub_agents/edit/<int:id>/', views.SubAgentEditView, name='edit_sub_agent'),
    path('sub_agents/view/<int:id>/', views.SubAgentViewView, name='view_sub_agent'),
    path('sub_agents/delete/<int:id>/', views.SubAgentEditView, name='delete_sub_agent'),

    path('buyers/', views.BuyersView, name='buyers'),
    path('buyers/add/', views.BuyersAddView, name='add_buyer'),
    path('buyers/edit/<int:id>/', views.BuyersEditView, name='edit_buyer'),
    path('buyers/view/<int:id>/', views.BuyersViewView, name='edit_buyer'),
    path('buyers/delete/<int:id>/', views.BuyerDeleteView, name='delete_buyer'),

    path('products/', views.ProductsView, name='products'),
    path('products/add/', views.ProductAddView, name='add_product'),
    path('products/edit/<int:id>/', views.ProductEditView, name='edit_product'),
    path('products/delete/<int:id>/', views.ProductDeleteView, name='delete_product'),
    path('products/<int:id>/', views.ProductView, name='single_product'),


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

    path('inspections/', views.InspectionsView, name='inspections'),
    path('inspections/add/', views.InspectionsAddView, name='add_inspection'),
    path('inspections/edit/<int:id>/', views.InspectionsEditView, name='edit_inspection'),
    path('inspections/delete/<int:id>/', views.InspectionsDeleteView, name='delete_inspection'),

    path('sample-requests/', views.SampleRequestsView, name='sample-requests'),
    path('sample-requests/add/', views.ShipmentAddView, name='add_sample-request'),
    path('sample-requests/edit/<int:id>/', views.ShipmentEditView, name='edit_sample-request'),
    path('sample-requests/delete/<int:id>/', views.ShipmentDeleteView, name='delete_sample-request'),

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

    path('buyer-complaints/', views.BuyerComplaintsView, name='buyer_complaints'),
    path('buyer-complaints/add/', views.BuyerComplaintAddView, name='add_buyer_complaint'),
    path('buyer-complaints/<int:id>/', views.BuyerComplaintAddResponseView, name='single_buyer_complaint'),

    path('supplier-complaints/', views.SupplierComplaintsView, name='supplier_complaints'),
    path('supplier-complaints/add/', views.SupplierComplaintAddView, name='add_supplier_complaint'),
    path('supplier-complaints/<int:id>/', views.SupplierComplaintAddResponseView, name='single_supplier_complaint'),

    path('sub-agent-complaints/', views.SubAgentComplaintsView, name='sub_agent_complaints'),
    path('sub-agent-complaints/add/', views.SubAgentComplaintAddView, name='add_sub_agent_complaint'),
    path('sub-agent-complaints/<int:id>/', views.SubAgentComplaintAddResponseView, name='single_sub_agent_complaint'),

    path('buyer-feedbacks/', views.BuyerFeedbacksView, name='buyer_feedbacks'),
    path('buyer-feedbacks/add/', views.BuyerFedbackAddView, name='add_buyer_feedback'),
    path('buyer-feedbacks/<int:id>/', views.BuyerFeedbackView, name='single_buyer_feedback'),

    path('supplier-feedbacks/', views.SupplierFeedbacksView, name='supplier_feedbacks'),
    path('supplier-feedbacks/add/', views.SupplierFedbackAddView, name='add_supplier_feedback'),
    path('supplier-feedbacks/<int:id>/', views.SupplierFeedbackView, name='single_supplier_feedback'),

    path('sub-agent-feedbacks/', views.SubAgentFeedbacksView, name='sub_agent_feedbacks'),
    path('sub-agent-feedbacks/add/', views.SubAgentFedbackAddView, name='add_sub_agent_feedback'),
    path('sub-agent-feedbacks/<int:id>/', views.SubAgentFeedbackView, name='single_sub_agent_feedback'),

    path('enquiries/', views.EnquiriesView, name='enquiries'),
    path('enquiries/add/', views.EnquiryAddView, name='add_enquiry'),
    path('enquiries/edit/', views.EnquiryEditView, name='edit_enquiry'),
    path('enquiries/delete/<int:id>/', views.EnquiryDeleteView, name='delete_enquiry'),

    #INQUIRY VIEWS
    path('inquiries/', views.InquiresView, name='inquiries'),
    path('inquiries/add/', views.AddInquiryView, name='add_inquiry'),
    path('inquiry/<int:id>/', views.InquiryView, name='inquiry'),
    path('inquiry/<int:id>/add-product/', views.AddInquiryProductView, name='inquiry_add_product'),
    path('inquiry/<int:id>/edit-product/', views.EditInquiryProductView, name='inquiry_edit_product'),
    path('inquiry/delete-product/<int:id>/', views.DeleteInquiryProductView, name='inquiry_delete_product'),
    path('inquiry/select-suppliers/<int:id>/', views.InquiryNotifySuppliersView, name='inquiry_select_suppliers'),
    path('inquiry/add-quotation/<int:id>/', views.AddSupplierQuotationView, name='inquiry_add_quotation'),
    path('inquiry/select-quotations/<int:id>/', views.SelectForwardQuotationsView, name='inquiry_select_quotations'),
    path('inquiry/add-customer-feedback/<int:id>/', views.AddInquiryUpdateView, name='inquiry_add_customer_feedback'),
    path('inquiry/confirm/<int:id>/', views.ConfirmInquiryView, name='inquiry_confirm'),
    path('inquiry/close/<int:id>/', views.CloseInquiryView, name='inquiry_close'),

]
