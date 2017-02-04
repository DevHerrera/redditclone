from django.conf.urls import url
import accounts.views

app_name = 'accounts'
urlpatterns = [
	url(r'^signup/', accounts.views.signup, name = 'sign_up'),
    url(r'^login/', accounts.views.login, name = 'log_in'),
    url(r'^logout/', accounts.views.logout_view, name = 'log_out'),

]
