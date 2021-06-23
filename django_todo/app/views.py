from django.http.response import HttpResponse
from app.models import Todo
from django.shortcuts import redirect, render

# Create your views here.
def todo(request):
    td = Todo.objects.all()
    return render(request,'url.html',{'td':td})

def save(request):
    if request.method == 'POST':
        link = request.POST.get('n1')
        uid = request.POST.get('n2')
        db = Todo(link = link , uid=uid)
        db.save()
        return redirect(todo)

def goto_link(request,uid):
    url_details = Todo.objects.get(uid=uid)
    return redirect(url_details.link)

