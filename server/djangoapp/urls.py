# Uncomment the imports before you add the code
from django.urls import path  # type: ignore
from django.conf.urls.static import static  # type: ignore
from django.conf import settings  # type: ignore
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration
    path(route='registation', view=views.registration, name='registration'),

    # path for login
    path(route='login', view=views.login_user, name='login'),
    path(route='logout', view=views.logout_request, name='logout'),

    # path for dealer reviews view

    # path for add a review view
    # PATH for get cars
    path('get_cars', views.get_cars, name='getcars'),
    path(route='get_dealers', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/', view=views.get_dealerships, name='get_dealers'),
    path(route='dealer/<int:dealer_id>',
         view=views.get_dealer_details, name='dealer_details'),
    path(route='reviews/dealer/<int:dealer_id>',
         view=views.get_dealer_reviews, name='dealer_details'),
    path(route='add_review', view=views.add_review, name='add_review'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
