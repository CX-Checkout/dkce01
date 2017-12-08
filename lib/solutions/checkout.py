# noinspection PyUnusedLocal
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    deals = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'E': [(2, {'B': 1})]
    }
    basket = {}

    # if not isinstance(skus, str):
    #     raise ValueError('skus must be str')

    for item in skus:
        if item not in prices:
            return -1
        if item in basket:
            basket[item] += 1
        else:
            basket[item] = 1

    total = 0
    for item in basket:
        if item in deals:
            amount = basket[item]
            for deal in deals[item]:
                while amount >= deal[0]:
                    if isinstance(deal[1], int):
                        total += deal[1]
                    elif isinstance(deal[1], dict):
                        for k in deal[1]:
                            if k in basket and basket[k] >= deal[1][k]:
                                total -= deal[1][k] * prices[k]
                        total += deal[0] * prices[item]
                    amount -= deal[0]
            total += amount * prices[item]
        else:
            total += (basket[item] * prices[item])

    return total
