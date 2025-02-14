from random import shuffle, randint
from queue import Queue
import time
import random



class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {} # nodes
        self.friendships = {} # edges


    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        
        stretch: returning T/F to check for collisions
        include collision counter
        """
        if user_id == friend_id:
            return False #("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False #("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()


    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        ***for use with dense graphs***
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(self.last_id)
        
        # Create friendships
        # generate all possible friendships
        # create a list of possible friendships
        possible_friendships = []

        for user_id in self.users:
            # avoid duplicates
            # negate collisions using range(user_id +1, self.last_id +1)
            # quadratic O(n*2)
            for friend_id in range(user_id +1, self.last_id +1):
                possible_friendships.append((user_id, friend_id)) # creates a tuple

        # shuffle all possible friendships
        shuffle(possible_friendships)

        # create friendships for the first N pairs of list/set
        # N is determined by formula: num_users * avg_friendships // 2  # integer value
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            user_id =friendship[0]
            friend_id = friendship[1]
            self.add_friendship(user_id, friend_id)

    def populate_graph_linear(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        ***for use with sparse graphs***
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f'User {i+1}')
        
        # Create friendships
        # generate all possible friendships
        # create a list of possible friendships
        total_friendships = []
        collisions = 0
        target_friendships = (num_users * avg_friendships)

        # utilize random library
        while len(total_friendships) < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1
        
        print(f'COLLISIONS: {collisions}')


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # bft with path
        # create empty queue
        q = Queue()

        # enqueue first path
        q.enqueue([user_id])

        # while the queue is not empty
        while q.size() > 0:
            # dequeue the path
            path = q.dequeue()
            # get last item in path - set as
            # a variable
            # set a newuser_id to the last element in the path [-1]
            newuser_id = path[-1]
            # check if visited - if friend_id not in visited[newuser_id]:
            if newuser_id not in visited:    
                # set visited[newuser_id]=Path
                visited[newuser_id] = path
                # for each friend_id in friendships[newuser_id]:
                for friend_id in self.friendships[newuser_id]:  
                    # copy the Path as newPath
                    new_path = path.copy()
                    # append friend_id to newPath
                    new_path.append(friend_id)
                    # enqueue newPath
                    q.enqueue(new_path)
        # return populatedvisited dictionary to the caller
        return visited


if __name__ == '__main__':   
    num_users = 200
    avg_friendships = 100
    sg = SocialGraph()

    start_time = time.time()
    sg.populate_graph(num_users, avg_friendships)   
    end_time = time.time()
    print(f'Quadratic Runtime: {end_time - start_time} sec')
    
    
    start_time = time.time()
    sg.populate_graph_linear(num_users, avg_friendships)
    end_time = time.time()
    print(f'Linear Runtime: {end_time - start_time} sec')

    sg.populate_graph(10, 2) 
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)