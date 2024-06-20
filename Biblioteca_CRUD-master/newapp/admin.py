from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'pages', 'publisher', 'published_date')  # Atualize os campos aqui
