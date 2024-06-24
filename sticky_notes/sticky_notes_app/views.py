from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import StickyNote


# Create your views here.
@login_required  # Ensures user is logged in to access
def index(request):
    """Lists all the stickynotes"""
    notes = StickyNote.objects.all()
    return render(request, "index.html", {"notes": notes})


@login_required
def add_note(request):
    "Create new note and add to index list"
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description") 
        StickyNote.objects.create(title=title, description=description)
        return redirect("index")
    return render(request, "add_note.html")


@login_required
def view_note(request, note_id):
    """View post: title, description and time created"""
    note = get_object_or_404(StickyNote, id=note_id)
    return render(request, "view_note.html", context={"note": note})


@login_required
def edit_note(request, note_id):
    """Allows user to make changes to note title or description"""
    note = get_object_or_404(StickyNote, id=note_id)
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        note.title = title
        note.description = description
        note.save()
        return redirect("view_note", note_id=note.id)
    return render(request, "edit_note.html", context={"note": note})


@login_required
def delete_note(request, note_id):
    "Removes sticky note from notice board"
    note = get_object_or_404(StickyNote, id=note_id)
    if request.method == "POST":
        note.delete()
        return redirect("index")
    return render(request, "delete_note.html", {"note": note})
