from django.urls import path

from . import views

urlpatterns = [
    path('', views.TeamListView.as_view(), name='list'),
    path('<pk>', views.TeamDetailView.as_view(), name='detail'),
    path('create/', views.TeamCreateView.as_view(), name='create'),
    path('edit/<pk>/', views.TeamUpdateView.as_view(), name='update'),
    path('delete/<pk>/', views.TeamDeleteView.as_view(), name='delete'),
]
