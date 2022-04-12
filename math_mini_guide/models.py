from tortoise import fields, Model

from utils.reference import AbstractBaseModel, random_string, b64encode


class Area(AbstractBaseModel):
    pass


class Catalogue(AbstractBaseModel):
    area = fields.ForeignKeyField('models.Area', description="领域", related_name='catalogue')


class Article(AbstractBaseModel):
    name = fields.CharField(description="文章名", max_length=50)
    catalogue = fields.ForeignKeyField('models.Category', description="类目", related_name='article')
    area = fields.ForeignKeyField('models.Area', description="领域", related_name='article')
    body = fields.TextField(verbose_name="内容")


class WechatUser(Model):
    id = fields.IntField(pk=True)
    open_id = fields.CharField(description="OpenID", max_length=50, unique=True)
    signature = fields.CharField(description="签名", max_length=50, default=random_string())

    def token(self):
        return f"{b64encode(self.open_id)}.{b64encode(self.signature)}"
