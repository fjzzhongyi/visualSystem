from django.conf.urls import url
from app_examples import views

urlpatterns = [
    url(r'^haze_forecast$', views.haze_forecast, name='haze_forecast'),
    url(r'^haze_forecast/get_haze_forecast_chart_data$',
        views.get_haze_forecast_chart_data,
        name='get_haze_forecast_chart_data'),
]