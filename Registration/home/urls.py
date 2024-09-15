from django.urls import path
from . import views

urlpatterns=[
    path('',views.loginPage,name='login'),
    path('signup/',views.signupPage,name='signup'),
    path('home/',views.homePage,name='home'),
    path('adminlogin/',views.adminLoginPage,name='adminlogin'),
    path('adminpanel/',views.adminPanel,name='adminpanel'),
    path('add/',views.addPage,name='add'),
    path('edit/',views.editPage,name='edit'),
    path('update/<str:id>',views.updatePage,name='update'),
    path('delete/<str:id>',views.deletePage,name='delete'),
    path('search/',views.searchPage,name='search'),
    path('logout/',views.logout_view,name='logout'),
]