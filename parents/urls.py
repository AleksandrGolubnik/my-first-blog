from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from parents.models import Advice
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Advice.objects.all().order_by("-date")[:20],
        template_name="parents/blogs.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Advice, template_name="parents/blog.html")),

       ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
