from django.contrib import admin

from apps.news.models import News


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    model = News
    readonly_fields = ('created_at', )
    list_display = ('id', 'title', 'created_at')
