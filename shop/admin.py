from django.contrib import admin
from .models import Category, Product, Post


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock',
                     'available']  # select attribute can be edited using edited from admin list display
    prepopulated_fields = {'slug': ('name',)}  # set slug value autmatically from name


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','status','created')
    list_filter = ('status','created','publish','author')
    search_fields = ('title','author')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Post, PostAdmin)

