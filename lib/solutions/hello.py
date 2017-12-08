# noinspection PyUnusedLocal
def hello(friend_name):
    if not isinstance(friend_name, str):
        raise ValueError('arg must be of type string')
    return 'Hello World!'
