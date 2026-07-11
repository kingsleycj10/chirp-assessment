Name:Okechukwu Kingsley.C.

APP-2025-22768



ChirpApp is built using several Python functions that handle user management, post interactions, and social networking features.



\# User Functions



\# `create\_user(username)`

Creates a new user account and adds the user to the system. It validates usernames, prevents duplicates, and stores user information.



\# `get\_profile(username)`

Retrieves a user's profile information, including their following list and posts they have created.







\# Post Functions



\# `create\_post(username, text)`

Allows a user to create a new post. It checks that the user exists and that the post content is not empty.



\# `delete\_post(post\_id)`

Removes a post from the system using its unique post ID.



\# `like\_post(post\_id)`

Increases the like count of a specific post and returns the updated post information.







\# Social Connection Functions



\#`follow(follower, followee)`

Allows one user to follow another user while validating that both users exist and preventing self-following.



\# `unfollow(follower, followee)`

Removes a user from another user's following list.





\# Feed \& Discovery Functions



\#`get\_feed(username)`

Generates a personalized feed by displaying posts from users that the selected user follows.



\# `trending(n=5)`

Returns the most liked posts based on popularity and displays the top trending content.



\# `search(term)`

Searches through posts using keywords and returns matching results.



\---



\#



ChirpApp contains functions that simulate the backend logic of a social media platform, including account creation, content sharing, user connections, engagement tracking, and content discovery.

```



