import sys
clients = 'luis,juan,'
def create_client(client_name):
    global clients

    if client_name not in clients:                          
        clients += client_name                              
        _add_comma()
    else:                                                   
        print('Client is already in the client\'s list')    

def list_clients():   
    global clients
    print(clients)

def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', update_client_name + ',')
    else:
        print('Clients is not in clients list')

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients=clients.replace(client_name+',','')
    else:
        _not_in_list()

def search_client(client_name):
    client_list= clients.split(',')
    for client in client_list:
        if client != client_name:
            continue
        else:
            return True

def _add_comma():
    global clients
    clients += ','

def _get_client_name():
    clientName = None
    while not clientName:
        clientName = input('What\'s the client name? ')
        if clientName == "exit":
            sys.exit()


def _not_in_list():
    print('Client not in list')

def _print_welcome():
    print('WELCOME TO SALES')
    print('*'*50)
    print('What would like to do? ')
    
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

if __name__ == "__main__":
    _print_welcome()

    command = input()
    command= command.upper()
    if command == 'C':
        client_name= _get_client_name()
        create_client(client_name)
        list_clients()
    elif command=='L':
        list_clients()
    elif command=='U':
        client_name= _get_client_name()
        updated_name=input('Whats the new client name')  
        update_client(client_name,updated_name) 
        list_clients()
    elif command == 'D':
        client_name= _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'S':
        client_name= _get_client_name()
        found=search_client(client_name)
        if found:
            print('{} is in the clients list' .format(client_name))
        else:
            print('{} is NOT in the clients list'.format(client_name))
    else:
        print('Invalid command!! ')
        if __name__ == "__main__":
            pass