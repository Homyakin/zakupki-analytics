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
    with connection.cursor() as cursor:
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(f"Enable to query {sql}", e)
    return []
