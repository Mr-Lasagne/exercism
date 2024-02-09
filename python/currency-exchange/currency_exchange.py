"""Solution to Currency Exchange."""


def exchange_money(budget: float, exchange_rate: float) -> float:
    """Calculate the value of exchanged currency.

    :param budget: The amount of money you are planning to exchange.
    :type budget: float
    :param exchange_rate: The unit value of the foreign currency.
    :type exchange_rate: float
    :return: The exchanged value of the foreign currency you can receive.
    :rtype: float
    """
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """Calculate currency left after a currency exchange.

    :param budget: The given amount of money.
    :type budget: float
    :param exchanging_value: The amount of your money you want to exchange.
    :type exchanging_value: float
    :return: The amount of your starting currency left after exchanging.
    :rtype: float
    """
    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Calculate the total value of bills.

    :param denomination: The value of a single bill.
    :type denomination: int
    :param number_of_bills: The total number of bills.
    :type number_of_bills: int
    :return: The calculated value of the bills.
    :rtype: int
    """
    return denomination * number_of_bills


def get_number_of_bills(amount: float, denomination: int) -> int:
    """Calculate the number of bills that can be obtained from a given amount.

    :param amount: A given amount of money.
    :type amount: float
    :param denomination: The value of a single bill.
    :type denomination: int
    :return: The number of bills that can be obtained from the amount.
    :rtype: int
    """
    return int(amount) // denomination


def get_leftover_of_bills(amount: float, denomination: int) -> float:
    """Calculate the amount of money left over after exchanging into bills.

    :param amount: A given amount of money.
    :type amount: float
    :param denomination: The value of a single bill.
    :type denomination: int
    :return: The amount that is left over, given the denomination.
    :rtype: float
    """
    return amount % denomination


def exchangeable_value(
    budget: float,
    exchange_rate: float,
    spread: int,
    denomination: int,
) -> int:
    """Calculate value of the new currency after exchange.

    :param budget: The amount of money you are planning to exchange.
    :type budget: float
    :param exchange_rate: The unit value of the foreign currency.
    :type exchange_rate: float
    :param spread: The percentage that is taken as an exchange fee.
    :type spread: int
    :param denomination: The value of a single bill.
    :type denomination: int
    :return: The maximum value of the new currency you can get after exchange.
    :rtype: int
    """
    adjusted_exchange_rate = (1 + (spread / 100)) * exchange_rate
    exchanged_money = exchange_money(budget, adjusted_exchange_rate)
    number_of_bills = get_number_of_bills(exchanged_money, denomination)
    return get_value_of_bills(denomination, number_of_bills)
