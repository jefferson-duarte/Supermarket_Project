from database_files import (category_txt, customer_txt, employee_txt, sell_txt,
                            stock_txt, supplier_txt)
from model import Category, Employee, Person, Product, Sell, Stock, Supplier


class DaoCategory:
    @classmethod
    def save(cls, category):
        with open(category_txt, 'a', encoding='utf-8') as file:
            file.writelines(category)
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open(category_txt, 'r', encoding='utf-8') as file:
            cls.category = file.readlines()

        cls.category = list(map(lambda x: x.replace('\n', ''), cls.category))

        list_categories = []
        for item in cls.category:
            list_categories.append(Category(item))

        return list_categories


class DaoSell:
    @classmethod
    def save(cls, sell: Sell):
        with open(sell_txt, 'a', encoding='utf-8') as file:
            file.writelines(
                f'{sell.itens_sold.name}|{sell.itens_sold.price}|'
                f'{sell.itens_sold.category}|{sell.seller}|'
                f'{sell.customer}|{sell.quantity_sold}|{sell.data}'
            )
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open(sell_txt, 'r', encoding='utf-8') as file:
            cls.sell = file.readlines()

        cls.sell = list(map(lambda x: x.replace('\n', ''), cls.sell))
        cls.sell = list(map(lambda x: x.split('|'), cls.sell))

        list_sell = []
        for item in cls.sell:
            list_sell.append(
                Sell(
                    Product(item[0], item[1], item[2]),
                    item[3], item[4], item[5], item[6]
                )
            )

        return list_sell


class DaoStock:
    @classmethod
    def save(cls, product: Product, quantity):
        with open(stock_txt, 'a', encoding='utf-8') as file:
            file.writelines(
                f'{product.name}|{product.price}|{product.category}|'
                f'{quantity}'
            )
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open(stock_txt, 'r', encoding='utf-8') as file:
            cls.stock = file.readlines()

        cls.stock = list(map(lambda x: x.replace('\n', ''), cls.stock))
        cls.stock = list(map(lambda x: x.split('|'), cls.stock))

        list_stock = []
        if len(cls.stock) > 0:
            for item in cls.stock:
                list_stock.append(
                    Stock(
                        Product(item[0], item[1], item[2]),
                        item[3]
                    )
                )
        return list_stock


class DaoSupplier:
    @classmethod
    def save(cls, supplier: Supplier):
        with open(supplier_txt, 'a', encoding='utf-8') as file:
            file.writelines(
                f'{supplier.name}|{supplier.cnpj}|{supplier.phone}|'
                f'{supplier.category}'
            )
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open(supplier_txt, 'r', encoding='utf-8') as file:
            cls.supplier = file.readlines()

        cls.supplier = list(map(lambda x: x.replace('\n', ''), cls.supplier))
        cls.supplier = list(map(lambda x: x.split('|'), cls.supplier))

        list_supplier = []

        for item in cls.supplier:
            list_supplier.append(Supplier(item[0], item[1], item[2], item[3]))

        return list_supplier


class DaoPerson:
    @classmethod
    def save(cls, person: Person):
        with open(customer_txt, 'a', encoding='utf-8') as file:
            file.writelines(
                f'{person.name}|{person.phone}|{person.cpf}|'
                f'{person.email}|{person.address}'
            )
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open(customer_txt, 'r', encoding='utf-8') as file:
            cls.customer = file.readlines()

        cls.customer = list(map(lambda x: x.replace('\n', ''), cls.customer))
        cls.customer = list(map(lambda x: x.split('|'), cls.customer))

        list_customer = []
        for item in cls.customer:
            list_customer.append(
                Person(item[0], item[1], item[2], item[3], item[4])
            )

        return list_customer


class DaoEmployee:
    @classmethod
    def save(cls, employee: Employee):
        with open(employee_txt, 'a', encoding='utf-8') as file:
            file.writelines(
                f'{employee.clt}|{employee.name}|{employee.phone}|'
                f'{employee.cpf}|{employee.email}|{employee.address}'
            )
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open(employee_txt, 'r', encoding='utf-8') as file:
            cls.employee = file.readlines()

        cls.employee = list(map(lambda x: x.replace('\n', ''), cls.employee))
        cls.employee = list(map(lambda x: x.split('|'), cls.employee))

        list_employee = []
        for item in cls.employee:
            list_employee.append(
                Employee(item[0], item[1], item[2], item[3], item[4], item[5])
            )

        return list_employee
