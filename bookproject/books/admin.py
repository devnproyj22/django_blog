from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BoodAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_date'] # 디스플레이 기능
    search_fields = ['title', 'author'] # 검색 기능
    list_filter = ['publication_date'] # 필터 기능

