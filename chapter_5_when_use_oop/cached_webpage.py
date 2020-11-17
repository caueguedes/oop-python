from urllib.request import urlopen


class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
        return self._content


import time
webpage = WebPage("http://ccphillips.net/")
now = time.time()
content1 = webpage.content  # Retrieving New Page...
print(time.time() - now)

now = time.time()
content2 = webpage.content
print(time.time() - now)

content1 == content2