#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)

    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)

    crnt_local = "NONE"

    for i in range(length-1):
        route[i] = hash_table_retrieve(hashtable, crnt_local)
        crnt_local = route[i]

    return route