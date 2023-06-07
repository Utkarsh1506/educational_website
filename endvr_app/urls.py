from django.contrib import admin
from django.urls import path
from endvr_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index.html", views.index, name="index"),
    path("about.html", views.about, name="about"),
    path("contact.html", views.contact, name="contact"),
    path("login.html", views.login, name="login"),
    path("signup.html", views.signup, name="signup"),
    path("logout.html", views.logout, name="logout"),
    path("team.html", views.team, name="team"),
    path("class_9th.html", views.class_9th, name="class_9th"),
    path("class_10th.html", views.class_10th, name="class_10th"),
    path("class_11th.html", views.class_11th, name="class_11th"),
    path("class_12th.html", views.class_12th, name="class_12th"),
    path("bsc.html", views.bsc, name="bsc"),
    path("btech.html", views.btech, name="btech"),
    path("skill.html", views.skill, name="skill"),
    path("terms_and_conditions.html", views.terms_and_conditions, name="terms_and_conditions"),
    path("hall_of_fame.html", views.hall_of_fame, name="hall_of_fame"),
]
