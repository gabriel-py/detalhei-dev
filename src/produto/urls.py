from django.urls import path
from . import views

urlpatterns = [
    path('<int:category_id>/', views.sync),
    path('ranking/<int:area_id>/', views.ranking),
    path('detailed_ranking/<int:area_id>/', views.detailed_ranking),
]
