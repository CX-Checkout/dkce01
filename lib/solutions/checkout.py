# noinspection PyUnusedLocal
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    deals = {'A': (3, 130), 'B': (2, 45)}
    basket = {}

    if not isinstance(skus, str):
        raise ValueError('skus must be str')

    for item in skus:
        if item not in prices:
            return -1
        if item in basket:
            basket[item] += 1
        else:
            basket[item] = 1

    total = 0
    for item in basket:
        total += (basket[item] % deals[item][0]) * prices[item]
        if basket[item] >= deals[item][0]:
            # excess
            total += (basket[item] // deals[item][0]) * deals[item][1]

    return total
