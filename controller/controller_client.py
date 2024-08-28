from dao import DaoPerson
from database_files import customer_txt
from model import Person


class ControllerClient:
    def register_client(self, name, phone, cpf, email, address):
        dao_person = DaoPerson.read()
        list_cpf = list(filter(lambda x: x.cpf == cpf, dao_person))

        if len(list_cpf) > 0:
            print(f'CPF "{cpf}" already exist.')
        else:
            if len(cpf) == 11 and len(phone) >= 10 and len(phone) <= 11:
                DaoPerson.save(Person(name, phone, cpf, email, address))
                print(f'Client "{name}" registed successfully.')
            else:
                print('Inser a cpf or phone valid.')

    def update_cliente(self, old_name, new_name, new_phone, new_cpf, new_email, new_address):  # noqa:E501
        dao_person = DaoPerson.read()

        list_name = list(filter(lambda x: x.name == old_name, dao_person))
        if len(list_name) > 0:
            dao_person = list(
                map(
                    lambda x: Person(new_name, new_phone, new_cpf, new_email, new_address)  # noqa:E501
                    if (x.name == old_name)
                    else (x), dao_person
                )
            )
            print(f'Client "{old_name}" updated successfully.')
        else:
            print(f'Client "{old_name}" does not exist.')

        with open(customer_txt, 'w', encoding='utf-8') as file:
            for item in dao_person:
                file.writelines(
                    f'{item.name}|{item.phone}|{item.cpf}|{item.email}|'
                    f'{item.address}'
                )
                file.writelines('\n')

    def remove_client(self, name):
        dao_person = DaoPerson.read()

        list_name = list(filter(lambda x: x.name == name, dao_person))
        if len(list_name) > 0:
            for index in range(len(dao_person)):
                if dao_person[index].name == name:
                    print(f'Client "{name}" removed successfully.')
                    del dao_person[index]
                    break

        else:
            print(f'Client "{name}" does not exist.')
            return None

        with open(customer_txt, 'w', encoding='utf-8') as file:
            for item in dao_person:
                file.writelines(
                    f'{item.name}|{item.phone}|{item.cpf}|{item.email}|'
                    f'{item.address}'
                )
                file.writelines('\n')

    def show_client(self):
        dao_person = DaoPerson.read()

        if len(dao_person) == 0:
            print('Does not have any clients.')

        for item in dao_person:
            print(f'{" Client ":=^30}')
            print(
                f'Name.....: {item.name}\n'
                f'Phone....: {item.phone}\n'
                f'Address..: {item.address}\n'
                f'Email....: {item.email}\n'
                f'CPF......: {item.cpf}\n'
            )
