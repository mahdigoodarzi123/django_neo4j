from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name="members"),
    path('all/', views.all_members, name="all"),
    # path('all/details/<int:id>', views.one_member, name="onemember"),
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("test/", views.test, name="test"),
    # path("success/", views.success, name = "success"),
]
