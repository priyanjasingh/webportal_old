# Create your views here.
from django.shortcuts import render_to_response,HttpResponseRedirect
from django.template import RequestContext
from frontapp.models import contacts
from frontapp.forms import contactForm
def home(request):
	return render_to_response('frontapp/index.html')
def contact(request):
        context = RequestContext(request)
        if request.POST:
		contactform= contactForm(data=request.POST)#fetch form with all the data
		if contactform.is_valid():
			contactform.save(commit=True)
			return HttpResponseRedirect('frontapp/contact')
		else:
			print contactform.errors
	else:
		contactform = contactForm()#fetch empty form 
		print contactform
	context_dict = {
		'contactform':contactform,
	}
	
	return render_to_response("frontapp/contact.html",context_dict,context)
def userlogin(request):
    """Login form.
    
    Arguments:
    - `request`:
    """
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
		for group in user.groups.all:
			if group.name == 'contributor':
		                login(request, user)
                		return HttpResponseRedirect('/user/upload/')
			if group.name == 'reviewer':
				login(request,user)
				return HttpResponseRedirect('/user/review')
            else:
                # An inactive account was used - no logging in!
                messages.info(request, "Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            messages.error(request, "Bad login!")
            return render_to_response('ac/login.html', context)
    else:
        return render_to_response('ac/login.html', context)


