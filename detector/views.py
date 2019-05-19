from django.shortcuts import render

from .forms import TextForm


def index(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            detected_language = form.detect_language()
            # Reset the form
            form = TextForm()
            return render(request, 'detector/index.html', {'detected_language': detected_language, 'form': form})
    else:
        form = TextForm()
    return render(request, 'detector/index.html', {'form': form})
