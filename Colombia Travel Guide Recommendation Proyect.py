#Colombia Travel Guide Recommendation Proyect
from TravelGuideData import travel_type
from TravelGuideData import travel_destination
from linkedlist import LinkedList
from treenode import TreeNode

#Create Greetings

def Colombia_travel_guide():
    print("*****Welcome to Colombia's paradise!*****\n")
    print("Prepare yourself for a wonderfull trip inside Colombia based on your interests")
    

#Create a the initial tree childs based on travel_type

    def build_tree(travel_destination_data):    
        root = TreeNode("Travel Destations")
        travel_type_map = {}
        for dest in travel_destination:
            type, main_dest, sub_destinations = dest[0], dest[1], dest[2:]
            if type not in travel_type_map:
                travel_type_node = TreeNode(type)
                root.add_child(travel_type_node)
                travel_type_map[type] = travel_type_node
            else:
                travel_type_node = travel_type_map[type]
        
            place_node = TreeNode(main_dest)
            travel_type_node.add_child(place_node)
            for sub_dest in sub_destinations:
                sub_dest_node = TreeNode(sub_dest)
                place_node.add_child(sub_dest_node)
        return root
    
    data_structure_from_data = build_tree(travel_destination)

#Traverse through the Tree
    type_string = ""
    for type in travel_type:
        type_string += "{0}\n".format(type)

    
    def find_travel_type(partial_input):
        for option in travel_type:
            if option.lower().startswith(partial_input.lower()):
                return travel_type.index(option)
        return None
    
    
    while True:
        while True:
            user_input = find_travel_type(input("Enter a travel type (e.g. 'bea' for Beach):\n" + type_string))
            if user_input != None:
                selected_travel_type = travel_type[user_input]
                break
            else:
                print("Sorry, that travel type is not currently available, please choose one of our list\n")

        selected_travel_type_node = None
        for node in data_structure_from_data.children:
            if node.value == selected_travel_type:
                selected_travel_type_node = node
                break
        
        
            
        print("For you, we have the following places for a {0}\n".format(selected_travel_type))
        for index, place in enumerate(selected_travel_type_node.children):
            print(f"{index + 1 }. {place.value}")
        
        partial_place_input = input("\nSelect a place you want to go:\n")
        selected_place = None
        for place_option in selected_travel_type_node.children:
            if place_option.value.lower().startswith(partial_place_input.lower()):
                selected_place = selected_travel_type_node.children[selected_travel_type_node.children.index(place_option)]    
        if selected_place is not None:
            print("Great! These are the following 'must do' in {0}".format(selected_place.value))
            for sub_dest in selected_place.children:
                for index, item in enumerate(sub_dest.value):
                    print(f"{index + 1}. {item}")
        else:
            print("Sorry, that place is not currently available, please choose one of our list")
        print("\nWould you like to try again? (Y/N)")
        if input().strip().lower() != "y":
            break
            

Colombia_travel_guide()



