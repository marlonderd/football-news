from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406496201',
        'name': 'Marlond Leanderd Batara',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)

# Create your views here.
