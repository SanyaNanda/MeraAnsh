from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('baby_clothes/', views.Clothes.as_view(), name="baby_clothes"),
    path('yt/', views.Yt.as_view(), name="yt"),
    path('insurance/', views.Insurance.as_view(), name="insurance"),
    path('govt/',views.Govt.as_view(),name="govt"),
    path('vaccine',views.Vaccine.as_view(),name="vaccine"),
    path('babysitter',views.Babysitter.as_view(),name="babysitter"),
    path('health_nutrition',views.Health.as_view(),name="health_nutrition"),
    path('add_post/',views.AddPostView.as_view(),name="add_post"),
    path('my_feed/',views.Feed.as_view(),name="my_feed"),
    path('my_prescriptions/',views.Pres.as_view(),name="my_prescriptions"),
    path('add_pres/',views.AddPres.as_view(),name="add_pres"),


]