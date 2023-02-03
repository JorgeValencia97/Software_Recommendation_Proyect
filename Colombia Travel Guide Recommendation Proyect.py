#Colombia Travel Guide Recommendation Proyect
from TravelGuideData import travel_type
from TravelGuideData import travel_destination

type_string = ""
for type in travel_type:
    type_string += "{0}\n".format(type)


def Colombia_travel_guide():
    print("*****Welcome to Colombia's paradise!*****\n")
    print("Prepare yourself for a wonderfull trip inside Colombia based on your interests")
    print("Type the beggining or whole word based on your favorite travel type:\n" + type_string)


Colombia_travel_guide()