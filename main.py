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
        "budget": 5000
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
        "budget": 700
    },
    "Columbus": {
        "attributes": [
            "COLLEGE_TOWN",
            "SPORTS",
        ],
        "synopsis": "Columbus is the state capital and the most populous "
                    "city of the U.S. state of Ohio.",
        "budget": 200
    },
    "Washington DC": {
        "attributes": [
            "AMERICAN_HISTORY",
            "MUSEUMS",
            "POLITICS",
        ],
        "synopsis": "Washington, D.C., the capital of the United States of "
                    "America and the seat of its three branches of government, "
                    "has an unparalleled collection of free, public museums, and "
                    "the lion's share of the nation's most treasured monuments "
                    "and memorials. The vistas on the National Mall between the "
                    "Capitol, Washington Monument, White House, and Lincoln Memorial "
                    "are iconic throughout the world.",
        "budget": 2500
    },
    "Cuba": {
        "attributes": [
            "SPANISH",
            "HISTORIC",
            "TROPICAL",
            "CIGARS",
            "RUM",
            "BEACHES",
        ],
        "synopsis": "Cuba is the largest Caribbean island, between the Caribbean Sea "
                    "and the North Atlantic Ocean. It lies 145 km (90 miles) south of Key West, "
                    "Florida, between the Cayman Islands and the Bahamas, to the west of Haiti, "
                    "and northwest of Jamaica.",
        "budget": 1000
    },
}


def main():
    print("Welcome to JourneyBoiye\n")

    # Prompt for basic info.
    name = input("Name: ")
    salary = input("Salary: ")
    budget = 5000
    age = input("Age: ")
    zipCode = input("What's your zip-code? ")

    likes = input("Tell me about yourself and interests:")
    print()

    print("Welcome {}!".format(name))
    print()

    print("Now, I'm going to ask you where you've been before and what you thought of these places")
    another = ""
    while another != "NO":
        loc = input("Location: ")
        rating = input("Rating (1-5): ")
        comments = input("Comments: ")
        another = input("Another (NO to quit)? ")
        print()


    print("Now enter some commands!")
    print()

    cmd = ""
    while cmd != "QUIT":
        cmd = input("> ").upper()
        if "SALARY" in cmd:
            budget = 1000
        elif "BROWSE" in cmd or "SHOW" in cmd:
            print("Recommendations")
            print()
            suggestions = dict(filter(lambda x: x[1]["budget"] == budget, LOCATIONS.items()))

            for name, attrs in suggestions.items():
                print(name)
                print(attrs["synopsis"])
                print()
                print("Recommended because\n")

                if budget == 5000:
                    print("Seafood")
                    print("CSE Major")
                    print("Large Salary\n")

                    print("Here's what Seattle has to offer")
                    for attr in attrs["attributes"]:
                        print(attr)

                elif budget == 1000:
                    print("Spanish Culture")
                    print("Lower salary\n")

                    print("Here's what Cuba has to offer")
                    for attr in attrs["attributes"]:
                        print(attr)

            print()
            response = input("Thoughts on the above? ")
            print("Thank you for your input")

        elif "FIND" in cmd or "SEARCH" in cmd:
            suggestions = dict(filter(lambda x: "AMERICAN_HISTORY" in x[1]["attributes"], LOCATIONS.items()))
            print("Results")
            print()

            for name, attrs in suggestions.items():
                print("Here's what {} has to offer".format(name))
                print(attrs["synopsis"])
                print()

                for attr in attrs["attributes"]:
                    print(attr)
                print()

        print()

if __name__ == "__main__":
    main()
