from fastapi import FastAPI, Body, Depends
from app.model import PostSchema, UserLoginSchema, UserSchema
from app.auth.jwt_handler import sign_jwt
from app.auth.jwt_bearer import jwtBearer

app = FastAPI()

posts = [
    {
        'id': 1,
        'title': 'penguins',
        'content': 'Penguins are a group of aquatic flightless birds'
    },
    {
        'id': 2,
        'title': 'tigers',
        'content': 'Tigers are the largest living cat species'
    },
    {
        'id': 3,
        'title': 'koala',
        'content': 'Koalas can be mostly found in Australia'
    }
]

users = []


@app.get('/', tags=['test'])
def greet():
    return {'message': 'Hello world  '}


@app.get('/posts', dependencies=[Depends(jwtBearer())], tags=['posts'])
def get_posts():
    return {'data': posts}


@app.get('/posts/{id}', dependencies=[Depends(jwtBearer())], tags=['posts'])
def get_a_post(id: int):
    if id > len(posts):
        return {'error': "Post doesn't exist"}

    for post in posts:
        if post['id'] == id:
            return {'data': post}
        else:
            return {'error': "Post doesn't exist"}


@app.post('/posts', dependencies=[Depends(jwtBearer())], tags=['posts'])
def make_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {'message': 'successfully created'}


@app.post('/users/signup', tags=['users'])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user.dict())
    return sign_jwt(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        if user['email'] == data.email and user['password'] == data.password:
            return True
    return False


@app.post('/users/login', tags=['users'])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return sign_jwt(user.email)
    else:
        return {
            'error': 'Invalid Credentials'
        }
