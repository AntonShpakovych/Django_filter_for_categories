from django.contrib import admin
from main.models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_news', 'news_img',
                    'full_text', 'category')
    list_display_links = ('id', 'title_news')
    search_fields = ('title_news', 'full_text')
    list_filter = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_category')
    list_display_links = ('id', 'title_category')
    search_fields = ('title_category', )


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
