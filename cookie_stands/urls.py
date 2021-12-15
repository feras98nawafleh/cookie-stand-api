from django.urls import path
from .views import cookie_standList, cookie_standDetail

urlpatterns = [
    path("", cookie_standList.as_view(), name="cookie_list"),
    path("<int:pk>/", cookie_standDetail.as_view(), name="cookie_detail"),
]
