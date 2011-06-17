from django.contrib import admin

from models import Signup

class SignupAdmin(admin.ModelAdmin):
	list_filter = ('invitation_sent', 'added', 'invitees', )
	date_hierarchy = 'added'

admin.site.register(Signup, SignupAdmin)

