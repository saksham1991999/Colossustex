from django.urls import path, include
from . import views
app_name = 'employee'


urlpatterns = [
    path('', views.HomeView, name='home'),
    path('profile/', views.ProfileView, name='profile'),

    path('suppliers/', views.SuppliersView, name='suppliers'),
    path('suppliers/delete/<int:id>/', views.SupplierDeleteView, name='supplier_delete'),

    path('sub_agents/', views.SubAgentView, name='sub_agents'),
    path('sub_agents/delete/<int:id>/', views.SupplierDeleteView, name='sub_agent_delete'),

    path('buyers/', views.BuyersView, name='buyers'),
    path('buyers/delete/<int:id>/', views.BuyerDeleteView, name='buyer_delete'),
]
