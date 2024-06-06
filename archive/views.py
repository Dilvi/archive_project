from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm

def archive_view(request):
    documents = Document.objects.all()
    search_results = None

    if request.method == 'POST':
        if 'add_document' in request.POST:
            form = DocumentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('archive_view')
        elif 'search_by_cell' in request.POST:
            cell_code = request.POST.get('cell_code')
            search_results = Document.objects.filter(cell_code__cell_code=cell_code)

    else:
        form = DocumentForm()

    return render(request, 'archive/archive.html', {'documents': documents, 'form': form, 'search_results': search_results})
