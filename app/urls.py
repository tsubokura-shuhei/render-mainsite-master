from django.urls import path
from app import views
from .views import IndexView, AboutView,WorkView,BusinessView,Business_serviceView,Business_newsView,Business_magazineView,ProfileView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('design/', AboutView.as_view(), name="design"),
    path('work/', WorkView.as_view(), name="work"),
    path('business/', BusinessView.as_view(), name="business"),
    path('business_service/', Business_serviceView.as_view(), name="business_service"),
    path('business_news/', Business_newsView.as_view(), name="business_news"),
    path('business_magazine/', Business_magazineView.as_view(), name="business_magazine"),
    path('profile/', ProfileView.as_view(), name="profile"),
    # path('main/', views.main, name="main"),
    path('work_page1', views.work_page1, name="work_page1"),
    path('work_page2', views.work_page2, name="work_page2"),
    path('work_page3', views.work_page3, name="work_page3"),
    path('work_page4', views.work_page4, name="work_page4"),
    path('work_page5', views.work_page5, name="work_page5"),
    path('work_page6', views.work_page6, name="work_page6"),
    path('work_page7', views.work_page7, name="work_page7"),
    path('work_page8', views.work_page8, name="work_page8"),
]