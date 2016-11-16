from django.contrib import admin

# Register your models here.
from .models import Article
from .models import Person
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
admin.site.register(Person,PersonAdmin)
admin.site.register(Article,Article)