from pydantic import BaseModel, Field

class UserLoginSchema(BaseModel):
    user: str = Field(default=None)
    pwd: str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo": {
                "user" : "nir",
                "pwd" : "ucode"
            }
        }
