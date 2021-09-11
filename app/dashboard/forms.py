from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DecimalField
from flask_babel import _, lazy_gettext as _l
from enum import Enum

# Categories in SelectField
class Categories(Enum):
    FOOD = _l("Food & Drinks")
    HOUSE = _l("Housing")
    ENTER = _l("Entertainment")
    TAX = _l("Tax")
    TRAVELS = _l("Travels")
    PETS = _l("Pets")
    SHOPPING = _l("Shopping")
    TRANSPORT = _l("Transportation")
    MEDICINE = _l("Medicine")
    SUPPLIES = _l("Supplies")
    VEHICLE = _l("Vehicle")
    COMMUNIC = _l("Communication")
    INVESTMENT = _l("Investments")
    INCOME = _l("Income")
    OTHER = _l("Other")

    def __str__(self):
        return self.value

categories = [(y.name, _l(str(y.value))) for y in Categories]

# Form to add expence
class AddExpenceForm(FlaskForm):
    tr_type = SelectField(choices=[('Income', _l('Income')), ('Expense', _l('Expence'))])
    category_select = SelectField(choices=categories)
    amount = DecimalField('Amount', render_kw={"placeholder": _l('Amount')})
    submit = SubmitField(_l('Добавить'))