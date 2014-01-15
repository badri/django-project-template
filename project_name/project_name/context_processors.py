rom django.contrib.sites.models import Site, RequestSite

def site(request):
    """Sets in the present context information about the current site."""
    domain = None

    if Site._meta.installed:
        site = Site.objects.get_current()

    else:
        site = RequestSite(request)

    return { 'Site' : site }


def extra_settings(request):
    """Don't pass all the settings information, only selected attributes. This is done for security purposes."""
    pass

