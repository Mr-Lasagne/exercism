def value_of_card(card):
    if card in ("JQK"):
        value = 10
    elif card == "A":
        value = 1
    else:
        value = int(card)

    return value


def higher_card(card_one, card_two):
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    if card_one_value == card_two_value:
        result = card_one, card_two
    elif card_one_value > card_two_value:
        result = card_one
    else:
        result = card_two

    return result


def value_of_ace(card_one, card_two):
    card_one_value = 11 if card_one == "A" else value_of_card(card_one)
    card_two_value = 11 if card_two == "A" else value_of_card(card_two)

    ace_value = 1 if 11 + (card_one_value + card_two_value) > 21 else 11

    return ace_value


def is_blackjack(card_one, card_two):
    return (card_one == "A" or card_two == "A") and (
        value_of_card(card_one) == 10 or value_of_card(card_two) == 10
    )


def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    return 8 < value_of_card(card_one) + value_of_card(card_two) < 12
