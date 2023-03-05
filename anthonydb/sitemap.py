from django.contrib.sitemaps import Sitemap, GenericSitemap
from django.contrib import sitemaps
from django.urls import reverse
from quotes.models import Author, Categories, Quote

author_dict = {'queryset': Author.objects.all()}
category_dict = {'queryset': Categories.objects.all()}
quote_dict = {'queryset': Quote.objects.all(), 'date_field': 'create_date'}


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return [
            'home_page_view',
            'about_page_view',
            'sandbox_page_view',
            'awards_page_view',
            'privacy_page_view',
            'search_sotu',
            'sotu_about',
            'booklist_home',
            'fiction_list',
            'non_fiction_list',
            'data_miscellany_home',
            'visual_us_births',
        ]

    def location(self, item):
        return reverse(item)


class ViewSitemap(Sitemap):
    """Reverse static views for XML sitemap."""

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['home', 'info', 'suggest']

    def location(self, item):
        return reverse(item)


sitemaps = {
    'static': StaticViewSitemap,
    'author': GenericSitemap(author_dict, priority=0.6),
    'categories': GenericSitemap(category_dict, priority=0.6),
    'quotes': GenericSitemap(quote_dict, priority=0.8),
    'views': ViewSitemap,
}
