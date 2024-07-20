from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Queue
from .forms import QueueForm

@login_required
def queue_list(request):
    items = Queue.objects.filter(user=request.user)
    return render(request, 'queue_list.html', {'items': items})

@login_required
def add_to_queue(request):
    if request.method == 'POST':
        form = QueueForm(request.POST)
        if form.is_valid():
            queue_item = form.save(commit=False)
            queue_item.user = request.user
            queue_item.save()
            return redirect('queue_list')
    else:
        form = QueueForm()
    return render(request, 'add_to_queue.html', {'form': form})

@login_required
def update_status(request, item_id, status):
    item = Queue.objects.get(id=item_id, user=request.user)
    if item:
        item.status = status
        item.save()
    return redirect('queue_list')
