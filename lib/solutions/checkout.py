def criteria(consume, basket):
    print(consume, basket)
    valid = True
    for k in consume:
        if k in basket and basket[k] >= consume[k]:
            basket[k] -= consume[k]
        else:
            valid = False
    return valid

# noinspection PyUnusedLocal
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    deals = [
        {'consume': {'A': 5}, 'output': 200, 'savings': 50},
        {'consume': {'E': 2, 'B': 1}, 'output': 80, 'savings': 30},
        {'consume': {'A': 3}, 'output': 130, 'savings': 20},
        {'consume': 'BB', 'output': 45, 'savings': 15},
    ]
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

    tmp_basket = basket.copy()
    for deal in deals:
        while criteria(deal['consume'], tmp_basket):
            total += deal['output']

    for item in tmp_basket:
        total += basket[item] * prices[item]

    return total
