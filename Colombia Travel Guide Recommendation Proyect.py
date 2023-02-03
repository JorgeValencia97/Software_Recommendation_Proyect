#Colombia Travel Guide Recommendation Proyect
from TravelGuideData import travel_type
from TravelGuideData import travel_destination
from linkedlist import LinkedList
from treenode import TreeNode

#Create Greetings
type_string = ""
for type in travel_type:
    type_string += "{0}\n".format(type)

def Colombia_travel_guide():
    print("*****Welcome to Colombia's paradise!*****\n")
    print("Prepare yourself for a wonderfull trip inside Colombia based on your interests")
    print("Type the beggining or whole word based on your favorite travel type:\n" + type_string)

#Create a the initial tree childs based on travel_type

def build_tree(travel_destination_data):
    root = TreeNode("Travel Destations")
    travel_type_map = {}
    for dest in travel_destination:
        travel_type, main_dest, sub_destinations = dest[0], dest[1], dest[2:]
        if travel_type not in travel_type_map:
            travel_type_node = TreeNode(travel_type)
            root.add_child(travel_type_node)
            travel_type_map[travel_type] = travel_type_node
        else:
            travel_type_node = travel_type_map[travel_type]
        
        place_node = TreeNode(main_dest)
        travel_type_node.add_child(place_node)
        for sub_dest in sub_destinations:
            sub_dest_node = TreeNode(sub_dest)
            place_node.add_child(sub_dest_node)
    
    return root







