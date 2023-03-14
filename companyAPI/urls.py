from django.urls import path
from .views import *
from companyAPI import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
) 


urlpatterns = [
    path('v1/testCelery/',views.testCelery, name='testCelery'),
    path('v1/getCompany/',GetCompany.as_view(), name='getCompany'),
    path('v1/getCompanyById/<int:company_id>',GetCompanyById.as_view(), name='getCompanyById'),
    path('v1/postCompany/',PostCompany.as_view(), name='postCompany'),
    path('v1/updateCompany/<int:company_id>',PutCompany.as_view(), name='updateCompany'),
    path('v1/deleteCompany/<int:company_id>',DeleteCompany.as_view(), name='deleteCompany'),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# urlpatterns = [
#     path('v1/getCompany/',views.getCompany, name='getCompany'),
#     path('v1/getCompanyById/<int:company_id>',views.get, name='getCompanyById'),
#     path('v1/postCompany/',views.postCompany, name='postCompany'),
#     path('v1/updateCompany/<int:company_id>',views.updateCompany, name='updateCompany'),
#     path('v1/deleteCompany/<int:company_id>',views.deleteCompany, name='deleteCompany'),
#     path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]
