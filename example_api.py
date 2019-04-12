from porron import Porron

beings = {
    1: "Cthulhu",
    2: "Godzilla",
    3: "King Kong",
    4: "Thanos"
}

locales = {
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

interface = Porron()

@interface.handle('/beings')
def list_beings():
    """List all beings"""
    return list(beings.items())

@interface.handle('/beings/{key_id}')
def show_being(key_id: int):
    """Get a being by ID"""
    return beings[key_id]

@interface.handle('/locales')
def list_locales():
    """List all locales"""
    return list(locales.items())

@interface.handle('/locales/{key_id}')
def show_locale(key_id: int):
    """Get a locale by ID"""
    return locales[key_id]

@interface.handle('/addresses')
def address_book():
    """List all beings and locales they live in"""
    return [(beings[k], locales[v]) for k,v in residencies.items()]

@interface.handle('/addresses/{offset}/{limit}')
def address_list(offset: int, limit: int):
    """List a subset of the address book"""
    return address_book()[offset:offset+limit]
