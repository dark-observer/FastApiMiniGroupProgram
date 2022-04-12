import random
import string
import base64

from tortoise import fields, models


class AbstractBaseModel(models.Model):
    id = fields.IntField(pk=True)
    no = fields.IntField(description='序号', default=0)
    name = fields.CharField(max_length=30, description="名字")

    class Meta:
        abstract = True


def random_string(length=50):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))


def b64encode(message: str):
    return base64.b64encode(message.encode()).decode()


def b64decode(message: str):
    return base64.b64decode(message).decode()
