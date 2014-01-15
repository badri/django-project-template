USERENA_SIGNIN_REDIRECT_URL = '/'
ANONYMOUS_USER_ID = -1
AUTH_PROFILE_MODULE = 'accounts.UserProfile'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: LOGIN_REDIRECT_URL % {"username": u.username},
}
USERENA_ACTIVATION_REQUIRED = False

USERENA_DISABLE_SIGNUP = False

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

