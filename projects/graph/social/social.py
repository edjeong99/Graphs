import random
from queue import Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(f"User {i+1}")

        # Create friendships

        # below codes has time complexity of O(n^2)
        # possibleFriendships = []
        # for userID in self.users:
        #     for friendID in range(userID + 1, self.lastID + 1):
        #         possibleFriendships.append((userID, friendID))
        # random.shuffle(possibleFriendships)
        #print(possibleFriendships[:numUsers])
        # print(len(possibleFriendships))

        ## assign friendship based on possibleFriendships
        # for i in range(numUsers * avgFriendships // 2):
        #     self.addFriendship(
        #         possibleFriendships[i][0], possibleFriendships[i][1])
 
        # below code replace above commented code of O(n^2)
        # populate with time complexity O(n)
        count = 0

        while count < numUsers * avgFriendships // 2:
            #get 2 different random number
            num1 = random.randint(1,numUsers)
            num2 = num1
            while num1 == num2:
                num2 = random.randint(1,numUsers)
            # addFriendship return True if add was successful 
            # addFriend check if if num1, num2 is already friend
            if self.addFriendship(num1, num2):
                count += 1

       

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # initialize queue and visited
        q = Queue()
        for friend in self.friendships[userID]:
            q.enqueue(userID)  #for each userID, I enqueue friend
            q.enqueue(friend)

        visited[userID] = [userID]

        while q.size() > 0:
            # dequeue a userID and one of its friend
            current_userID = q.dequeue()
            current_user_friend = q.dequeue()
            
            # if current userID is not in visited, do stuff.
            if current_user_friend not in visited:
                
                # add current userID to and the path
                visited[current_user_friend] = visited[current_userID] +[current_user_friend]
                # enqueue friends of current userID
                for friend in self.friendships[current_user_friend]:
                    q.enqueue(current_user_friend)
                    q.enqueue(friend)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    #print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
    print(len(connections))
