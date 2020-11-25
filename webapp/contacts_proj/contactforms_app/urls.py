from django.urls import path
from .views import (
    contact_create_view,
    contact_change_view,
    contact_detail_view,
)

app_name = 'contacts'
urlpatterns = [
    path('create/', contact_create_view, name='contact-create'),
    path('<uuid:id>/change', contact_change_view, name='contact-change'),
    path('<uuid:id>/', contact_detail_view, name='contact-details'),
]
