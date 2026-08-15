from django.contrib import admin
from django.urls import path

from tools.views import (
    home,
    image_tools,
    video_tools,
    tool_detail,
    about,
    privacy,
    terms,
    disclaimer,
    contact,
)


urlpatterns = [

    # =========================
    # ADMIN
    # =========================

    path(
        "admin/",
        admin.site.urls
    ),


    # =========================
    # HOME
    # =========================

    path(
        "",
        home,
        name="home"
    ),


    # =========================
    # AI IMAGE TOOLS
    # =========================

    path(
        "ai-image-tools/",
        image_tools,
        name="image_tools"
    ),


    # =========================
    # AI VIDEO TOOLS
    # =========================

    path(
        "ai-video-tools/",
        video_tools,
        name="video_tools"
    ),


    # =========================
    # TOOL DETAIL PAGE
    # =========================

    path(
        "tool/<slug:slug>/",
        tool_detail,
        name="tool_detail"
    ),


    # =========================
    # FOOTER PAGES
    # =========================

    path(
        "about/",
        about,
        name="about"
    ),

    path(
        "privacy/",
        privacy,
        name="privacy"
    ),

    path(
        "terms/",
        terms,
        name="terms"
    ),

    path(
        "disclaimer/",
        disclaimer,
        name="disclaimer"
    ),

    path(
        "contact/",
        contact,
        name="contact"
    ),

]