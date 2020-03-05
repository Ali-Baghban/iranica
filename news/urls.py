from django.urls import path


from .views import news_view,news_details
urlpatterns = [
    path('', news_view, name='news'),
    path('<int:news_id>', news_details, name='news_details')
]
