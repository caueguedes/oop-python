import re
import sys


pattern = sys.argv[1]
search_string = sys.argv[2]
match = re.match(pattern, search_string)

if match:
    template = "'{}' matches pattern '{}'"
else:
    template = "'{}' does not match pattern '{}'"

print(template.format(search_string, pattern))

# $ python regex_generic.py "hello worl" "hello world" -> 'hello world' matches pattern 'hello worl'
# $ python regex_generic.py "ello world" "hello world" -> 'hello world' does not match pattern 'ello world'

# patterns
'^hello world$'
'he.lo world'
'he[lp]lo world'  # matches: helpo world; hello world
'hell[a-z] world'
'hell[a-zA-Z0-9] world'

#escaping
'0\.[0-9][0-9]'
'\(abc\]'
'\s\d\w'

# Matching multiple
'hel*o'  # matches 'hellllllllllllllllo'
'[A-Z][a-z]* [a-z]*\.'  # * means zero or many
'[A-Z][a-z]+ [a-z]+\.'  # * means one or many

# Grouping
'abc{3}'  # abccc
'(abc){3}'  # abcabcabc
'[A-Z][a-z]*( [a-z]+)*\.$'  # will match simple english sentences
