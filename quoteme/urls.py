
from django.conf.urls import url
from django.contrib import admin
from quotes import views as quotesviews
from authentication import views as authviews

urlpatterns = [
    url(r'^$', quotesviews.index, name='index'),
    url(r'^dashboard/(?P<username>[a-zA-Z%20]+)$', quotesviews.dashboard, name='dashboard'),
    url(r'^dashboard/(?P<username>[a-zA-Z ]+)/add$', quotesviews.dashboard_add_quote, name='dashboard-add-quote'),
    url(r'^dashboard/(?P<username>[a-zA-Z ]+)/details$', quotesviews.dashboard_details, name='details'),
    url(r'^login', authviews.login_view, name='login'),
    url(r'^logout', authviews.logout_view, name='logout'),
    url(r'^like/(?P<quote_id>\d+)', quotesviews.like_button_clicked),
    url(r'^admin/', admin.site.urls),
]
