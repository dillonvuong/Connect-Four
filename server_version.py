#Molly Taing 82155694 and Dillon Vuong 82352779 Lab 5 
import socket_handling
import common_version
import connectfour


def _run_ui() -> 'State of the board when game ends' or 'False if connection fails':
    'runs the user interface in order to play connect four with the server'
    host = _ask_for_host()
    port = _ask_for_port()
    print('Connecting...')
    connection = socket_handling.connect(host, port)
    
    if socket_handling.check_connection(connection): 
        print('Connected!')
        print()
        if socket_handling.hello(connection, _ask_for_username()):

            common_version.welcome()

            state = connectfour.new_game()# keep renewing this to the current state

            common_version.print_board(common_version.board(state))

            while connectfour.winner(state) == 0  and common_version.not_full(common_version.board(state)):
                print()
                common_version.turn(state.turn)
                try:
                    if state.turn == 1:
                        choice = input()
                        column = int(choice[1]) - 1
                        if choice[0] == 'd' and len(choice) == 2:
                            common_version.print_board(common_version.board(connectfour.drop(state, column)))
                            state = connectfour.drop(state, column)
                        elif choice[0] == 'p' and len(choice) == 2:
                            common_version.print_board(common_version.board(connectfour.pop(state, column)))
                            state = connectfour.pop(state, column)
                        else:
                            print('Invalid Move: Please try again.')
                            common_version.print_board(common_version.board(state))
                        user_move = socket_handling.ConnectFourMove(choice[0], str(column + 1))
                        
                    else:
                        server_move = socket_handling.move(connection, user_move)
                        server_column = int(server_move[1]) - 1
                        print(server_move)
                        
                        if server_move[0] == 'd':
                            common_version.print_board(common_version.board(connectfour.drop(state, server_column)))
                            state = connectfour.drop(state, server_column)
                        else:
                            common_version.print_board(common_version.board(connectfour.pop(state, server_column)))
                            state = connectfour.pop(state, server_column)
                            
                except connectfour.InvalidMoveError:
                    print('Invalid Move: Please try again.')
                    common_version.print_board(common_version.board(state))
                except IndexError:
                    print('Invalid Move: Please try again.')
                    common_version.print_board(common_version.board(state))
                except ValueError:
                    print('Invalid Move: Please try again.')
                    common_version.print_board(common_version.board(state))   

            socket_handling.close(connection)
            return connectfour.winner(state)
        else:
            print('That server is not compatible with this program. Ending connection...')
            return False
    else:
        print('Connection failed! Host/Port not valid. Ending program...')
        return False
        
    

    
        
def _ask_for_username()-> str:
    'asks for the user to enter a username and returns it as a string'
    while True:
        username = input('Please enter a username: ').strip()
        
        if len(username) > 0 and ' ' not in username:
            return username 
        else:
            print('That username is blank or contains white space; please try again.')
            
def _ask_for_host() -> str:
    'asks for the user to enter a host'
    while True:
        host = input('Please enter a valid host: ')

        if len(host) > 0:
            return host.strip()
        else:
            print('That host is blank;  please try again.')
            
def _ask_for_port() -> str:
    'asks the user to enter a port.'
    while True:
        try:
            port = int(input('Please enter a valid port: '))
            if port in range(0, 65536):
                return int(port)
            else:
                print('That port is invalid (not in the range 0 to 65535); please try again')
        except ValueError:
            print('That port is not a number; please try again.')
            

            

if __name__ == '__main__':
    board_result = _run_ui()
    if board_result != False:
        common_version.winner(board_result)


            



    




