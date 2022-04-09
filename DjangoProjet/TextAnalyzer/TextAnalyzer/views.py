#I have created this file - 'Amir'

from django.http import HttpResponse
from django.shortcuts import render


# Templates1
def homepage(request):
    return render(request, 'homepage.html')



# Analyze_Post_request

def analyze(request):
    # get textarea
    textarea = request.POST.get('textarea', 'default_none')

    #get checkbox value (on/off)
    RemovePunc_Box = request.POST.get('RemovePunc_Box', 'off')
    Capitalized_Box = request.POST.get('Capitalized_Box', 'off')
    RemoveNewline_Box = request.POST.get('RemoveNewline_Box', 'off')
    ExtraSpaceRemover_Box = request.POST.get('ExtraSpaceRemover_Box','off')
    CharacterCounter_Box = request.POST.get('CharacterCounter_Box', 'off')

    # Analyze TextArea
    # check checkbox value (on/off)
    purpose = ''
    if (RemovePunc_Box == 'on'):
        analyzed = ""
        punctuations_list = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in textarea:
            if char not in punctuations_list:
                analyzed = analyzed + char
        purpose += '*Remove Punctuations\n'
        params = {'purpose':purpose, 'analyzed_text':analyzed}
        textarea = analyzed

    if(Capitalized_Box == 'on'):
        analyzed = ""
        for char in textarea:
            analyzed = analyzed + char.upper()
        purpose += '*Capitalized Text\n'
        params = {'purpose':purpose, 'analyzed_text': analyzed}
        textarea = analyzed

    if(RemoveNewline_Box == 'on'):
        analyzed = ""
        for char in textarea:
            if char != '\n' and char !='\r': #escape cahracter in python
                analyzed = analyzed + char
        purpose += '*Removed New lines\n'
        params = {'purpose':purpose, 'analyzed_text': analyzed}
        textarea = analyzed

    if(ExtraSpaceRemover_Box == 'on'):
        analyzed = ""
        textarea = textarea.strip()

        for index, char in enumerate(textarea):
            if not (textarea[index] == " " and textarea[index+1] == " ") :
                analyzed = analyzed + char
        purpose += '*Extra Space Removering\n'
        params = {'purpose':purpose, 'analyzed_text':analyzed}
        textarea = analyzed

    if(CharacterCounter_Box == 'on'):
        count = len(textarea)
        purpose += '* Counting Character\n'
        params = {'purpose':purpose, 'analyzed_text':analyzed + '.\nCount Character : ' + str(count)}

    if (RemoveNewline_Box == 'off' and Capitalized_Box == 'off' and RemovePunc_Box == 'off' and ExtraSpaceRemover_Box == 'off'):
        return HttpResponse("Error : Please check the CheckBox !")

    return render(request, 'output_analyzed.html', params)

