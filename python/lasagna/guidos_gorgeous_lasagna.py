"""Solution to Guido's Gorgeous Lasagna."""

EXPECTED_BAKE_TIME = 40
LAYER_PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: The baking time (in minutes) that has already
        elapsed.
    :type elapsed_bake_time: int
    :return: The remaining bake time (in minutes) based on 'EXPECTED_BAKE_TIME'.
    :rtype: int
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def total_layer_preparation_time(number_of_layers: int) -> int:
    """Calculate the preparation time.

    :param number_of_layers: The number of lasagna layers.
    :type number_of_layers: int
    :return: The preparation time (in minutes) based on 'PREPARATION_TIME'.
    :rtype: int
    """
    return LAYER_PREPARATION_TIME * number_of_layers


def total_elapsed_cooking_time(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the elapsed cooking time.

    :param number_of_layers: The number of layers in the lasagna.
    :type number_of_layers: int
    :param elapsed_bake_time: The elapsed cooking time (in minutes).
    :type elapsed_bake_time: int
    :return: The total time elapsed (in minutes) preparing and cooking.
    :rtype: int
    """
    return total_layer_preparation_time(number_of_layers) + elapsed_bake_time
