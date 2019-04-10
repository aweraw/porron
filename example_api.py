from porron import Porron

interface = Porron()

people = {
    1: "Aidan Williams",
    2: "Matt Ogle",
    3: "Pat Robinson",
    4: "Mike Pearson"
}

cities = {
    1: "Melbourne",
    2: "Russell Island",
    3: "Wangaratta"
}

residencies = {
    1: 2,
    2: 1,
    3: 3,
    4: 1
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
def list_cities() -> list:
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
