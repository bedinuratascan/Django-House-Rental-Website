from django.contrib import admin

# Register your models here.
from house.models import Category, House, Images

class HouseImageInline(admin.TabularInline):
    model = Images
    extra = 6

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'status']
    list_filter = ['status']
    readonly_fields = ('image_tag',)


class HouseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'rent', 'image_tag', 'status']
    list_filter = ['status', 'category']
    inlines = [HouseImageInline]
    readonly_fields = ('image_tag',)

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'house', 'image_tag']
    readonly_fields = ('image_tag',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Images, ImagesAdmin)