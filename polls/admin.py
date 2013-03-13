from django.contrib import admin
from polls.models import Poll, Choice

#admin.site.register(Poll)
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['question']}),
            ('Date information', {'field':['pub_date'], 'classes': ['collapse']}),
            ]
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
