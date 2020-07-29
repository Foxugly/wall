from django.views.generic.dates import ArchiveIndexView, DateDetailView, DayArchiveView, MonthArchiveView, \
    YearArchiveView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Photo, Gallery


# Gallery views.


class GalleryListView(ListView):
    queryset = Gallery.objects.on_site().is_public()
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        return context


class GalleryDetailView(DetailView):
    queryset = Gallery.objects.on_site().is_public()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        return context

class GalleryDateView:
    queryset = Gallery.objects.on_site().is_public()
    date_field = 'date_added'
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        return context

class GalleryDateDetailView(GalleryDateView, DateDetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        return context


class GalleryArchiveIndexView(GalleryDateView, ArchiveIndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        return context


class GalleryDayArchiveView(GalleryDateView, DayArchiveView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        return context


class GalleryMonthArchiveView(GalleryDateView, MonthArchiveView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        return context


class GalleryYearArchiveView(GalleryDateView, YearArchiveView):

    make_object_list = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        return context

# Photo views.


class PhotoListView(ListView):
    queryset = Photo.objects.on_site().is_public()
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        return context


class PhotoDetailView(DetailView):
    queryset = Photo.objects.on_site().is_public()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        return context


class PhotoDateView:
    queryset = Photo.objects.on_site().is_public()
    date_field = 'date_added'
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        return context


class PhotoDateDetailView(PhotoDateView, DateDetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        return context


class PhotoArchiveIndexView(PhotoDateView, ArchiveIndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        return context


class PhotoDayArchiveView(PhotoDateView, DayArchiveView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        return context


class PhotoMonthArchiveView(PhotoDateView, MonthArchiveView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        return context

class PhotoYearArchiveView(PhotoDateView, YearArchiveView):
    make_object_list = True
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        return context
