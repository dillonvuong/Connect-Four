#Molly Taing 82155694 and Dillon Vuong 82352779 Lab 5 
from collections import namedtuple
import socket

ConnectFourConnection = namedtuple('ConnectFourConnection',
                                   ['socket','input','output'])

ConnectFourMove = namedtuple('ConnectFourMove', ['move', 'column'])

INVALID = 1
server_move = []
CONNECTION_FAILED = -1

def connect(host: str, port: int) -> ConnectFourConnection:
    '''
    Connects to a Polling server running on the given host and listening
    on the given port, returning a PollingConnection object describing
    that connection if successful, or raising an exception if the attempt
    to connect fails.
    '''
    try:
        connectfour_socket = socket.socket()
        connectfour_socket.connect((host, port))
        connectfour_input = connectfour_socket.makefile('r')
        connectfour_output = connectfour_socket.makefile('w')

        return ConnectFourConnection(
            socket = connectfour_socket,
            input = connectfour_input,
            output = connectfour_output)
    except socket.gaierror:
        return CONNECTION_FAILED
    except OSError:
        return CONNECTION_FAILED
    except TimeoutError:
        return CONNECTION_FAILED
        

    connectfour_input = connectfour_socket.makefile('r')
    connectfour_output = connectfour_socket.makefile('w')

    return ConnectFourConnection(
        socket = connectfour_socket,
        input = connectfour_input,
        output = connectfour_output)

def check_connection(connection: int) -> bool:
    'checks if the connection is valid or not'
    if connection == -1:
        return False
    else:
        return True

        

def hello(connection: ConnectFourConnection, username: str) -> bool:
    '''
    Logs a user into the ConnectFour service over a previously-made connection.
    and checks to see if the server is compatible.
    '''
    _write_line(connection, 'I32CFSP_HELLO '+ username)
    if _read_line(connection).startswith('WELCOME'):
        _write_line(connection, 'AI_GAME')
        return True
    else:
        return False
    
    
def move(connection: ConnectFourConnection, user_move: ConnectFourMove)-> server_move or INVALID:
    'Takes a user move and returns a move from the server'
    if user_move.move == 'd':
        _write_line(connection, "DROP " + user_move.column )
        s_move = _find_command(connection)

        if s_move == 1: # if server move is equal to INVALID
            return INVALID
        else:
            server_move = (s_move.split())
            return _convert(server_move)   
    else:
        _write_line(connection, "POP " + user_move.column)
        s_move = _find_command(connection)

        if s_move == 1:
            return INVALID
        else:
            server_move = (s_move.split())
            return _convert(server_move)
            
            


def close(connection: ConnectFourConnection) -> None:
    'Closes the connection to the Polling server'
    connection.input.close()
    connection.output.close()
    connection.socket.close()


def _convert(server_move: list) -> str:
    'converts server_move back into a string that will work with console/server modules'
    return f'{server_move[0][0].lower()}{server_move[1]}'            


def _find_command(connection: ConnectFourConnection) -> str or INVALID:
    'finds command drop pop or invalid'
    while True:
        f = _read_line(connection)
        if f.startswith('DROP'):
            return f
            
        elif f.startswith('POP'):
            return f
        
        elif f.startswith('INVALID'):
            return INVALID
            
        

def _read_line(connection: ConnectFourConnection) -> str:
    '''
    Reads a line of text sent from the server and returns it without
    a newline on the end of it
    '''
    line = connection.input.readline()[:-1]

    return line



def _write_line(connection: ConnectFourConnection, line: str) -> None:
    '''
    Writes a line of text to the server, including the appropriate
    newline sequence, and ensures that it is sent immediately.
    '''
    connection.output.write(line + '\r\n')
    connection.output.flush()

