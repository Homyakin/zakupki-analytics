import database.queries
from utils.save import save_to_excel

data = database.queries.get_emergency_contract_position_okpd2(5)
print(data)
save_to_excel(data, 'okpd2.xlsx')
