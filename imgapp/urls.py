from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.mainpage,name='mainpage'),
    path('addtable',views.addtable,name='addtable'),
    path('showpage',views.showpage,name='showpage'),
    path('editpage/<int:id>',views.editpage,name='editpage'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),

]
