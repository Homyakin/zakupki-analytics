import pymysql.connections
from pymysql.cursors import DictCursor
from typing import List, Dict

connection = pymysql.connections.Connection(
        host='localhost',
        user='root',
        password='12345',
        db='zakupki',
        charset='utf8mb4',
        cursorclass=DictCursor
    )


def get_emergency_contracts_by_regions() -> List[Dict]:
    sql = """SELECT COUNT(*) as count, region_name as region FROM zakupki.contract
                where emergency = 1
                group by region_name
                order by region_name;"""
    return execute(sql)


def get_emergency_contract_position_okpd2(count: int = 0) -> List[Dict]:
    sql = f"""SELECT * FROM (
                SELECT okpd2_code, okpd2_name, COUNT(*) as count FROM zakupki.contract_position WHERE guid in (
                    SELECT cp.guid FROM zakupki.contract c
                    INNER JOIN zakupki.position_to_contract ptc ON (c.guid = ptc.contract_guid)
                    INNER JOIN zakupki.contract_position cp ON (ptc.position_guid = cp.guid)
                    where c.emergency = 1
                    group by cp.guid
                )
                group by okpd2_code, okpd2_name
            ) as okpd2 WHERE count > {count};"""
    return execute(sql)


def execute(sql: str) -> List[Dict]:
    with connection.cursor() as cursor:
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(f"Enable to query {sql}", e)
    return []
