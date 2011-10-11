import uuid
from django.db import models

from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

class BaseModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tags = TaggableManager()
    
    def __unicode__(self):
        return self.name
    
    class Meta(object):
        abstract = True 

class AlphaModel(BaseModel):
    pass

class BetaModel(BaseModel):
    pass

class TaggedCharPkModel(TaggedItemBase):
    content_object = models.ForeignKey("CharPkModel")
    
class AnotherTaggedCharPkModel(TaggedItemBase):
    content_object = models.ForeignKey("AnotherCharPkModel")

class CharPkModel(models.Model):
    tags = TaggableManager(through=TaggedCharPkModel)

    id = models.CharField(max_length=32, primary_key=True,
            default=lambda:str(uuid.uuid4()).replace("-", ""))

class AnotherCharPkModel(models.Model):
    ttaaggss = TaggableManager(through=AnotherTaggedCharPkModel)

    id = models.CharField(max_length=32, primary_key=True,
            default=lambda:str(uuid.uuid4()).replace("-", ""))

