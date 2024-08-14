from datetime import datetime


class Category:
    def __init__(self, category):
        self.category = category


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category


class Stock:
    def __init__(self, product: Product, quantity):
        self.product = product
        self.quantity = quantity


class Sell:
    def __init__(self, itens_sold: Product, seller, customer, quantity_sold, data=datetime.now()):  # noqa:E501
        self.itens_sold = itens_sold
        self.seller = seller
        self.customer = customer
        self.quantity_sold = quantity_sold
        self.data = data


class Supplier:
    def __init__(self, name, cnpj, phone, category):
        self.name = name
        self.cnpj = cnpj
        self.phone = phone
        self.category = category


class Person:
    def __init__(self, name, cpf, phone, email, address):
        self.name = name
        self.cpf = cpf
        self.phone = phone
        self.email = email
        self.address = address


class Employee(Person):
    def __init__(self, clt, name, cpf, phone, email, address):
        self.clt = clt
        # TODO:super(Employee, self).__init__(name, cpf, phone, email, address)

        super().__init__(name, cpf, phone, email, address)
