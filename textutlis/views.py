from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check the checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    wordcount = request.POST.get('wordcount', 'off')

    analyzed = djtext
    purpose = []

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@!#$%^&*_~`'''
        analyzed = "".join(char for char in analyzed if char not in punctuations)
        purpose.append("Removed Punctuations")

    if fullcaps == "on":
        analyzed = analyzed.upper()
        purpose.append("Changed to Uppercase")

    if newlineremover == "on":
        analyzed = "".join(char for char in analyzed if char not in ("\n", "\r"))
        purpose.append("Removed Newlines")

    if extraspaceremover == "on":
        analyzed = " ".join(analyzed.split())
        purpose.append("Removed Extra Spaces")

    if charcount == "on":
        purpose.append("Character Count")
        char_count = len(analyzed)
        analyzed += f"\nCharacter Count: {char_count}"

    if wordcount == "on":
        purpose.append("Word Count")
        word_count = len(analyzed.split())
        analyzed += f"\nWord Count: {word_count}"

    if purpose:
        params = {'purpose': ', '.join(purpose), 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error: No option selected.")


    
