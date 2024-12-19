from django.shortcuts import render, redirect, get_object_or_404
from .forms import LibraryForm
from .models import Library

def library_create(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library_list')
    else:
        form = LibraryForm()
    return render(request, 'library/library_form.html', {'form': form})

def library_list(request):
    libraries = Library.objects.all()
    return render(request, 'library/library_list.html', {'libraries': libraries})

def library_edit(request, id):
    library = get_object_or_404(Library, id=id)
    if request.method == 'POST':
        form = LibraryForm(request.POST, instance=library)
        if form.is_valid():
            form.save()
            return redirect('library_list')
    else:
        form = LibraryForm(instance=library)
    return render(request, 'library/library_form.html', {'form': form})

def library_delete(request, id):
    library = get_object_or_404(Library, id=id)
    if request.method == 'POST':
        library.delete()
        return redirect('library_list') 
    return render(request, 'library/library_confirm_delete.html', {'library': library})