from django.shortcuts import render
from django.views.generic import DetailView

from src.admin_panel.models import SiteHomePage, SiteAboutPage
from src.admin_panel.services.site_pages_services import (
    get_or_create_page_object,
)


def home_view(request):
    return render(request, "site/pages/home.html")


class HomeView(DetailView):
    template_name = "site/pages/home.html"

    def get_object(self, queryset=None):
        obj = get_or_create_page_object(SiteHomePage)
        return obj


class AboutView(DetailView):
    template_name = "site/pages/about.html"

    def get_object(self, queryset=None):
        obj = get_or_create_page_object(SiteAboutPage)
        return obj


def services_view(request):
    return render(request, "site/pages/services.html")


def contacts_view(request):
    return render(request, "site/pages/contacts.html")
