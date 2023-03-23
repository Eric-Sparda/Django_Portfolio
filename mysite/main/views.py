from django.shortcuts import render,redirect
from .models import logo,welcome,Content,text, price, contact
from .forms import contactform
# Create your views here.
def home(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            contact.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = contactform()
    mylogo = logo.objects.all()[0]
    about = welcome.objects.all()[0]
    content_1 = Content.objects.all()[0]
    content_2 = Content.objects.all()[1]
    text_sample = text.objects.all()[0]
    price_1 = price.objects.all()
    return render(request, 'main/index.html', context={
        "mylogo":mylogo,
        "about":about,
        "content_1":content_1,
        "content_2":content_2,
        "text_sample":text_sample,
        "price_1":price,
        'form':form
    })
