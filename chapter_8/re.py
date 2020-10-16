import re

pattern = "[a-zA-Z.]+@([a-z]*\.[a-z]+)$"
search_string = "some.user@wxample.com"
match = re.match(pattern, search_string)

if match:
    domain = match.groups()[0]
    print(domain)

import re
re.findall('a.', 'abacadefagah')  # ['ab', 'ac', 'ad', 'ag', 'ah']
re.findall('a(.)', 'abacadefagah')  # ['b', 'c', 'd', 'g', 'h']
re.findall('(a)(.)', 'abacadefagah')  #[('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'g'), ('a', 'h')]
re.findall('((a)(.))', 'abacadefagah')  # [('ab', 'a', 'b'), ('ac', 'a', 'c'), ('ad', 'a', 'd'), ...


re.search(pattern, search_string)  # will return first match
