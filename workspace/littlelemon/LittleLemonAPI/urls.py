from django.urls import path
from .views import MenuItemView, SingleMenuItemView

urlpatterns = [
    path('menu-items/', MenuItemView.as_view()),
    path('menu-item/<int:pk>', SingleMenuItemView.as_view()),
]