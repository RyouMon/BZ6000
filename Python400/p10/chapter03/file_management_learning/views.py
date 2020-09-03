from django.http import Http404
from django.shortcuts import render
from file_management_learning.models import Photo
# Create your views here.


def get_photo(request, pk):
    try:
        photo = Photo.objects.get(pk=pk)
        return render(request, 'file_management_learning/photo.html', {'photo': photo})
    except Photo.DoesNotExist:
        raise Http404
