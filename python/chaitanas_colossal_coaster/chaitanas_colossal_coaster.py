"""Solution to Chaitana's Colossal Coaster."""

from __future__ import annotations


def add_me_to_the_queue(
    express_queue: list[str],
    normal_queue: list[str],
    ticket_type: int,
    person_name: str,
) -> list[str]:
    """Add a person to the express or normal queue depending on the ticket type.

    :param express_queue: The names in the fast-track queue.
    :type express_queue: list[str]
    :param normal_queue: The names in the normal queue.
    :type normal_queue: list[str]
    :param ticket_type: The type of ticket. 1 = express, 0 = normal.
    :type ticket_type: int
    :param person_name: The name of person to add to a queue.
    :type person_name: str
    :return: The updated queue the name was added to.
    :rtype: list[str]
    """
    queue = express_queue if ticket_type == 1 else normal_queue
    queue.append(person_name)
    return queue


def find_my_friend(queue: list[str], friend_name: str) -> int:
    """Search the queue for a name and return their queue index.

    :param queue: The names in the queue.
    :type queue: list[str]
    :param friend_name: The name of friend to find.
    :type friend_name: str
    :return: The index at which the friends name was found.
    :rtype: int
    """
    return queue.index(friend_name)


def add_me_with_my_friends(queue: list[str], index: int, person_name: str) -> list[str]:
    """Insert the late arrival's name at a specific index of the queue.

    :param queue: The names in the queue.
    :type queue: list[str]
    :param index: The index at which to add the new name.
    :type index: int
    :param person_name: The name to add.
    :type person_name: str
    :return: The queue updated with new name.
    :rtype: list[str]
    """
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: list[str], person_name: str) -> list[str]:
    """Remove the mean person, given by the provided name, from the queue.

    :param queue: The names in the queue.
    :type queue: list[str]
    :param person_name: The name of mean person.
    :type person_name: str
    :return: The queue updated with the mean persons name removed.
    :rtype: list[str]
    """
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue: list[str], person_name: str) -> int:
    """Count how many times the provided name appears in the queue.

    :param queue: The names in the queue.
    :type queue: list[str]
    :param person_name: The name you wish to count or track.
    :type person_name: str
    :return: The number of times the name appears in the queue.
    :rtype: int
    """
    return queue.count(person_name)


def remove_the_last_person(queue: list[str]) -> str:
    """Remove the person in the last index from the queue and return their name.

    :param queue: The names in the queue.
    :type queue: list[str]
    :return: The name that has been removed from the end of the queue.
    :rtype: str
    """
    return queue.pop()


def sorted_names(queue: list[str]) -> list[str]:
    """Sort the names in the queue in alphabetical order and return the result.

    :param queue: The names in the queue.
    :type queue: list[str]
    :return: A copy of the queue in alphabetical order.
    :rtype: list[str]
    """
    return sorted(queue)
