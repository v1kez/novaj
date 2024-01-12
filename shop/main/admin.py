from django.contrib import admin
from .models import Product, News, Feed, History

admin.site.register(Product)
admin.site.register(News)
admin.site.register(Feed)
admin.site.register(History)