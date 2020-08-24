from django.urls import include, path
from . import views

urlpatterns = [
  path('welcome', views.welcome),
  
  path('getchild/<int:child_id>', views.get_child),
  path('addchild', views.add_child),
  path('updatechild/<int:child_id>', views.update_child),
  path('deletechild/<int:child_id>', views.delete_child),
  
  path('getparent/<int:parent_id>', views.get_parent),
  path('addparent', views.add_parent),
  path('updateparent/<int:parent_id>', views.update_parent),
  path('deleteparent/<int:parent_id>', views.delete_parent)
]