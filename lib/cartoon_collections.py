def roll_call_dwarves(names):
    for i, name in enumerate(names, start=1):
        print(f'{i}. {name}')

def summon_captain_planet(calls):
    call_list = [call.capitalize() + "!" for call in calls]
    return call_list
    # return list(input)

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(snacks):
    cheeses = ["cheddar", "gouda", 'camembert']
    for snack in snacks:
        if snack in cheeses:
            return snack 
    return None

# Commented out Test (Test not accounted for)p
# def summon_captain_planet(input):
#     return list(input)