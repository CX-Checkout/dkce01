def criteria(consume, basket):
    print('{}\t\t{}'.format(consume, basket))
    valid = True
    for k in consume:
        if not (k in basket and basket[k] >= consume[k]):
            valid = False
    return valid

def consume(consume, basket):
    for k in consume:
        basket[k] -= consume[k]

# noinspection PyUnusedLocal
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    deals = [
        {'consume': {'A': 5}, 'output': 200, 'savings': 50},
        {'consume': {'E': 2, 'B': 1}, 'output': 80, 'savings': 30},
        {'consume': {'A': 3}, 'output': 130, 'savings': 20},
        {'consume': {'B': 2}, 'output': 45, 'savings': 15},
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

    ##greedy algorithm
    tmp_basket = basket.copy()
    for deal in deals:
        while criteria(deal['consume'], tmp_basket):
            consume(deal['consume'], tmp_basket)
            total += deal['output']
    print(tmp_basket)

    for item in tmp_basket:
        total += tmp_basket[item] * prices[item]
        print(tmp_basket[item] * prices[item])

    return total
