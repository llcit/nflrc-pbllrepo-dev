# utils.py

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

from social.exceptions import AuthForbidden


def logout_clean(request):
    logout(request)
    return redirect('https://accounts.google.com/Logout?&continue=https://www.google.com')


def auth_allowed(response, details, *args, **kwargs):
    """
    Return the nflrc pbll repo user object if authenticated email matches a user email.
    Implies that allowed users must be created in system beforehand, with an
    email that matches the gmail account used to authenticate.
    """
    try:
        print 'Google USER ==> ', details
        nflrc_user = User.objects.get(email=details.get('email'))
        return nflrc_user
    except:
        return None


def nflrc_auth_allowed(backend, details, response, *args, **kwargs):
    """
    If auth_allowed returns a user object, set the user variable for the pipeline.
    A valid user variable is processed to determine if a social (google) association needs
    to be created. See nflrc_social for the next op in the pipeline.
    """
    nflrc_user = auth_allowed(response, details)
    if not nflrc_user:
        raise AuthForbidden(backend)
    else:
        return {'user': nflrc_user}


def nflrc_social_user(backend, uid, user=None, *args, **kwargs):
    """
    Previous pipeline op, nflrc_auth_allowed, should prevent a null user but
    checking here, again, just in case.
    The effect of this op is that a social association is set. If social association
    is None, the pipeline will create a new social association to the nflrc user object.
    Subsequent (non overridden pipeline ops) will process as designed, based on the social and user
    variables being initialized with values.
    """
    if user:
        provider = backend.name
        social = backend.strategy.storage.user.get_social_auth(provider, uid)
        if not social:  # user has not logged in previously (e.g., no social auth obj exists) -- make their account active.
            user.is_active = True
    else:
        raise AuthForbidden(backend)
    return {'social': social,
            'user': user,
            'is_new': user is None,
            'new_association': False}


