import json


class Contact:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    @property
    def full_name(self):
        return ("{} {}".format(self.first, self.last))


class ContactEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Contact):
            return {
                "is_contact": True,
                "first": obj.first,
                "last": obj.last,
                "full": obj.full_name,
            }
        return super().default(obj)


def decode_contact(dic):
    if dic.get("is_contact"):
        return Contact(dic["first"], dic["last"])
    else:
        return dic


c = Contact("Jhon", "Smith")
json.dumps(c.__dict__)  # '{"last": "Smith", "first": "Jhon"}'

json.dumps(c, cls=ContactEncoder)   # '{"is_contact": true, "last": "Smith",
# "full": "John Smith", "first": "John"}'

data = json.dumps(c, cls=ContactEncoder)
dumped_contact = json.loads(data, object_hook=decode_contact)
c  # <__main__.Contact object ... >
c.full_name  # 'john smith'

