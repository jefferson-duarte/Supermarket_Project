from dao import DaoSupplier
from database_files import supplier_txt
from model import Supplier


class ControllerSupplier:
    def register_supplier(self, name, cnpj, phone, category):
        dao_supplier = DaoSupplier.read()
        list_cnpj = list(filter(lambda x: x.cnpj == cnpj, dao_supplier))
        list_phone = list(filter(lambda x: x.phone == phone, dao_supplier))

        if len(list_cnpj) > 0:
            print(f'CNPJ "{cnpj}" already exist.')

        elif len(list_phone) > 0:
            print(f'Phone number "{phone}" already exist.')

        else:
            if len(cnpj) == 14 and len(phone) <= 11 and len(phone) >= 10:
                DaoSupplier.save(Supplier(name, cnpj, phone, category))
                print(f'Supplier "{name}" registed successufull.')
            else:
                print('Insert a CNPJ or phone valid.')

    def update_supplier(self, old_name, new_name, new_cnpj, new_phone, new_category):  # noqa:E501
        dao_supplier = DaoSupplier.read()

        list_name = list(filter(lambda x: x.name == old_name, dao_supplier))

        if len(list_name) > 0:
            list_cnpj = list(filter(lambda x: x.cnpj == new_cnpj, list_name))
            if len(list_cnpj) == 0:
                dao_supplier = list(
                    map(
                        lambda x: Supplier(
                            new_name, new_cnpj, new_phone, new_category
                        )
                        if (x.name == old_name)
                        else (x), dao_supplier
                    )
                )
            else:
                print(f'CNPJ "{new_cnpj}" already exist.')
        else:
            print(f'Supplier "{new_name}" does not exist.')

        with open(supplier_txt, 'w', encoding='utf-8') as file:
            for item in dao_supplier:
                file.writelines(f'{item.name}|{item.cnpj}|{item.phone}|{item.category}')  # noqa:E501
                file.writelines('\n')
            print(f'Supplier "{new_name}" updated successfully.')

    def show_suppiers(self):
        dao_supplier = DaoSupplier.read()

        if len(dao_supplier) == 0:
            print('Do not have any supplier.')

        for item in dao_supplier:
            print(f'{" SUPPLIER ":=^30}')
            print(
                f'Name......: {item.name}\n'
                f'Phone.....: {item.phone}\n'
                f'CNPJ......: {item.cnpj}\n'
                f'Category..: {item.category}\n'
            )
