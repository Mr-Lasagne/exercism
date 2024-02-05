def get_list_of_wagons(*args):
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    first, second, locomotive, *rest = each_wagons_id

    return [locomotive, *missing_wagons, *rest, first, second]


def add_missing_stops(route, **kwargs):
    return {**route, "stops": list(kwargs.values())}


def extend_route_information(route, more_route_information):
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    [*row_one], [*row_two], [*row_three] = zip(*wagons_rows)

    return [row_one, row_two, row_three]
