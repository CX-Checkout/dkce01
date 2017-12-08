def criteria(consume, basket):
    valid = True
    for k in consume:
        if len(k) > 1:
            amt = 0
            for i in k:
                if i in basket:
                    amt += basket[i]
                    if amt >= consume[k]:
                        return True
        elif not (k in basket and basket[k] >= consume[k]):
            valid = False
    return valid

def consume(consume, basket):
    for k in consume:
        if len(k) > 1:
            for i in k:
                amt = 0
                if i in basket:
                    if (amt + basket[i]) > consume[k]:
                        basket[i] -= consume[k] - amt
                    else:
                        amt += basket[i]
        else:
            basket[k] -= consume[k]

# noinspection PyUnusedLocal
def checkout(skus):
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10,
        'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 70, 'L': 90,
        'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
        'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17,
        'Y': 20, 'Z': 21
    }
    deals = [
        {'consume': {'A': 5}, 'output': 200, 'savings': 50},
        {'consume': {'P': 5}, 'output': 200, 'savings': 50},
        {'consume': {'U': 4}, 'output': 120, 'savings': 40},
        {'consume': {'E': 2, 'B': 1}, 'output': 80, 'savings': 30},
        {'consume': {'R': 3, 'Q': 1}, 'output': 150, 'savings': 30},
        {'consume': {'H': 10}, 'output': 80, 'savings': 20},
        {'consume': {'V': 3}, 'output': 130, 'savings': 20},
        {'consume': {'A': 3}, 'output': 130, 'savings': 20},
        {'consume': {'B': 2}, 'output': 45, 'savings': 15},
        {'consume': {'N': 3, 'M': 1}, 'output': 120, 'savings': 15},
        {'consume': {'STXYZ': 3}, 'output': 45, 'savings': 15},
        {'consume': {'K': 2}, 'output': 150, 'savings': 10},
        {'consume': {'V': 2}, 'output': 90, 'savings': 10},
        {'consume': {'Q': 3}, 'output': 80, 'savings': 10},
        {'consume': {'F': 3}, 'output': 20, 'savings': 10},
        {'consume': {'H': 5}, 'output': 45, 'savings': 5}
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

    for item in tmp_basket:
        total += tmp_basket[item] * prices[item]

    return total
