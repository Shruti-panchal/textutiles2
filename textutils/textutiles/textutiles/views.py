# I have created this file -- shruti

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST. get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalise = request.POST.get('capitalise', 'off')
    newline = request.POST.get('newline', 'off')
    extraspace = request.POST.get('extraspace', 'off')

    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[]/^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        prmtrs = {'purpose': 'Removing Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed

    if capitalise == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        prmtrs = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newline == "on":
        analyzed = ""
        for char in djtext:
            if (char != "\n" and char != "\r"):
                analyzed = analyzed + char
        prmtrs = {'purpose': 'Removing Newline', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspace == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        prmtrs = {'purpose': 'Removing Extraspace', 'analyzed_text': analyzed}
        djtext = analyzed

    if (removepunc != "on" and capitalise != "on" and newline != "on" and extraspace != "on"):
        return HttpResponse("please select an option")
    return render(request, 'analyze.html', prmtrs)
