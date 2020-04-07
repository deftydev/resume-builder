from django.urls import path, include
from . import views

urlpatterns = [
      path('create', views.ProductCreateView.as_view() ,name='create'),
      path('update/<int:pk>', views.ProductUpdateView.as_view() ,name='update'),
      path('delete/<int:pk>', views.ProductDeleteView.as_view() ,name='delete'),
      path('<int:product_id>', views.detail ,name='detail'),
      path('<int:product_id>/upvote', views.upvote ,name='upvote'),


]
