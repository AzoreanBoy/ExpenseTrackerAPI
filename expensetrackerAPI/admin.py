from django.contrib import admin

# Models
from .models import *

# Customizing admin titles
admin.site.site_header = "Expense Tracker Admin"
admin.site.site_title = "Expense Tracker Admin Portal"
admin.site.index_title = "Welcome to the Expense Tracker Admin Portal"


# Registering models


# Registering Category with custom admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "type")
    search_fields = ("name", "type")
    list_filter = ("type",)
    ordering = ("name",)


# Registering SubCategory
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "category_type_display")
    search_fields = ("name", "category__name", )
    list_filter = ("category",)
    ordering = ("name", "category__name", )

    def category_type_display(self, obj):
        return obj.category.get_type_display()
    
    category_type_display.short_description = "Category Type"
