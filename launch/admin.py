from django.contrib import admin

from models import Signup

class SignupAdmin(admin.ModelAdmin):
	list_display = ('email', 'added', 'invitees', 'invitation_sent', )
	list_filter = ('invitation_sent', 'added', )
	date_hierarchy = 'added'

admin.site.register(Signup, SignupAdmin)
