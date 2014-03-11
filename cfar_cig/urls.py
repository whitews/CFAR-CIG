from django.conf.urls import patterns, url
from django.views.generic import TemplateView

# Main site pages
urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^mission/$', TemplateView.as_view(template_name="mission.html"), name='mission'),
    url(r'^meetings/$', TemplateView.as_view(template_name="meetings.html"), name='meetings_home'),
    url(r'^workshops/$', TemplateView.as_view(template_name="workshops.html"), name='workshops_home'),
    url(r'^protocols/$', TemplateView.as_view(template_name="protocols.html"), name='protocols'),
    url(r'^participating/$', TemplateView.as_view(template_name="participating_cfars.html"), name='participating_cfars'),
    url(r'^vendors/$', TemplateView.as_view(template_name="vendors.html"), name='vendors'),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"), name='contact'),
)

# 2013 Duke Flow Cytometry Workshop
urlpatterns += patterns('',
    url(r'^workshops/2013/DukeFlow/$', TemplateView.as_view(template_name="workshops/2013_Workshop_Duke_FlowCytometry/overview.html"), name='2013_Duke_FC_overview'),
    url(r'^workshops/2013/DukeFlow/register$', TemplateView.as_view(template_name="workshops/2013_Workshop_Duke_FlowCytometry/register.html"), name='2013_Duke_FC_register'),
    url(r'^workshops/2013/DukeFlow/agenda/1$', TemplateView.as_view(template_name="workshops/2013_Workshop_Duke_FlowCytometry/day_1.html"), name='2013_Duke_FC_day_1'),
    url(r'^workshops/2013/DukeFlow/agenda/2$', TemplateView.as_view(template_name="workshops/2013_Workshop_Duke_FlowCytometry/day_2.html"), name='2013_Duke_FC_day_2'),
    url(r'^workshops/2013/DukeFlow/agenda/3$', TemplateView.as_view(template_name="workshops/2013_Workshop_Duke_FlowCytometry/day_3.html"), name='2013_Duke_FC_day_3'),
    url(r'^workshops/2013/DukeFlow/agenda/4$', TemplateView.as_view(template_name="workshops/2013_Workshop_Duke_FlowCytometry/day_4.html"), name='2013_Duke_FC_day_4'),
    url(r'^workshops/2013/DukeFlow/agenda/5$', TemplateView.as_view(template_name="workshops/2013_Workshop_Duke_FlowCytometry/day_5.html"), name='2013_Duke_FC_day_5'),
    url(r'^workshops/2013/DukeFlow/links', TemplateView.as_view(template_name="workshops/2013_Workshop_Duke_FlowCytometry/links.html"), name='2013_Duke_FC_links'),
    url(r'^workshops/2013/DukeFlow/hotels$', TemplateView.as_view(template_name="workshops/2013_Workshop_Duke_FlowCytometry/hotels.html"), name='2013_Duke_FC_hotels'),
    url(r'^workshops/2013/DukeFlow/contact', TemplateView.as_view(template_name="workshops/2013_Workshop_Duke_FlowCytometry/contact.html"), name='2013_Duke_FC_contact'),
)

# 2013 Duke R Workshop
urlpatterns += patterns('',
    url(r'^workshops/2013/DukeR/$', TemplateView.as_view(template_name="workshops/2013_Workshop_Duke_R/overview.html"), name='2013_Duke_R_overview'),
    url(r'^workshops/2013/DukeR/agenda/1$', TemplateView.as_view(template_name="workshops/2013_Workshop_Duke_R/week_1_day_1.html"), name='2013_Duke_R_week_1_day_1'),
    url(r'^workshops/2013/DukeR/agenda/2$', TemplateView.as_view(template_name="workshops/2013_Workshop_Duke_R/week_1_day_2.html"), name='2013_Duke_R_week_1_day_2'),
    url(r'^workshops/2013/DukeR/agenda/3$', TemplateView.as_view(template_name="workshops/2013_Workshop_Duke_R/week_2_day_1.html"), name='2013_Duke_R_week_2_day_1'),
    url(r'^workshops/2013/DukeR/agenda/4$', TemplateView.as_view(template_name="workshops/2013_Workshop_Duke_R/week_2_day_2.html"), name='2013_Duke_R_week_2_day_2'),
    url(r'^workshops/2013/DukeR/links', TemplateView.as_view(template_name="workshops/2013_Workshop_Duke_R/links.html"), name='2013_Duke_R_links'),
    url(r'^workshops/2013/DukeR/contact', TemplateView.as_view(template_name="workshops/2013_Workshop_Duke_R/contact.html"), name='2013_Duke_R_contact'),
)
