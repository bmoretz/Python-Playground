from basicdb import *

db_filename = "geo.json"
tbl_codes = "geozipcodes"

def init_db():
    if db == None:
        load_db(db_filename)

def state_of(zipcode):
    init_db()

    return select(where(db_from(tbl_codes), "Zip Code", zipcode), "State")

def northernmost(state):
    init_db()

    results = orderby(where(db_from(tbl_codes), "State", state), "Longitude")

    if len(results) == 0:     
        raise Exception("No results found for state: " + state)
        
    return results.pop()["Zip Code"]

def zipcodes_in_city(city_name):
    init_db()

    return distinct(select(where(db_from(tbl_codes), "City", city_name), "Zip Code"))

def states_by_size():

    init_db()

    lookup = {}

    for record in db_from(tbl_codes):

        state = record["State"]
        code = record["Zip Code"]

        if state == "State" or code == "Zip Code" or len(state) == 0:
            continue

        if state not in lookup:
            lookup[state] = [ code ]

        if code not in lookup[state]:
            lookup[state].append(code)

    states = { s : len(z) for s, z in lookup.items()}
    return sorted(states, key = states.get)

def test_state_of():
    assert state_of('99553') == ['Alaska']

    for code in ['99553', '36273', '65452', '25724']:
        print(state_of(code))

def test_northernmost():
    state = "Alask"

    northernmost(state)

def test_zipcodes_in_city():
    city_name = "Crockr"

    distinct(select(where(db_from(tbl_codes), "City", city_name), "Zip Code"))

def test_states_by_size():
    print(states_by_size())

if __name__ == "__main__":
    test_northernmost()