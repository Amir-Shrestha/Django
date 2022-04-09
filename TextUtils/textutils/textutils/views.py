# I have created this file - Amir

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyzed(request):
    # Get form value(text,checkbox_value)
    textarea2 = request.GET.get('textarea1', 'default')
    remove_punc2 = request.GET.get('remove_punc1', 'off')
    full_cap2 = request.GET.get('full_cap1', 'off')
    new_line_remover2 = request.GET.get('new_line_remover1', 'off')
    extra_space_remover2 = request.GET.get('extra_space_remover1', 'off')
    # character_count2 = request.GET.get('character_count1', 'off')
    purpose=''

    # Analyze Form Text according to check box
    if remove_punc2=='on':
        analyzed_text = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in textarea2:
            if char not in punctuations:
                analyzed_text = analyzed_text + char
        textarea2 = analyzed_text
        purpose = purpose + 'Remove Puncuation,'

    if full_cap2=='on':
        analyzed_text = ''
        for char in textarea2:
            analyzed_text = analyzed_text + char.upper()
        textarea2 = analyzed_text
        purpose = purpose + '  Full CAPITALIZED,'

    if new_line_remover2=='on':
        analyzed_text = ''
        for char in textarea2:
            if char != '\n':
                print('yes')
                analyzed_text = analyzed_text + char
        textarea2 = analyzed_text
        purpose = purpose + '  New Line Removed,'


    if extra_space_remover2=='on':
        analyzed_text = ''
        for index,char in enumerate(textarea2):
            if not(textarea2[index]==' ' and textarea2[index+1]==' '):
                analyzed_text = analyzed_text + char
        textarea2 = analyzed_text
        purpose = purpose + '  Extra Space Removed,'
            # print(textarea2[index + 1]) # it works but at last it gives error index out of range

    # if character_count2=='on':
    #     count = len(textarea2)
    #     purpose = purpose + 'Character Counted'
    #     return render(request,'analyze.html', params)


    if(extra_space_remover2=='off' and new_line_remover2=='off' and full_cap2=='off' and remove_punc2=='off'):
        return HttpResponse("  No Purpose !")

    params = {'purpose': purpose, 'analyzed_text': textarea2}
    return render(request,'analyze.html', params)

def nav(request):
    navbar = '''
        <h2>NavBar :</h2>
            <a href=''> Home </a><br>
            <a href='https://www.facebook.com/'> FB </a><br>
            <a href='https://www.youtube.com/'> YoutubE </a><br>
            <a href='https://www.instagram.com/'> InstgraM </a><br>
            <a href='https://twitter.com/?lang=en'> TwitteR </a><br>
            <a href='https://www.linkedin.com/signup/cold-join'> LinkdiN </a><br>
    '''
    return HttpResponse(navbar)


