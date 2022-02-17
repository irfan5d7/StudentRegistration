from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    data = ["Irfan Mohammad", "Anitha Shivaramaiah", "Anthony	Johnson", "Hrushith Bobba", "Rahul Somavarapu",
            "Saketh Gondela", "Shivakumar Soma", "Varsha Srinivasan"]
    context = {'data': data}
    return render(request, 'about.html', context=context)
