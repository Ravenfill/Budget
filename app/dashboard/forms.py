from flask_wtf import Form
from wtforms import StringField, SelectField, SubmitField, DecimalField

class AddExpenceForm(Form):
    category_select = SelectField(choices=['Продукты', 'Развлечения', 'Налоги', 'Путешествия', 'Животние', 'Одежда', 'Транспорт', 'Медицина', 'Непредвиденные расходы',])
    product_name = StringField('Продукт')
    price_value = DecimalField('Цена')
    submit = SubmitField('submit')