from pydantic import BaseModel


class actorRequestSchema(BaseModel):
    category: str
    name: str
    sku: str
    price: int
    image: str
    description: str
    description_long: str
    currency: str
    countInStock: int


class actorResponseSchema(actorRequestSchema):
    id: int

    class Config():
        orm_mode = True