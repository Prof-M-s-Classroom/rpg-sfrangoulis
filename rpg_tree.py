from sqlalchemy import false


class StoryNode:
    """Represents a node in the decision tree."""
    def __init__(self, event_number, description, left=None, right=None):
        # print(f"TODO: Initialize StoryNode with event_number={event_number}, description={description}")
        # TODO: Initialize instance variables (event_number, description, left, right)
        self.event_number = event_number
        self.description = description
        self.left = left
        self.right = right


class GameDecisionTree:
    """Binary decision tree for the RPG."""
    def __init__(self):
        # print("TODO: Initialize an empty decision tree")
        # TODO: Initialize an empty dictionary to store nodes
        self.nodes={}
        # TODO: Set root to None
        self.root = None


    def insert(self, event_number, description, left_event, right_event):
        """Insert a new story node into the tree."""
        # print(f"TODO: Insert event {event_number} with description '{description}' into the tree")
        # TODO: Check if event_number exists in self.nodes, if not create a new StoryNode
        # TODO: Set root if it's the first node inserted
        # TODO: Assign left and right children based on left_event and right_event
        if event_number  not in self.nodes:
            self.nodes[event_number]=(StoryNode(event_number,description))
        else:
            self.nodes[event_number].description = description

        self.nodes[left_event] = StoryNode(left_event, None)
        self.nodes[right_event] = StoryNode(right_event,None  )
        self.nodes[event_number].left = self.nodes[left_event]
        self.nodes[event_number].right = self.nodes[right_event]

        if(self.root is None):
            self.root = self.nodes[event_number]

    def play_game(self):
        """Interactive function that plays the RPG."""
        # print("TODO: Implement the game logic for traversing the decision tree")

        # TODO: Start from the root node
        current_node = self.root

        # TODO: Loop through player choices, navigating left or right based on input
        while current_node:

            print(current_node.description)
            if (current_node.left is None and current_node.right is None):
                print("end")
                break
            decision = input("Decision?: ").lower()
            if(decision == 'left'):
                current_node = current_node.left
            elif(decision == 'right'):
                current_node = current_node.right

        # TODO: Print event descriptions and ask for player decisions


        # TODO: End game when reaching a leaf node (where left and right are None)



def load_story(filename, game_tree):
    """Load story from a file and construct the decision tree."""
    # print(f"TODO: Read story file '{filename}' and parse events")
    # TODO: Open the file and read line by line
    with open(filename) as file:
        for line in file:
            line = line.strip()


    # TODO: Split each line into event_number, description, left_event, right_event
            l=line.split("|")
            event_number = int(l[0])
            description=l[1]
            left_event=int(l[2])
            right_event=int(l[3])
    # TODO: Call game_tree.insert() for each event to build the tree
            game_tree.insert(event_number, description, left_event, right_event)

# Main program
if __name__ == "__main__":
    # print("TODO: Initialize the GameDecisionTree and load story data")
    game_tree = GameDecisionTree()

    # print("TODO: Load the story from 'story.txt'")
    load_story("story.txt", game_tree)

    # print("TODO: Start the RPG game")
    game_tree.play_game()
