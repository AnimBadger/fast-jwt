from pydantic import BaseModel, EmailStr, Field


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)

    class Config:
        schema_extra = {
            "post_demo": {
                'title': 'some title',
                'content': 'some content'
            }
        }


class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema_extra = {
            'user_demo': {
                'name': 'Anim',
                'email': 'code@gmail.edu.gh',
                'password': '123'
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema_extra = {
            'user_demo': {
                'email': 'code@gmail.edu.gh',
                'password': '123'
            }
        }
