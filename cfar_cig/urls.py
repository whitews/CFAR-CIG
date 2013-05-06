from django.conf.urls import patterns, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^register$', TemplateView.as_view(template_name="register.html"), name='register'),
    url(r'^agenda/1$', TemplateView.as_view(template_name="day_1.html"), name='day_1'),
    url(r'^agenda/2$', TemplateView.as_view(template_name="day_2.html"), name='day_2'),
    url(r'^agenda/3$', TemplateView.as_view(template_name="day_3.html"), name='day_3'),
    url(r'^agenda/4$', TemplateView.as_view(template_name="day_4.html"), name='day_4'),
    url(r'^agenda/5$', TemplateView.as_view(template_name="day_5.html"), name='day_5'),
    url(r'^references', TemplateView.as_view(template_name="references.html"), name='references'),
    url(r'^hotels$', TemplateView.as_view(template_name="hotels.html"), name='hotels'),
    url(r'^contact', TemplateView.as_view(template_name="contact.html"), name='contact'),

    # url(r'^cfar_cig/', include('cfar_cig.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
