class Options:
    default_options = {
        'port': 21,
        'host': 'localhost',
        'username': None,
        'password': None,
        'debug': False,
    }

    def __init__(self, **kwargs):
        # kwargs will overwrite the first Options.default_options dict
        self.options = {**Options.default_options, **kwargs}
        # self.options = dict(Options.default_options)
        # self.options.update(kwargs)

    def __getitem__(self, item):
        return self.options[item]


options = Options(username="dusty", password="drowssap", debug=True)
options['debug']
