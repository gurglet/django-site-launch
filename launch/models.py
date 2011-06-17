from django.db import models

class Signup(models.Model):
	added = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	email = models.EmailField("Leave your email and we'll put you on our invite list.",
		unique=True)
	invitation_sent = models.BooleanField(default=False)
	
	# Number of people this person has successfully invited
	invitees = models.IntegerField(default=0)
	
	def __unicode__(self):
		return u"Signup <%s>" % self.email
