from porron import Porron

interface = Porron()

people = {
    1: "Cthulhu",
    2: "Godzilla",
    3: "King Kong",
    4: "Thanos"
}

cities = {
    1: "Ocean",
    2: "Jungle",
    3: "Space"
}

residencies = {
    1: 1,
    2: 1,
    3: 2,
    4: 3
}

@interface.handle('/people')
def list_people():
    """List all people"""
    return list(people.items())

@interface.handle('/people/{key_id}')
def show_person(key_id: int):
    """Get a person by ID"""
    return people[key_id]

@interface.handle('/cities')
def list_cities():
    """List all cities"""
    return list(cities.items())

@interface.handle('/cities/{key_id}')
def show_city(key_id: int):
    """Get a city by ID"""
    return cities[key_id]

@interface.handle('/addresses')
def address_book():
    """List all people and cities cities they live in"""
    return [(people[k], cities[v]) for k,v in residencies.items()]

@interface.handle('/addresses/{offset}/{limit}')
def address_list(offset: int, limit: int):
    """List a subset of the address book"""
    return address_book()[offset:offset+limit]
