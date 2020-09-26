from django.contrib import admin
from listings.models import listing


class listingAdmin(admin.ModelAdmin):
    class Meta:
        model = listing

    list_display = ['id', 'realtor', 'title', 'address', 'price', 'is_published']
    list_display_links = ['id', 'realtor', 'title', ]
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('id', 'realtor', 'title', 'address', 'price',)
    list_per_page = 2


# Register your models here.
admin.site.register(listing,listingAdmin)
