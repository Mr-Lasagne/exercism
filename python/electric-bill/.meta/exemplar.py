def get_extra_hours(hours):
    return (hours + 3) % 24


def get_kW_amount(watts):
    # rounds to one decimal place here
    return round(watts / 1000, 1)


def get_kwh_amount(watts):
    return get_kW_amount(watts) // 3600


def get_efficiency(power_factor):
    return power_factor / 100


def get_cost(watts, power_factor, price):
    return price * (get_kwh_amount(watts) / get_efficiency(power_factor))
