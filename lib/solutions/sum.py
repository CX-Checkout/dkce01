# noinspection PyShadowingBuiltins,PyUnusedLocal
def sum(x, y):
    if not 0 < x < 100:
        raise ValueError('arg x must be between 0 and 100')
    if not 0 < x < 100:
        raise ValueError('arg y must be between 0 and 100')

    return x + y
