from django.conf.urls.defaults import patterns, include

urlpatterns = patterns(
    "",
    (r'(?P<blog_slug>[\w\-_]+)/', include('cmsplugin_blog.urls')),
    )
