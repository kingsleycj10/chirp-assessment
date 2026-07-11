users = {}
posts = {}  

def create_user(username):
    """Register a new user."""

    username = username.strip().lower()

    if username == "":
        return {"ok": False, "error": "Username cannot be empty."}

    if username in users:
        return {"ok": False, "error": f"User '{username}' already exists."}

    users[username] = {"following": []}

    return {"ok": True, "user": username}



def create_post(username, text):
    """Create a new post."""

    username = username.strip().lower()
    text = text.strip()

    if username not in users:
        return {"ok": False, "error": f"User '{username}' does not exist."}

    if text == "":
        return {"ok": False, "error": "Post cannot be empty."}

    post_id = len(posts) + 1

    posts[post_id] = {"author": username, "text": text,"likes": 0}

    
    return {"ok": True, "post": {"id": post_id, **posts[post_id]}}


users = {"alice": {"following": ["bob", "kingsley"]},"bob": {"following": ["kingsley"]},"kingsley": {"following": []}}


def like_post(post_id):
    """Increase the like count of a post."""

    try:
        post_id = int(post_id)
    except (ValueError, TypeError):
        return {"ok": False, "error": "Post ID must be a number."}

    if post_id not in posts:
        return {"ok": False, "error": f"Post {post_id} not found."}

    posts[post_id]["likes"] += 1

    return {"ok": True, "post": {"id": post_id, **posts[post_id]}}

posts = {
    1: { "author": "alice","text": "My first post","likes": 0},
    2: {"author": "bob", "text": "Learning Python","likes": 0},
    3: {"author": "kingsley", "text": "My project","likes": 0}}


def follow(follower, followee):
    """Allow one user to follow another."""

    follower = follower.strip().lower()
    followee = followee.strip().lower()

    if follower not in users:
        return {"ok": False, "error": f"User '{follower}' does not exist."}

    if followee not in users:
        return {"ok": False, "error": f"User '{followee}' does not exist."}

    if follower == followee:
        return {"ok": False, "error": "You cannot follow yourself."}

    if followee not in users[follower]["following"]:
        users[follower]["following"].append(followee)

    return {"ok": True, "follower": follower, "following": users[follower]["following"]}


print(create_user("Alice"))
print(create_user("Bob"))
print(create_user("Kingsley"))


def get_profile(username):
    """Return a user's following list and their own posts."""
    username = username.strip().lower() if isinstance(username, str) else ""

    if username not in users:
        return {"ok": False, "error": f"user '{username}' does not exist"}

    own_posts = [{"id": pid, **post} for pid, post in posts.items() if post["author"] == username]

    return {"ok": True, "user": username, "following": users[username]["following"],"posts": own_posts,}

print(create_user("Xavi"))
print(create_user("Bosco"))
print(create_user("Kings"))



def get_feed(username):
    """Return posts from users this person follows."""

    username = username.strip().lower()

    if username not in users:
        return {"ok": False, "error": f"User '{username}' not found."}

    following = users[username]["following"]

    feed = []

    for post_id, post in posts.items():
        if post["author"] in following:
            feed.append({"id": post_id, **post})

    return {"ok": True, "feed": feed}

users = {"alice": {"following": ["bob", "kingsley"]},"bob": {"following": ["kingsley"]},"kingsley": {"following": []}}

posts = {
    1: { "author": "bob", "text": "Hello from Bob!","likes": 3},
    2: {"author": "kingsley", "text": "Learning Python!","likes": 5},
    3: { "author": "alice","text": "My first post!","likes": 1},
    4: {"author": "mary", "text": "Good morning!","likes": 2}}




def trending(n=5):

    """Return the top n most-liked posts."""

    ranking = []

    for post_id, post in posts.items():
        ranking.append((post["likes"], post_id))

    ranking.sort(reverse=True)

    trending_posts = []

    for likes, post_id in ranking[:n]:
        trending_posts.append({"id": post_id, **posts[post_id]})

    return {"ok": True, "trending": trending_posts,}


posts = {
    1: {"author": "alice","text": "Hello everyone!","likes": 10},

    2: {"author": "bob","text": "Python is amazing!","likes": 50},

    3: {"author": "kingsley","text": "Learning programming!","likes": 30},}




def unfollow(follower, followee):

    follower = follower.strip().lower()
    followee = followee.strip().lower()

    if follower not in users or followee not in users:
        return {"ok": False, "error": "One or both users do not exist."}

    if followee in users[follower]["following"]:
        users[follower]["following"].remove(followee)

    return {"ok": True, "following": users[follower]["following"]}

users = {"alice": {"following": ["bob", "kingsley"]},"bob": {"following": ["kingsley"]},"kingsley": {"following": []}}



def delete_post(post_id):

    try:
        post_id = int(post_id)
    except (ValueError, TypeError):
        return {"ok": False, "error": "Invalid post ID."}

    if post_id not in posts:
        return {"ok": False, "error": "Post not found."}

    del posts[post_id]

    return {"ok": True, "message": f"Post {post_id} deleted."}


post = {1: "My first post",2: "Learning Python",3: "My project"}


posts = {
    1: {"author": "alice","text": "I love Python programming","likes": 5},
    2: {"author": "bob","text": "Football is fun","likes": 2},
    3: {"author": "charlie", "text": "Python is awesome","likes": 7}}

def search(term):
    term = term.strip().lower() if isinstance(term, str) else ""

    if not term:
        return {"ok": False, "error": "search term cannot be empty"}

    matches = [ {"id": pid, **post}for pid, post in posts.items()if term in post["text"].lower()]

    return {"ok": True, "term": term, "results": matches}



print(create_user("Fab")) 
print(create_user("Kingsley"))        
print(create_user("   "))   

print(create_post("Alice", "Hello everyone!"))
print(create_post("Bob", "Python is fun!"))
print(create_post("John", "Hi!"))
print(create_post("Alice", "     "))

print(like_post(1))        # Valid post
print(like_post(1))        # Like it again
print(like_post("2"))      # String that can be converted to a number
print(like_post(10))       # Post doesn't exist
print(like_post("hello"))  # Invalid input  

print(follow("Alice", "Bob"))
print(follow("Alice", "Kingsley"))
print(follow("John", "Bob"))
print(follow("Alice", "Mary"))
print(follow("Alice", "Alice"))
print(follow("Alice", "Bob")) 

print("\nTest 1: Xavi follows Bosco")
print(follow("Xavi", "Bosco"))
print("\nTest 2: Xavi follows Kings")
print(follow("Alice", "Kings"))

print("Alice's feed:")
print(get_feed("Alice"))
print("\nBob's feed:")
print(get_feed("Bob"))
print("\nUnknown user:")
print(get_feed("John"))


print(trending())


print("Test 1: Alice unfollows Bob")
print(unfollow("Alice", "Bob"))
print("\nCurrent users:")
print(users)
print("\nTest 2: Unknown user")
print(unfollow("Mary", "Bob"))
print("\nTest 3: Alice unfollows Kingsley")
print(unfollow("Alice", "Kingsley"))
print("\nFinal users:")
print(users)


# Test 1: Delete an existing post
result = delete_post(2)
print(result)
print(posts)

# Test 2: Try deleting a post that does not exist
result = delete_post(99)
print(result)

# Test 3: Give an invalid ID
result = delete_post("hello")
print(result)

# Test 4: Give a string number
result = delete_post("3")
print(result)
print(posts)


print(search("python"))
print(search("PYTHON"))
print(search("   football   "))
print(search("java"))
print(search(""))