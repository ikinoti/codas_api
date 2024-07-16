from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from . import views


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('', views.endpoints),
    path('advocates/', views.advocate_list),
    path('advocates/<str:username>', views.advocate_detail),

    # companies/
    path('companies/', views.companies_list)
]