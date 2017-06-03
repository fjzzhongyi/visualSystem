from django.conf.urls import url
from visualization import views

urlpatterns = [
    url(r'^$', views.visual_index, name='visualization'),
    url(r'^introduction/$', views.visual_intro, name='visual_intro'),
    url(r'^algorithms/([_0-9a-zA-Z]+)/([_0-9a-zA-Z]+)', views.visual_alg, name='visual_alg'),
    url(r'^algorithms/submit_alg_data', views.submit_alg_data, name='submit_alg_data'),
]