from django.contrib import admin

from . import models

# admin.site.register(models.TestCase)
# admin.site.register(models.Question)
# admin.site.register(models.Choice)
# admin.site.register(models.Answer)
# admin.site.register(models.ProcessingTestCase)


class ChoiceInline(admin.TabularInline):
    model = models.Choice


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline,
    ]
