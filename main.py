import pprint

# Synopsis from Wikipedia.
LOCATIONS = {
    "Seattle": {
        "attributes": [
            "WINTER_SPORTS",
            "WATER_SPORTS",
            "HIKING",
            "SEAFOOD",
            "SPORTS",
        ],
        "synopsis": "Seattle is a seaport city on the west coast of the "
                    "United States.",
    },
    "Boston": {
        "attributes": [
            "SEAFOOD",
            "AMERICAN_HISTORY",
            "SPORTS",
        ],
        "synopsis": "Boston is the capital city and most populous "
                    "municipality of the Commonwealth of Massachusetts "
                    "in the United States.",
    },
    "Columbus": {
        "attributes": [
            "COLLEGE_TOWN",
            "SPORTS",
        ],
        "synopsis": "Columbus is the state capital and the most populous "
                    "city of the U.S. state of Ohio.",
    },
}


def main():
    print("Welcome to JourneyBoiye")

    # Prompt for user's name.
    name = input("Name: ")
    print("Welcome {}!".format(name))

    # Prompt for what they do/don't like.
    likes = input("What kinds of things do you like?\n")

    # Prompt for current zip-code.
    zipCode = input("What's your zip-code? ")

    print("Given your profile, you may be interested in:")

    # We're going to hardcode some search criteria.
    suggestions = dict(filter(lambda x: "SEAFOOD" in x[1]["attributes"], LOCATIONS.items()))

    pprint.pprint(suggestions)

if __name__ == "__main__":
    main()
