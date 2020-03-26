
import os
import csv

clients =[]
CLIENT_TABLE='C:\\Users\\Inna\\Desktop\\platzi\\python\\samples\\CRUD\\.clients.csv'
CLIENT_SCHEMA= ['name','company','email', 'position']

def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f: #abrir el archivo en modo de lectura(read
        reader= csv.DictReader(f, fieldnames=CLIENT_SCHEMA) #
        for row in reader:
            clients.append(row)

def _save_clients_to_storage():
    tmp_table_name='{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer= csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
      
        writer.writerows(clients)
        f.close() 
        os.remove(CLIENT_TABLE) 
        os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(client):
    global clients #variable global y se puede usar dentro de la funcion
    if client not in clients:
        clients.append(client)
    else:
        _not_in_list()

def list_clients():
    print('uid |  Name  | Company  | Email  | Position ') # Encabezado
    print('='*50)  # Encabezado
    for idx, client in enumerate(clients):#enumeramos la lista pero con indice
        print('{uid} | {name} | {company} | {email} | {position}'.format(uid=idx,
        name=client['name'],
        company= client['company'],
        email=client['email'],
        position=client['position']))


def update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_name
    else:
        _not_in_list()

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        _not_in_list()


def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True




def _print_welcome():
    print('WELCOME TO SALES')
    print('*'*50)
    print('What would like to do? ')
    print('[L]ist clients')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')
    print('[S]earch client')


def _get_client_field(field_name):
    field = None

    while not field:
        field =  input('What\'s the client {} '. format(field_name))

    return field

def _get_client_name():
    client_name = None
    while not client_name:
        client_name= input ('What\'s client name: ')
        if client_name.lower() == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _not_in_list():
    print('Client not in list')


if __name__ == "__main__":
    _initialize_clients_from_storage()
    _print_welcome()

    command = input('')
    if command.lower() == 'c':
        client = {
            'name':_get_client_field('name'), 
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }
        create_client(client)
        list_clients()
    elif command.lower() == 'd':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif  command.lower() == 'u':
        client_name = _get_client_name()
        updated_client_name = input('What\'s the updated client name==> ')
        update_client(client_name, updated_client_name)
        list_clients()
    elif command.lower() == 's':
        client_name =_get_client_name()
        found = search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client : {}  is not in our client\'s list'.format(client_name))
    elif command.lower() == 'l':
        list_clients()
    else:
        print('Invalid command!! ')

    _save_clients_to_storage()