from django.shortcuts import render, redirect
from .models import Education, Resume, Experience, SkillItem, ResponsibilityItem
from cv.forms import ContactForm
#import narzędzi do serwera pocztowego
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

def show_index(request):
    return render(request, 'index.html', {})

def show_cv(request):
    education = Education.objects.all()
    experience = Experience.objects.all()
    resume = Resume.objects.get(firstname='Karol')
    programming = SkillItem.objects.filter(category='DEV')
    professional = SkillItem.objects.filter(category='PRO')
    other = SkillItem.objects.filter(category='OTH')
    form_class = ContactForm
    enterprises=Experience.objects.all()
    responsibilities=[]
    for element in enterprises:
        responsibilities.append(ResponsibilityItem.objects.filter(experience__enterprise=str(element)))
    #logika sprawdzająca poprawność formularza mailowego
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')
            template = get_template('contact_template.txt')


            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['youremail@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect('cv')
    return render(request, 'cv.html', {'education':education, 'resume':resume, 'experience':experience, 'programming':programming,
                                       'professional':professional, 'other':other, 'form': form_class,'responsibilities':responsibilities})