from adress import Adress
from mailing import Mailing

to_adress = Adress("623400", "Каменск-Уральский", "Улица Каменская", "12", "24")

from_adress = Adress("620000", "Екатеринбург", "Улица Малышева", "19", "25")

mailing = Mailing(to_adress, from_adress, 500, "TRACK687159")
