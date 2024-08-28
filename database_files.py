import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

category_txt = os.path.join(BASE_DIR, 'database/category.txt')
sell_txt = os.path.join(BASE_DIR, 'database/sell.txt')
stock_txt = os.path.join(BASE_DIR, 'database/stock.txt')
supplier_txt = os.path.join(BASE_DIR, 'database/supplier.txt')
customer_txt = os.path.join(BASE_DIR, 'database/customer.txt')
employee_txt = os.path.join(BASE_DIR, 'database/employee.txt')

list_files = [
    category_txt, sell_txt, stock_txt, supplier_txt, customer_txt, employee_txt
]


def create_files():
    for file_name in list_files:
        if not os.path.exists(file_name):
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write('')
