from enum import Enum
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class MusicBand(str, Enum):
   AEROSMITH = "AEROSMITH"
   QUEEN = "QUEEN"
   ACDC = "AC/DC"


class UserBase(BaseModel):
    name: str = Field(min_length=1, max_length=128)
    mobile : constr(regex="^09\d{9}$")
    address: str | None 
    age: int | None  