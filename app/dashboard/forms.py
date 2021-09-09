from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DecimalField
from flask_babel import _, lazy_gettext as _l
from enum import Enum

# Categories in SelectField
class Categories(Enum):
    FOOD = _l('Продукты')
    ENTER = _l('Развлечения')
    TAX = _l('Налоги')
    TRAVELS = _l('Путешествия')
    PETS = _l('Питомцы')
    CLOTHES = _l('Одежда')
    TRANS = _l('Транспорт')
    MEDICINE = _l('Медицина')
    UNEXP = _l('Непредвиденные расходы')

    def __str__(self):
        return self.value

categories = [(y.name, _l(str(y.value))) for y in Categories]

# Form to add expence
class AddExpenceForm(FlaskForm):
    category_select = SelectField(choices=categories)
    product_name = StringField('Продукт', render_kw={"placeholder": _l('Продукт')})
    price_value = DecimalField('Цена', render_kw={"placeholder": _l('Цена')})
    submit = SubmitField(_l('Добавить'))


