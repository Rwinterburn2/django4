from django.shortcuts import render, HttpResponse, redirect
from .models import ToDoItem

# Create your views here.

def home(request):
    return render(request, "home.html")

def todos(request):
    items = ToDoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def add_item(request):
    if request.method == "POST":
        # Get data from form
        item_name = request.POST.get('item_name')
        item_done = request.POST.get('item_done') == 'on'  # Checkbox will be 'on' if checked
        
        # Create a new ToDoItem and save it to the database
        new_item = ToDoItem(title=item_name, completed=item_done)
        new_item.save()

        # Redirect to the to-do list page after adding the item
        return redirect('Todos')  # Ensure 'Todos' is the correct URL name for the to-do list

    # If GET request, render the add_item form
    return render(request, "add_item.html")





