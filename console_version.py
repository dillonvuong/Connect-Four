#Molly Taing 82155694 and Dillon Vuong 82352779 Lab 5 
import connectfour
import common_version

def run(state) -> int:
    'runs the function that plays the game'
    
    while connectfour.winner(state) == 0 and common_version.not_full(common_version.board(state)):
        print()
        common_version.turn(state.turn)
        choice = input()
        try:
            column = int(choice[1:]) - 1
            if choice[0] == 'd':
                common_version.print_board(common_version.board(connectfour.drop(state, column)))
                state = connectfour.drop(state, column)
            elif choice[0] == 'p':
                common_version.print_board(common_version.board(connectfour.pop(state, column)))
                state = connectfour.pop(state, column)
            else:
                print('Invalid Move: Please try again.')
                common_version.print_board(common_version.board(state))
        except connectfour.InvalidMoveError:
            print('Invalid Move: Please try again.')
            common_version.print_board(common_version.board(state))
        except IndexError:
            print('Invalid Move: Please try again.')
            common_version.print_board(common_version.board(state))
        except ValueError:
            print('Invalid Move: Please try again.')
            common_version.print_board(common_version.board(state))
    return connectfour.winner(state)


if __name__ == '__main__':

    common_version.welcome()

    state = connectfour.new_game()

    common_version.print_board(common_version.board(state))
    
    board_result = run(state)
    common_version.winner(board_result)

        
        
    
    
    
