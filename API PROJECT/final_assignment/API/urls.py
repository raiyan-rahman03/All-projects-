from django.urls import path ,include
from .views import *







urlpatterns = [
    path('menu-items/<int:pk>/', menu_items_view),
    path('menu-items/', menu_items_view),
    path('group/<str:name>/',group_org),
    path('group/<str:name>/<int:id>/',delete_grp_user),
    path('cart',CartView.as_view()),
    path('cart_add',CartAddView.as_view()),
   
    path('cart_del/' ,cart_del.as_view()),
    path('order' , oder_view.as_view()),
    path('order_add' , oder_view_post.as_view()),
    path('oderitem' , user_order.as_view()),

    path('orders/<int:pk>',manager_order_up_and_dev.as_view()),


]
    
    
    

