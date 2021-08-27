from django.urls import path
from .views import *

urlpatterns = [

    # Seller Section URLS
    path('addbook/',addBook,name='ADDBOOK'),
    path('showbooks/',showBooks,name='SHOWBOOKS'),
    path('updatebook/<int:pk>/',updateBooks,name='UPDATEBOOK'),
    path('deletebook/<int:pk>/',deleteBook,name='DELETEBOOK'),
    path('soldbook/',soldbook,name='SOLDBOOK'),

    # Customer Section URLS
    path('signup/',signup,name='SIGNUP'),
    path('signin/',signin,name='SIGNIN'),
    path('signout/',signout,name='SIGNOUT'),
    path('',customerBookView,name='CUSTOMERBOOKVIEW'),
    path('search/<int:id>',searchBook,name='SEARCHBOOK'),
    path('purchase/<int:pk>',purchaseBook,name='PURCHASEBOOK'),
    path('showpurchase/',purchasedbook,name='SHOWPURCHASED')
]