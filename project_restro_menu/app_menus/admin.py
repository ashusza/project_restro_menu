from django.contrib import admin
from app_menus.models import Category,Menu
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_title","category_code"]

class MenuAdmin(admin.ModelAdmin):
    list_display=("menu_title","menu_category", "menu_ingridient","menu_created_at")
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu,MenuAdmin)

#cutomizing admin panel title and headings
admin.site.site_title="Admin Panel" #page subtitle
admin.site.site_header="RESTRO" #page header
admin.site.index_title="RESTRO" #page title