from django.urls import path
from . import views as cus_views
urlpatterns =[
    # path('',cus_views.customer_dashboard, name='dashboard'),
    # path('login/',cus_views.customer_login, name='login'),
    path('addcustomer/',cus_views.customer_signup, name='addcustomer'),
    # path('logout/',cus_views.customer_logout, name='logout'),
    path('customers/',cus_views.show_customer, name='all_customers'),
    path('update/<int:id>/',cus_views.update_customer, name='update_customer'),
    path('delete/<int:id>/',cus_views.delete_customer, name='delete_customer'),


    # path('exm/',cus_views.exampleonly,name='exm')

]
