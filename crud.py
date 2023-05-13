from connection import engine
from tables import users_table, posts_table
from sqlalchemy import (
    insert, 
    select,
    update,
    delete,
)

# adding user to the database 
def addUser(username, firstName, lastName):
    statement = insert(users_table).values(username=username, firstName=firstName, lastName=lastName)
    with engine.connect() as conn:
        conn.execute(statement)
        conn.commit()
        

# adding post to the database
def addPost(username, title, content):
    user_query = select(users_table).where(users_table.c.username == username)
    with engine.connect() as conn:
        user = conn.execute(user_query)
        if user is not None:
            statement = insert(posts_table).values(
                title=title, 
                content=content, 
                user=user.first().id
                )
            conn.execute(statement)
            conn.commit()


# get all posts 
def getAllPosts():
    statement = select(posts_table)
    with engine.connect() as conn:
        results = conn.execute(statement)
        for row in results:
            print(f"<Post {row.id}> title: {row.title}, content: {row.content}")
            


# updating user's information
def updateUser(id, username, firstName, lastName): 
    user_query = select(users_table).where(users_table.c.id==id)
    
    with engine.connect() as conn:
        result = conn.execute(user_query)
        if user_query is not None:
            statement = update(users_table).where(users_table.c.id == id).values(
            username = username if username is not None else result.first().username,
            firstName = firstName if firstName is not None else result.first().firstName,
            lastName = lastName if lastName is not None else result.first().lastName
            )
            conn.execute(statement)
            conn.commit()
            

# deleting post from database 
def deletePost(id):
       statement = delete(posts_table).where(posts_table.c.id==id)
       with engine.connect() as conn:
           if statement is not None:
               conn.execute(statement)    
               conn.commit() 


# below are examples: 
# addUser(username="lackson", firstName="Lackson", lastName="Munthali")
# addPost(username="lackson", title="Post Title", content="This is a description")
# getAllPosts()
# updateUser(id=1, username="Jane", firstName="Jane", lastName="Doe")
# deletePost(id=1)

