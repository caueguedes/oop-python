def no_args():
    pass


def mandatory_args(x, y, z):
    pass


def default_arguments(x, y, z, a="Some string", b=False):
    pass


def kw_only(x, y=' default_kw', *, a, b=' only'):
    print(x, y, a, b)


kw_only('x', a='mandatory')

