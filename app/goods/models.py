from django.db.models import CharField, Model, SlugField


class Categories(Model):
    name = CharField(max_length=150, unique=True, verbose_name='Название категории')
    slug = SlugField(unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
