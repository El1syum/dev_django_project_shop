from django.db.models import CharField, Model, SlugField, TextField, ImageField, DecimalField, PositiveIntegerField, \
    ForeignKey, CASCADE


class Categories(Model):
    name = CharField(max_length=150, unique=True, verbose_name='Название категории')
    slug = SlugField(unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(Model):
    name = CharField(max_length=150, unique=True, verbose_name='Название')
    slug = SlugField(unique=True, blank=True, null=True, verbose_name='URL')
    description = TextField(blank=True, null=True, verbose_name='Описание')
    image = ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    quantity = PositiveIntegerField(default=0, verbose_name='Количество')
    category = ForeignKey(Categories, on_delete=CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['id']

    def __str__(self):
        return f'{self.name} - {self.quantity}'

    def display_id(self):
        return f'{self.id:05}'

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount/100, 2)

        return self.price
