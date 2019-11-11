class Property:
    def __init__(self, id, title,
                 published_date=None, address=None, category=None, meters=None, floor=None, rooms=None, price=None):
        self.id = id
        self.title = title
        self.published_date = published_date
        self.address = address
        self.category = category
        self.meters = meters
        self.floor = floor
        self.rooms = rooms
        self.price = price

    def __repr__(self):
        return 'id: {}, title: {}'.format(self.id, self.title)

    def as_map(self):
        return {
            "id": self.id,
            "title": self.title,
            "published_date": self.published_date,
            "address": self.address,
            "category": self.category,
            "meters": self.meters,
            "floor": self.floor,
            "rooms": self.rooms,
            "price": self.price
        }
