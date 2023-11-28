from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About


class AboutModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(About, AboutModelAdmin)
