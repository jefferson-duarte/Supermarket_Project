from dao import DaoEmployee
from database_files import employee_txt
from model import Employee


class ControllerEmployee:
    def register_employee(self, clt, name, phone, cpf, email, address):
        dao_employee = DaoEmployee.read()

        list_cpf = list(filter(lambda x: x.cpf == cpf, dao_employee))
        list_clt = list(filter(lambda x: x.clt == clt, dao_employee))

        if len(list_cpf) > 0:
            print(f'CPF "{cpf}" already exist.')

        elif len(list_clt) > 0:
            print(f'CLT "{clt}" already exist.')

        else:
            if len(cpf) == 11 and len(phone) >= 10 and len(phone) <= 11:
                DaoEmployee.save(
                    Employee(clt, name, phone, cpf, email, address)
                )
                print(f'Employee "{name}" registed successfully.')
            else:
                print('Insert a CPF or Phone valid.')

    def update_employee(self, old_name, new_clt, new_name, new_phone, new_cpf, new_email, new_address):  # noqa:E501
        dao_employee = DaoEmployee.read()

        filter_name = list(filter(lambda x: x.name == old_name, dao_employee))
        if len(filter_name) > 0:
            dao_employee = list(
                map(
                    lambda x: Employee(new_clt, new_name, new_cpf, new_phone, new_email, new_address)  # noqa:E501
                    if (x.name == old_name)
                    else (x), dao_employee
                )
            )
        else:
            print(f'Employee "{old_name}" does not exist.')

        with open(employee_txt, 'w', encoding='utf-8') as file:
            for item in dao_employee:
                file.writelines(
                    f'{item.clt}|{item.name}|{item.phone}|'
                    f'{item.cpf}|{item.email}|{item.address}'
                )
                file.writelines('\n')
            print(f'Employee "{new_name}" updated successfully.')

    def remove_employee(self, name):
        dao_employee = DaoEmployee.read()

        list_name = list(filter(lambda x: x.name == name, dao_employee))
        if len(list_name) > 0:
            for item in range(len(dao_employee)):
                if dao_employee[item].name == name:
                    del dao_employee[item]
                    break

        else:
            print(f'Employee "{name}" does not exist.')

        with open(employee_txt, 'w', encoding='utf-8') as file:
            for item in dao_employee:
                file.writelines(
                    f'{item.name}|{item.phone}|{item.cpf}|'
                    f'{item.email}|{item.address}'
                )
                file.writelines('\n')
            print(f'Employee "{name}" removed successfully.')

    def show_employee(self):
        dao_employee = DaoEmployee.read()

        if len(dao_employee) == 0:
            print('Do not have any employee to show.')

        for item in dao_employee:
            print(f'{" Employee ":=^30}')
            print(
                f'Name.....: {item.name}\n'
                f'Phone....: {item.phone}\n'
                f'Emial....: {item.email}\n'
                f'Address..: {item.address}\n'
                f'CPF......: {item.cpf}\n'
                f'CLT......: {item.clt}\n'
            )
