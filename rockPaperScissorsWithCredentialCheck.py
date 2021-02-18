# rockPaperScissorsWithCredentialCheck

import random

# welcome message
print("----------------------------------------------------------------------------------------")
print("Hi there, my name is Rock-Paper-Scissor.\nMay I see your valid User ID and password, please?")
print("----------------------------------------------------------------------------------------")

# verifying user credentials
_id = input("User ID:\t")
if 'asterix_29' == _id.lower():
    b = input("Password:\t")
    print("----------------------------------------------------------------------------------------")
    print("Processing User ID...")
    print("Validating Password...")
    if 'pop12345xy' == b.lower():
        print("Hello,", _id)
        # rock-paper-scissor initialisation and rules
        global num
        how = input('how many matches do you want to play?\t')
        num = int(how)
        print("Rules for you:-\n'R' or 'r' for Rock\n'P' or 'p' for Paper\n'S' or 's' for Scissors")
        print("----------------------------------------------------------------------------------------")

        # player's input
        def play():
            user = input("So what's your choice?\n")
            user = user.lower()
            if (user != 'r') and (user != 's') and (user != 'p'):
                print('Something is wrong.\nPlease check the rules and give input accordingly.\n')
                print('ミ●﹏☉ミ')
                print("----------------------------------------------------------------------------------------")
                play()

            computer = random.choice(['r', 'p', 's'])

            if user == computer:
                return 0, user, computer

            # win: r > s, s > p, p > r
            elif is_win(user, computer):
                return 1, user, computer

            else:
                return -1, user, computer

        # satisfying winning conditions
        def is_win(player, opponent):
            # winning conditions: r > s, s > p, p > r
            if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
                    player == 'p' and opponent == 'r'):
                return True
            return False


        def play_best_of(num):
            # play against the computer until someone wins the most of num games
            player_wins = 0
            computer_wins = 0

            counter = 0
            while counter < num:
                result, user, computer = play()
                counter += 1
                # tie
                if result == 0:
                    print('You and I both have chosen {}.\nIts a tie.\n'.format(user))
                    print('(◔‿◔)')
                # you win
                elif result == 1:
                    player_wins += 1
                    print('You chose {} and I chose {}.\nCongrats, you won!!!\n'.format(user, computer))
                    print('( ⚈̥̥̥̥̥́⌢⚈̥̥̥̥̥̀)')
                else:
                    computer_wins += 1
                    print('You chose {} and I chose {}.\nWoohoo, I won. Better luck next time\n'.format(user, computer))
                    print('(✷‿✷)')
                print("----------------------------------------------------------------------------------------")

            if player_wins > computer_wins:
                print('You have won the most of {} games!\nYou are the new champion :D\n'.format(num))
                print(
                    '人(＾▽＾)人(＾▽＾)人(＾▽＾)人(＾▽＾)人(＾▽＾)人(＾▽＾)ﾉ\n     (＾▽＾)人(＾▽＾)人(＾▽＾)人(＾▽＾)人(＾▽＾)ﾉ\n         (＾▽＾)人(＾▽＾)人(＾▽＾)人(＾▽＾)ﾉ')
            elif player_wins == computer_wins:
                print('Wow!!\nIts a draw. Well played.\n')
                print("✌('ω')")
            else:
                print('I have won the most of {} games!\nYou played well. Better luck next time.\n'.format(num))
                print('💪( ͡👁️ ͜ʖ ͡👁️҂)')
            print("----------------------------------------------------------------------------------------")
            play_again()


        def play_again():
            play_ag = input("Wanna play again?\nType 'Y' or 'y' for Yes\nType 'N' or 'n' for No and exit\n\n")
            if play_ag.lower() == 'y':
                play()
            elif play_ag.lower() == 'n':
                return -1
            else:
                print('Something is wrong.\nTry again\n\n')
                play_again()


        # starting the game
        if __name__ == '__main__':
            play_best_of(num)

    # Forget Password Section
    else:
        print("Incorrect Password.")
        print("Sorry", _id + ", you're not allowd.")
        forget_password = input("forgot password?\nPress\n Y for YES\n N for NO\n")
        if forget_password.lower() == 'y':
            _mail = input("Please enter the registered e-mail address:")
            if _mail.lower() == 'pop.9bakp@gmail.com':
                print("----------------------------------------------------------------------------------------")
                print("User ID: asterix_29\nPassword: pop12345xy")
            else:
                print("Sorry", _id + ", your e-mail address does not match. You're not allowed.")
                print("----------------------------------------------------------------------------------------")
                print(
                    "                    !!!Attention!!!\nA security alert has been sent to the registered email address.\n              Thank you "
                    "for your support.")
        elif forget_password.lower() == 'n':
            print("See you soon,", _id)
        print("----------------------------------------------------------------------------------------")
else:
    print("----------------------------------------------------------------------------------------")
    print("Unauthorized User ID.")
    print("Sorry", _id + ", you're not allowed.")
    print("----------------------------------------------------------------------------------------")
