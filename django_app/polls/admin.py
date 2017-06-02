from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model=Choice
    extra=3


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question_text','pub_date','was_published_recently',
    )
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]




admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)