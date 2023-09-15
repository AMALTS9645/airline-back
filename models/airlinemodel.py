from mongoengine import Document, StringField, BooleanField, URLField


class Airlines(Document):
    name = StringField()
    code = StringField(unique=True)
    isLowCost = BooleanField()
    logo = URLField()
