from django.contrib import admin

from .models import (
    SeoData,
    Article,
    SiteHomePage,
    SiteAboutPage,
    GalleryImage,
    Document,
    SiteServicesPage,
    House,
    Section,
    Flat,
    Tariff,
    User,
    Service,
    ServicePrice,
    Message,
    Account,
    MeterData,
    Receipt,
)

admin.site.register(Account)
admin.site.register(SeoData)
admin.site.register(Article)
admin.site.register(SiteHomePage)
admin.site.register(SiteAboutPage)
admin.site.register(SiteServicesPage)
admin.site.register(Document)
admin.site.register(GalleryImage)
admin.site.register(House)
admin.site.register(Flat)
admin.site.register(Section)
admin.site.register(Tariff)
admin.site.register(User)
admin.site.register(Service)
admin.site.register(ServicePrice)
admin.site.register(Message)
admin.site.register(MeterData)
admin.site.register(Receipt)
