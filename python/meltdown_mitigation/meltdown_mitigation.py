"""Solution to Meltdown Mitigation."""

TEMP_MAX = 800
NEUTRONS_LOW = 500
TEMP_NEUTRONS_PRODUCT_MAX = 5 * 10**5
ONE_HUNDRED_TEN_PERCENT = 110
NINETY_PERCENT = 90
EIGHTY_PERCENT = 80
SIXTY_PERCENT = 60
THIRTY_PERCENT = 30


def is_criticality_balanced(temperature: float, neutrons_emitted: float) -> bool:
    """Verify criticality is balanced.

    :param temperature: The temperature value (in kelvin).
    :type temperature: float
    :param neutrons_emitted: float - The number of neutrons emitted per second.
    :type neutrons_emitted: float
    :return: True if criticality is balanced, False otherwise.
    :rtype: bool
    """
    return (
        temperature < TEMP_MAX
        and neutrons_emitted > NEUTRONS_LOW
        and (temperature * neutrons_emitted) < TEMP_NEUTRONS_PRODUCT_MAX
    )


def reactor_efficiency(
    voltage: float,
    current: float,
    theoretical_max_power: float,
) -> str:
    """Assess reactor efficiency zone.

    :param voltage: float - The voltage value.
    :type voltage: float
    :param current: The current value.
    :type current: float
    :param theoretical_max_power: The power that corresponds to 100% efficiency.
    :type theoretical_max_power: float
    :return: The colour code corresponding to the level of efficiency.
    :rtype: str
    """
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100
    if efficiency >= EIGHTY_PERCENT:
        return "green"
    if efficiency >= SIXTY_PERCENT:
        return "orange"
    if efficiency >= THIRTY_PERCENT:
        return "red"
    return "black"


def fail_safe(
    temperature: float,
    neutrons_produced_per_second: float,
    threshold: float,
) -> str:
    """Assess and return the status code for the reactor.

    :param temperature: The value of the temperature (in kelvin).
    :type temperature: float
    :param neutrons_produced_per_second: The neutron flux.
    :type neutrons_produced_per_second: float
    :param threshold: The threshold for each status code category.
    :type threshold: float
    :return: The status code.
    :rtype: str
    """
    temperature_neutron_product = temperature * neutrons_produced_per_second
    percentage_of_threshold = (temperature_neutron_product / threshold) * 100
    if percentage_of_threshold < NINETY_PERCENT:
        return "LOW"
    if percentage_of_threshold <= ONE_HUNDRED_TEN_PERCENT:
        return "NORMAL"
    return "DANGER"
