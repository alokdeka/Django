from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{}:;"'\,<>./?@#$%^&*_~  '''
        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Upper', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove Newlines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
            else:
                return HttpResponse("Error!")
        params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif charcount == "on":
        count = 0;
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " or djtext[index] == "\n"):
                count = count + 1
        params = {'purpose': 'Character Count', 'analyzed_text': count}
        return render(request, 'analyze.html', params)

    if removepunc != "on" and fullcaps !="on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on":
        return HttpResponse("Please select one operation and try again!")