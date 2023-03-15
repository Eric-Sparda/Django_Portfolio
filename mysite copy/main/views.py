from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def even(request):
    evens = []
    
    if request.method == 'POST':
        numbers = request.POST.get('Numbers', '')
        if numbers:
            numbers_list = [int(i) for i in numbers.split()]
            for i in numbers_list:
                if i % 2 == 0:
                    evens.append(i)
    return render(request, 'main/even.html', context={'evens': evens})
