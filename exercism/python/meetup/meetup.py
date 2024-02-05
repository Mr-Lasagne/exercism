# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    def __init__(self):
        raise NotImplementedError("This method has not been implemented yet.")


def meetup(year, month, week, day_of_week):
    raise NotImplementedError("This function has not been implemented yet.")
