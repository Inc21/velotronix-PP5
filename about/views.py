from django.shortcuts import render, redirect
from .models import About
from .forms import ContactForm, AboutForm
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.decorators import login_required


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


@login_required(login_url='/accounts/login/')
def edit_about(request):
    """ A view to edit the about page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    about = About.objects.all()
    delivery = about[0].delivery_info
    returns = about[0].returns_info
    faq = about[0].faq
    privacy = about[0].privacy_policy

    if request.method == 'POST':
        form = AboutForm(request.POST, instance=about[0])
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated About page!')
            return redirect('about')
        else:
            messages.error(request, 'Failed to update About page. '
                                    'Please ensure the form is valid.')
    else:
        form = AboutForm(instance=about[0])
        messages.info(request, 'You are editing the About page.')

    template = 'about/edit_about.html'
    context = {
        'form': form,
        'delivery': delivery,
        'returns': returns,
        'faq': faq,
        'privacy': privacy,
    }

    return render(request, template, context)
