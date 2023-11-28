from django.shortcuts import render
from .models import About


def about(request):
    """ A view to return the about page """
    about = About.objects.all()
    delivery = about[0].delivery_info
    returns = about[0].returns_info
    faq = about[0].faq
    privacy = about[0].privacy_policy

    template = "about/about.html"
    context = {
        'delivery': delivery,
        'returns': returns,
        'faq': faq,
        'privacy': privacy,
    }

    return render(request, template, context)
