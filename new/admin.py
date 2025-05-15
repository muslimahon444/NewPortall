from django.contrib import admin
from .models import NewArticle,Category

class NewArticleAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category)
admin.site.register(NewArticle)


