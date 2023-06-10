from django.contrib import admin
from django.urls import path
from endvr_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout, name="logout"),
    path("team", views.team, name="team"),
    path("class_9", views.class_9, name="class_9"),
    path("class_10", views.class_10, name="class_10"),
    path("class_11", views.class_11, name="class_11"),
    path("class_12", views.class_12, name="class_12"),
    path("bsc", views.bsc, name="bsc"),
    path("btech", views.btech, name="btech"),
    path("skill", views.skill, name="skill"),
    path("terms_and_conditions", views.terms_and_conditions, name="terms_and_conditions"),
    path("hall_of_fame", views.hall_of_fame, name="hall_of_fame"),
    path("course_details", views.course_details, name="course_details"),
    path("Physics", views.Physics, name="Physics"),
]
