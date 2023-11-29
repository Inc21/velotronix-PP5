from django.shortcuts import render, redirect
from .models import About
from .forms import ContactForm, AboutForm
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse


def about(request):
    """ A view to return the about page """
    about = About.objects.all()
    delivery = about[0].delivery_info
    returns = about[0].returns_info
    faq = about[0].faq
    privacy = about[0].privacy_policy

    form = ContactForm()
    author = ""
    email = ""
    subject = ""
    message = ""

    if request.method == "POST":
        form = ContactForm(request.POST)
        user = request.user
        if form.is_valid():
            author = form.cleaned_data['author']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            form.save()

            html = render_to_string('about/emails/contact_form.html', {
                'author': author,
                'email': email,
                'subject': subject,
                'message': message,
                'user': user,
            })

            send_mail('The contact form entry',
                      'The contact form message',
                      'noreply@test.com', ['intc21@gmail.com'],
                      fail_silently=False, html_message=html)
            messages.success(request, 'Message sent successfully!')
            return redirect("about")

    else:
        form = ContactForm()

    template = "about/about.html"
    context = {
        'delivery': delivery,
        'returns': returns,
        'faq': faq,
        'privacy': privacy,
        'form': form,
        'author': author,
        'email': email,
        'subject': subject,
        'message': message,
    }

    return render(request, template, context)


# def contactUs(request):
#     """
#     This view will display the contact form.
#     """
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         tm_email = request.user.userprofile.email
#         tm_profile = request.user.userprofile.username
#         if form.is_valid():
#             author = form.cleaned_data['author']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']

#             html = render_to_string('users/emails/contact_developer.html', {
#                 'author': author,
#                 'email': email,
#                 'subject': subject,
#                 'message': message,
#                 'tm_profile': tm_profile,
#                 'tm_email': tm_email,
#             })

#             send_mail('The contact form entry',
#                       'The contact form message',
#                       'noreply@test.com', ['intc21@gmail.com'],
#                       fail_silently=False, html_message=html)
#             messages.success(request, 'Message sent successfully!')
#             # next = request.GET.get('next', reverse('contact-form'))
#             # return HttpResponseRedirect(next)
#     else:
#         form = ContactForm()

#     template = "about/about.html"
#     context = {'form': form}
#     return render(request, template, context)
