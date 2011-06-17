from django.core.urlresolvers import reverse
from django.db.models import F
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from forms import SignupForm
from models import Signup

import base36

def home(request, code=None):
	signup_inviter = None
	if code:
		try: signup_inviter = Signup.objects.get(pk=base36.base36decode(code.upper()))
		except: pass
	
	form = SignupForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			signup = form.save()
			request.session['code'] = base36.base36encode(signup.pk)
		
			if signup_inviter:
				# Update the inviter's invitee count
				signup_inviter.invitees = F('invitees') + 1
				signup_inviter.save()
		
			return redirect(reverse('launch_app_success'))
		else:
			# If user has signed up already, show the invite code
			try:
				signup = Signup.objects.get(email=form.data.get('email', ''))
				return render_to_response('launch/already_registered.html', {
					'code': base36.base36encode(signup.pk)
				}, context_instance=RequestContext(request))
			except:
				pass
	return render_to_response('launch/form.html', {
		'form': form
	}, context_instance=RequestContext(request))

def success(request):
	return render_to_response('launch/success.html', {
		'code': request.session.get('code', '').lower()
	}, context_instance=RequestContext(request))
