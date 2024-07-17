from django.db.models import CharField, Model, SlugField


class Categories(Model):
    name = CharField(max_length=150, unique=True)
    slug = SlugField(unique=True, blank=True, null=True)

    class Meta:
        db_table = 'category'
