from django.conf.urls import include, url
from . import views
import social.apps.django_app.urls
import paypal.standard.ipn.urls
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^accounts/logout/$', views.account_logout, name='logout'),
    url(r'^accounts/login/$', views.func1, name='login'),
    url('', include(social.apps.django_app.urls, namespace='social')),
    url(r'^shop1/$', views.func1, name='shop1'),
    url(r'^shop2/(?P<product_id>[0-9]+)/$', views.func2, name='shop2'),
    url(r'^shop3/$', views.func3, name='shop3'),
    url(r'^shop4/$', views.func4, name='shop4'),
    url(r'^add-to-cart/$', views.add_to_cart, name='add'),
    url(r'^remove-from-cart/$', views.remove_from_cart, name='remove'),
    url(r'^payment/cart/$', views.paypal_pay, name='cart'),
    url(r'^payment/success/$', views.paypal_success, name='success'),
    url(r'^paypal/', include(paypal.standard.ipn.urls)),
]
