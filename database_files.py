import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

category_txt = os.path.join(BASE_DIR, 'database/category.txt')
sell_txt = os.path.join(BASE_DIR, 'database/sell.txt')
stock_txt = os.path.join(BASE_DIR, 'database/stock.txt')
supplier_txt = os.path.join(BASE_DIR, 'database/supplier.txt')
customer_txt = os.path.join(BASE_DIR, 'database/customer.txt')
employee_txt = os.path.join(BASE_DIR, 'database/employee.txt')
