from pydantic import BaseModel


class actorRequestSchema(BaseModel):
    category: str
    name: str
    image_2: str
    image: str
    description: str
    description_long: str


class actorResponseSchema(actorRequestSchema):
    id: int

    class Config():
        orm_mode = True