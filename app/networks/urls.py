from django.urls import path

from . import views

urlpatterns = [
    path("", views.RackListView.as_view(), name="rack-list"),
    path("create/", views.PortCreateView.as_view(), name="port-create"),
    path("rack/<int:pk>/", views.RackDetailView.as_view(), name="rack-detail"),
    path("switch/<int:pk>/", views.SwitchDetail.as_view(), name="switch-detail"),
    path("port/detail/<int:pk>/", views.PortDetail.as_view(), name="port-detail"),
    path("port/update/<int:pk>/", views.PortUpdateView.as_view(), name="port-update"),
]
