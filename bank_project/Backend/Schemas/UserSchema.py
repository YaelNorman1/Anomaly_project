from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    user: str = Field(default=None)
    pwd: str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo": {
                "user" : "nir",
                "pwd" : "ucode"
            }
        }
