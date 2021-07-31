from django.contrib import admin
from .models import Resume, Form, Field, Education, Experience, Review, \
    Portfolio, SkillDescription, SkillName, Awards, Certificate, MetaData, UserIP

admin.site.register(Resume)
admin.site.register(Form)
admin.site.register(Field)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Review)
admin.site.register(Portfolio)
admin.site.register(SkillDescription)
admin.site.register(SkillName)
admin.site.register(Awards)
admin.site.register(Certificate)
admin.site.register(MetaData)

class UserIPAdmin(admin.ModelAdmin):
    list_display = ('ip', 'first_visited', 'last_visited') 

admin.site.register(UserIP, UserIPAdmin)

