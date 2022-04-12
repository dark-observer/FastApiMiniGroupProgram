from tortoise import fields, models


class AbstractBaseModel(models.Model):
    id = fields.IntField(pk=True)

    class Meta:
        abstract = True
