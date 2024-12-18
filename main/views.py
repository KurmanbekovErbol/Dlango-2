from django.shortcuts import render

def mein(requset):
    context = {
        "title": 'Домашнее задание №2',
        "name": 'Курманбеков Эрбол'
    }
    return render(requset, 'index.html', context=context)