from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DecimalField

class AddExpenceForm(FlaskForm):
    category_select = SelectField(choices=['Продукты', 'Развлечения', 'Налоги', 'Путешествия', 'Питомцы', 'Одежда', 'Транспорт', 'Медицина', 'Непредвиденные расходы',])
    product_name = StringField('Продукт')
    price_value = DecimalField('Цена')
    submit = SubmitField('Добавить')