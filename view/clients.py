from time import sleep

from controller.controller_client import ControllerClient
from utils import clean_screen


def client_view():
    client = ControllerClient()

    while True:
        clean_screen()
        print('=' * 35)
        print(f'{" Client ": ^35}')

        option_client = int(input(
            '===================================\n'
            '[1] Register a new client\n'
            '[2] Remove a client\n'
            '[3] Update a client\n'
            '[4] Show all clients\n'
            '[5] Exit\n'
            '===================================\n'
        ))

        match option_client:
            case 1:
                clean_screen()

                name = input('Input the client name: ')
                phone = input('Input the client phone: ')
                cpf = input('Input the client CPF: ')
                email = input('Input the client email: ')
                address = input('Input the client address: ')

                client.register_client(name, phone, cpf, email, address)
                sleep(5)

            case 2:
                clean_screen()

                name = input('Insert the name to remove: ')
                client.remove_client(name)
                sleep(5)

            case 3:
                clean_screen()

                old_name = input('Insert the name to change: ')
                new_name = input('Insert the new name: ')
                phone = input('Insert the phone: ')
                cpf = input('Insert the CPF: ')
                email = input('Insert the email: ')
                address = input('Insert the address: ')

                client.update_cliente(
                    old_name, new_name, phone, cpf, email, address
                )
                sleep(5)

            case 4:
                clean_screen()
                client.show_client()
                sleep(5)

            case 5:
                break
