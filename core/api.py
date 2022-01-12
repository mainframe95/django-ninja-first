import datetime
from ninja import NinjaAPI
from ninja import Schema, Path

api = NinjaAPI()

class PathDate(Schema):
    year: int
    month: int
    day: int

    def value(self):
        return datetime.date(self.year, self.month, self.day)

# path requierd
@api.get("/events/{year}/{month}/{day}")
def events(request, date: PathDate = Path(...)):
    return {"date": date.value()}

weapons = ["Ninjato", "Shuriken", "Katana", "Kama", "Kunai", "Naginata", "Yari"]

# query string
@api.get("/weapons")
def list_weapons(request, limit: int = 10, offset: int = 0):
    return weapons[offset: offset + limit]

@api.get("/weapons/search")
def search_weapons(request, q: str, offset: int = 0):
    results = [w for w in weapons if q in w.lower()]
    print(q, results)
    return results[offset: offset + 10]

class Item(Schema):
    name: str
    description: str = None
    price: float
    quantity: int


@api.post("/items")
def create(request, item: Item):
    return item

@api.put("/items/{item_id}")
def update(request, item_id: int, item: Item):
    return {"item_id": item_id, "item": item.dict()}