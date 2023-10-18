from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class HomepageSitemap(Sitemap):
    priority: 0.7
    changefreq = 'weekly'

    def items(self):
        return ['homepage:index']

    def location(self, item):
        return reverse(item)
