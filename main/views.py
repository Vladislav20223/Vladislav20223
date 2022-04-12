from django.shortcuts import render
from django.http import HttpResponse

#Шаблон

def base(request):
    return render (request, 'main/base.html')

#Страница приветствия

def index(request):
    return render (request, 'main/index.html')

#Базовые страницы квеста

def one(request):
    return render (request, 'main/one.html')

def two(request):
    return render (request, 'main/two.html')

def threee(request):
    return render (request, 'main/threee.html')

#Разделение квеста

def four(request):
    return render (request, 'main/four.html')

#Если пользователь пошел направо (эта ветка заканчивается выиграшем)
def fiveone(request):
    return render (request, 'main/fiveone.html')

def fivetwo(request):
    return render (request, 'main/fivetwo.html')

def fivethree(request):
    return render (request, 'main/fivethree.html')

def fivefour(request):
    return render (request, 'main/fivefour.html')

def fivefive(request):
    return render (request, 'main/fivefive.html')

def fivesix(request):
    return render (request, 'main/fivesix.html')

def fiveseven(request):
    return render (request, 'main/fiveseven.html')

def fiveeight(request):
    return render (request, 'main/fiveeight.html')

#Если пользователь пошел направо (эта ветка заканчивается проигрышем)

def sixone(request):
    return render (request, 'main/sixone.html')

def sixtwo(request):
    return render (request, 'main/sixtwo.html')

def sixthree(request):
    return render (request, 'main/sixthree.html')

def sixfour(request):
    return render (request, 'main/sixfour.html')

def sevenone(request):
    return render (request, 'main/sevenone.html')

def seventwo(request):
    return render (request, 'main/seventwo.html')

def seventhree(request):
    return render (request, 'main/seventhree.html')


def sevenfive(request):
    return render (request, 'main/sevenfive.html')

def note(request):
    return render (request, 'main/note.html')

def final(request):
    return render (request, 'main/final.html')


#Простой уровень сложности
def aone(request):
    return render (request, 'main/aone.html')

def atwo(request):
    return render (request, 'main/atwo.html')

def athree(request):
    return render (request, 'main/athree.html')

def afour(request):
    return render (request, 'main/afour.html')

def afive(request):
    return render (request, 'main/afive.html')

def asix(request):
    return render (request, 'main/asix.html')

def aseven(request):
    return render (request, 'main/aseven.html')

def aeight(request):
    return render (request, 'main/aeight.html')

def anine(request):
    return render (request, 'main/anine.html')

def aten(request):
    return render (request, 'main/aten.html')

def bone(request):
    return render (request, 'main/bone.html')

def btwo(request):
    return render (request, 'main/btwo.html')


def bthree(request):
    return render (request, 'main/bthree.html')

def bfour(request):
    return render (request, 'main/bfour.html')

def bfive(request):
    return render (request, 'main/bfive.html')

def bfinal(request):
    return render (request, 'main/bfinal.html')

def update_note(request, progress, book_id, note_id):
    note = get_object_or_404(models.Note, id=note_id)
    if request.method == 'GET':
        return render(
            request,
            'note.html',
            context={
                'page': progress.book_page,
                'note': note,
            },
        )
    note.text = request.POST['text']
    note.pinned = 'pinned' in request.POST
    note.page = {
        'keep': note.page,
        'change': progress.book_page,
        'remove': None,
    }[request.POST['page']]
    note.save()
    return _return_to(book_id)

