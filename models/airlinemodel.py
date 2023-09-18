from mongoengine import Document, StringField, BooleanField, URLField, DateTimeField


class Airlines(Document):
    name = StringField()
    code = StringField(unique=True)
    isLowCost = BooleanField()
    logo = URLField()
    createdAt = DateTimeField()
    updatedAt = DateTimeField()
