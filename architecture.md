- # DB:
    - Tables:
        - User:
            - ID => UUID (Primary Key)
            - username => char(127)
            - PW => bcrypt hashing

        - Topic:
            - ID => UUID (Primary Key)
            - Owner => User.ID
            - Content => char(127)
            - Hash (to identify uniqueness)
            - TTL => LocalTimeDate().now()
            - Current comment number
            - Previous comment number
            - Total comment number

        - Comments:
            - ID => UUID (Primary Key)
            - Owner => User.ID
            - Topic => Topic.ID
            - Content => char(1023)
- # Functionality:
    - User:
        - Login:
            Enter username, password
        - Create an account:
            - Create a username (required=available),
            - Create a password
        - Create a topic:
            - Choose some topic (required=topic is unique, no duplicates exist)
            - Search for a topic
        - Comment:
            - Leave a comment under a topic (1023 long)

    - Topic:
        - All unique (Hash)
        - TTL (Time To Live (LocalTimeDate())):\
            When a topic is created, it sets its `ttl = LocalTimeDate().now() + 1 hour`, current comment number to 0. After 1 hour, system checks if there are new comments:
            * If there are new comments, then new TTL is set to `ttl += (totalCommentNumber - currentCommentNumber)` minutes, and `currentCommentNumber is set to (totalCommentNumber - currentCommentNumber)`.\
            * If there are no new comments, then whole 'Topic' is removed with the comments inside it.

