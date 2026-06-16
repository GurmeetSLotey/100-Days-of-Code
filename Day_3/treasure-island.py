print("""
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
      """)

print("Welcome to Treasue Island." \
"\nYour mission is to find the treasure.")

choice = input("You come at a cross road do you go Left or Right?\n")

if choice != 'left' and choice != 'l':
    print("The path turns dark as you adventure forward and boom you fall into a hole.")
    print("Game Over.")
    exit()

choice = input("You arrive at a lake do you swim or wait?\n")

if choice != 'wait' and choice != 'w':
    print("You find a swimsuit near by and change in the shed." \
    "\nYou jump into the lake and start swimming across when suddenly you are attacked by trouts.")
    print("Game Over.")
    exit()

choice = input("You wait at the lake." \
"\nA few minutes pass by when three doors suddenly appears infront of you." \
"\nRed, Yellow & Blue." \
"\nWhich door do you choose?")

if choice == 'Red' or choice == 'r':
    print('As you walk up to the red door and grab the handle, your body catches on fire.'
    '\nGame Over.')
    exit()
elif choice == 'Blue' or choice == 'b':
    print("You walk up to the blue door and open it.\n" \
    "You see a forrest and walk through.\n" \
    "As soon as you pass through fully the door shuts behind you are attacked by wild beasts.\n" \
    "Game Over.")
    exit()
elif choice == 'Yellow' or choice == 'y':
    print("Congratulations!!!\n" \
    "You Win!")
else:
    print("Game Over.")
    exit()
    