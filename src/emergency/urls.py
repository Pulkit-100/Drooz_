from django.conf.urls import url

from .views import home_view,add_contact,added#, EmergencyCreate


urlpatterns = [
    url(r'^$', home_view,name="home"),
    url(r'^add/$', add_contact,name="add_contact"),
    url(r'^added/$', added,name="added"),


]