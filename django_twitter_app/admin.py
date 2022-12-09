from django.contrib import admin
from  django_twitter_app import models

# Register your models here.

# admin.site.register(models.Post)

class PostAdmin(admin.ModelAdmin):
    """
    Settings admin page for Todo
    """
    list_display = (  # отображение
        'title',
        'description',
    )
    list_display_links = (  # для ссылка (для перехода внутрь)
        'title',
    )
    list_editable = (  # поле, доступное для редактирования в общем списке
        'description',
    )
    list_filter = (  # поля для фильтрации
        'title',
        'description',
    )
    search_fields = (  # поля для поиска (ввод поиска в одном месте)
        'title',
        'description',
    )
    fieldsets = (
        ("Основное", {"fields": ('title',)}),
        ("Дополнительное", {"fields": ('description',)}),
    )


admin.site.register(models.Post, PostAdmin)  # complex register model
