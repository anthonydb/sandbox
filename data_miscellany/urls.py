from django.urls import path
from data_miscellany.views import (
    BookListFictionView,
    BookListNonfictionView,
    BooklistHomeView,
    VizUSBirthsView,
    DataMiscellanyHomeView,
)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('booklist/fiction/', BookListFictionView, name='fiction_list'),
    path('booklist/nonfiction/', BookListNonfictionView, name='non_fiction_list'),
    path('booklist/', BooklistHomeView.as_view(), name='booklist_home'),
    path('visual-us-births/', VizUSBirthsView.as_view(), name='visual_us_births'),
    path('', DataMiscellanyHomeView.as_view(), name='data_miscellany_home'),
]
