from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from activity.models import Upload

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Upload.objects.all(),
        template_name="activity/files.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Upload, template_name="activity/file.html")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
