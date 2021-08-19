from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DecimalField
from flask_babel import lazy_gettext

class AddExpenceForm(FlaskForm):
    category_select = SelectField(choices=['Продукты', 'Развлечения', 'Налоги', 'Путешествия', 'Питомцы', 'Одежда', 'Транспорт', 'Медицина', 'Непредвиденные расходы',])
    product_name = StringField('Продукт', render_kw={"placeholder": lazy_gettext('Продукт')})
    price_value = DecimalField('Цена', render_kw={"placeholder": lazy_gettext('Цена')})
    submit = SubmitField('Добавить')