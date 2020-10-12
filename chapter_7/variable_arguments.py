def get_pages(*links):
    for link in links:
        # download the link with urllib
        print(link)


get_pages()
get_pages('http://link1.com')
get_pages('http://link1.com', 'http://link2.com')
