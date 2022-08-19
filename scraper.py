from urllib.parse import urlparse
import scrapy

TARGET_DOMAIN = 'ctfassets.net'
FOLLOW_DOMAIN = 'www.essex.gov.uk'


class AssetSpider(scrapy.Spider):
    name = "assets"
    start_urls = [
        'https://www.essex.gov.uk/'
    ]

    def parse(self, response):
        # Introspect all tags with an src or an href attribute for the target domain
        for img in response.xpath('//@src|//@href').extract():
            if TARGET_DOMAIN in img:
                yield {
                    'asset': img,
                    'source': response.url
                }
        
        # Follow a href to find new pages
        for link in response.xpath('//a/@href').extract():
            # We want to stay within the same site, consider a link to be relative if
            # it has a path but no host or scheme.
            # This excludes URIs like //www.example.com and mailto:example@example.com
            parsed = urlparse(link)
            relative = parsed.path and not parsed.netloc and not parsed.scheme
            # Follow the link if it's relative or if it's absolute within our domain
            if FOLLOW_DOMAIN in link or relative:
                if '?' in link:
                    # Skip parameterised requests
                    continue
                yield response.follow(link, callback=self.parse)
