# Day 9 - Dictionaries and Nesting. 
# Project: Secret Auction

# A dictionary has a key and a value associated to this key.
# {Key: Value}

# Retrieving items from dictionary ->> print(dict_name["name-of-key"])
# Adding new items to dictionary ->> dict_name["new-key"] = "value"

# empty_list = []
# empty_dict = {}

## Loop through a dictionary
# for key in dict:
#   print(key)
#   print(dict[key])

### NESTING

# Put list and dictionaries inside another dictionary.
# {
#   Key: [List],
#   Key: {Dict},
# }

## Examples:

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5 }
}

# Nesting Dictionaries in Lists
travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]