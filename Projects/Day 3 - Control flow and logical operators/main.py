print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_or_right = input('You see a fork in the road - there is a clear path on the left, and an overgrown path on the right.\n'
                      'Choose carefully - type "left" or "right"?!\n').lower()

if left_or_right=="left":
    print("\n------- You have chosen left ------\n")        
    swim_or_wait = input('\nYou encounter a beach - looking into the far distance you espy a volcanic island surrounded by smoke... \n'
                         'A boat approaches slowly on yonder horizon - which you could wait on to make the crossing\n'
                         'Type "swim" (to get to the island now asap!) or "wait" (for the boat)?\n\n').lower()
    if swim_or_wait=="wait":
        print("\n------- You have chosen to wait ------\n")
        print("\nAfter waiting for yonks, it turns out to be a pirate boat with skull and crossbones flag...\n"
              "Captained by Hook and Blackbeard, with a parrot on Blackbeard's shoulder glaring at you saying 'pollywannaattacker'\n"
              "The pirates take you hostage and sail onwards\n"
              "Just when you approach the island they tell you to walk off the plank into shark-infested waters, and go to steal your treasure map\n"
              "But the magic emitted from the area drifts into your consciousness..\n"
              "Allowing you to take control of Blackbeard's parrot - you peck at the pirate's faces - then escape off the boat heading into the island's foliage\n"
              "You can hear them screaming in bouts of agony and futile anger as you make your way through the mystical forest\n"
              "Suddenly you encounter a set of doors")
        which_door = input('Which door do you choose to open? Type "red" / "yellow" / "blue"?\n\n').lower()
        
        if which_door=="red":
            print("\n------- You have chosen the red door ------\n") 
            print("\nOh no homie! This red door leads into a deadly firepit\n")
            print(r'''
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣆⢳⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣾⣷⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠠⣄⠀⢠⣿⣿⣿⣿⡎⢻⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⢸⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣾⣿⣿⣿⣿⠃⠀⢸⣿⣿⣿⣿⣿⣿⠀⣄⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⠏⠀⠀⣸⣿⣿⣿⣿⣿⡿⢀⣿⡆⠀
    ⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⣿⣿⣿⣿⣿⣿⠇⣼⣿⣿⡄
    ⠀⢰⠀⠀⣴⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⢠⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⣧
    ⠀⣿⡀⢸⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⣸⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠀⣿⣷⣼⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⢹⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⡄⢻⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⠇
    ⢳⣌⢿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⠏⠀
    ⠀⢿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⠋⣠⠀
    ⠀⠈⢻⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣵⣿⠃⠀
    ⠀⠀⠀⠙⢿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠃⠀⠀
    ⠀⠀⠀⠀⠀⠙⢿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠋⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣦⣀⠀⠀⠀⠀⢀⣴⠿⠛⠁⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠓⠂⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        
        ''')
           
            print("Burned by fire\nGame over.")
            
        elif which_door=="yellow":
            print("\n------- You have chosen the yellow door ------\n") 
            print("\nYou open the yellow door\n"
              "To find yourself surrounded by palm trees and paradise\n"
              "A treasure chest emblazoned with a skull sits in the middle of an empty throne - with immeasurable riches to last a thousand lifetimes!\n"
              "Plus a magical teleportation crystal that allows you to travel wherever you would like!\n")
            
            print(r'''
                                      ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`

                  ''')
            
            print("You win! Time to live a life of great convenience and luxury!\n"
                  "Plus you help save the climate by avoiding any plane emissions - travelling around the world at the click of your magic crystal!")
            
            
        
        
        elif which_door=="blue":
            print("\n------- You have chosen the blue door ------\n") 
            print("\nRichard Attenborough drive towards you in a jeep doing doughnuts whilst spitting some scientific bars, whilst John Williams conducts an orchestra running behind him to keep up\n"
                  "'Welcome to Jurassic Park' announces Attenborough with a grin on his face - followed by panic as giant footsteps and screeches are heard\n")
            
            print(r'''
                                                                       ___._
                                                   .'  <0>'-.._
                                                  /  /.--.____")
                                                 |   \   __.-'~
                                                 |  :  -'/
                                                /:.  :.-'
__________                                     | : '. |
'--.____  '--------.______       _.----.-----./      :/
        '--.__            `'----/       '-.      __ :/
              '-.___           :           \   .'  )/
                    '---._           _.-'   ] /  _/
                         '-._      _/     _/ / _/
                             \_ .-'____.-'__< |  \___
                               <_______.\    \_\_---.7
                                 /'=r_.-'     _\\ =/
                          .--'   /            ._/'>
                        .'   _.-'
                       / .--'
                      /,/
                      /`)
                      'c=,
                      
                      
                                             __~a~_
                                ~~;  ~_
                  _                ~  ~_                _
                 '_\;__._._._._._._]   ~_._._._._._.__;/_`
                 '(/'/'/'/'|'|'|'| (    )|'|'|'|'\'\'\'\)'
                 (/ / / /, | | | |(/    \) | | | ,\ \ \ \)
                (/ / / / / | | | ~(/    \) ~ | | \ \ \ \ \)
               (/ / / / /  ~ ~ ~   (/  \)    ~ ~  \ \ \ \ \)
              (/ / / / ~          / (||)|          ~ \ \ \ \)
              ~ / / ~            M  /||\M             ~ \ \ ~
               ~ ~                  /||\                 ~ ~
                                   //||\\
                                   //||\\
                                   //||\\
                                   '/||\'


            ___                                      .-~. /_"-._
            `-._~-.                                  / /_ "~o\  :Y
                \  \                                / : \~x.  ` ')
                ]  Y                              /  |  Y< ~-.__j
                /   !                        _.--~T : l  l<  /.-~
                /   /                 ____.--~ .   ` l /~\ \<|Y
                /   /             .-~~"        /| .    ',-~\ \L|
            /   /             /     .^   \ Y~Y \.^>/l_   "--'
            /   Y           .-"(  .  l__  j_j l_/ /~_.-~    .
            Y    l          /    \  )    ~~~." / `/"~ / \.__/l_
            |     \     _.-"      ~-{__     l  :  l._Z~-.___.--~
            |      ~---~           /   ~~"---\_  ' __[>
            l  .                _.^   ___     _>-y~
            \  \     .      .-~   .-~   ~>--"  /
            \  ~---"            /     ./  _.-'
                "-.,_____.,_  _.--~\     _.-~
                            ~~     (   _}
                                    `. ~(
                                    )  \
                                    /,`--'~\--'

                  
                  ''')
            print("Oh boy - you are all eaten by dinosaurs!\nGame over.")
            
        else:
            print("\n------- You have not chosen a valid door ------\n")
            print("Game over - you chose to walk away from the doors, so you spontaneously combust")
        
    else:
        print("\n------- You have chosen swim or anything else------\n")
        print("Oh no! These are dangerous waters - you find yourself surrounded by the hyper-intelligent sharks from Deep Blue Sea...\n"
              "And they are starving!")
        print(r'''
        
        
                           /""-._
                          .      '-,
                          :         '',
                          ;      *     '.
                          ' *         () '.
                           \               \
                            \      _.---.._ '.
                             :  .' _.--''-''  \ ,'
               .._            '/.'             . ;
                ; `-.          ,                \'
                 ;   `,         ;              ._\
                  ;    \     _,-'                ''--._
                   :    \_,-'                          '-._
                    \ ,-'                       .          '-._
                   .'         __.-'';            \...,__       '.
                  .'      _,-'       \              \   ''--.,__ '\
                 /   _,--' ;          \             ;           "^.}
                ;_,-' )     \  )\      )            ;
                     /       \/  \_.,-'             ;
                    /                              ;
                 ,-'  _,-''                       ;' 
                ' _.-'      '-._...--''-._...--''
                       



                                          /\  
                                         /:|        
                                       ,'::|
                                      /::::|
                                    ,':::::\                                      _..
                 ____........-------,..:::  \                                  ,-' /
         _.--"""". . . .      .   .  .  .  ""`-._                           ,-' .;'
        <. - :::::o......  ...   . . .. . .  .  .""--._                  ,-'. .;'
         `-._  ` `":`:`:`::||||:::::::::::::::::.:. .  ""--._ ,'|     ,-'.  .;'
             """_=--       //'.... ````:`:`::::::::::.:.:.:. .`-`._-'.   .;'
                 ""--.__     (       \               ` ``:`:``:::: .   .;'
                        "\""--.:-.     `.                             .:/
                          \. /    `-._   `.""-----.,-..::(--"".\""`.  `:\
                           `         `-._ \          `-:\          `. `:\
                                           ""            "            `-._)



            ''')

        print("Just when you think things couldn't get any worse, a giant Cthulhu suddenly appears!")
        print(r'''
        
                             .-'   `'.
                            /         \
                            |         ;
                            |         |           ___.--,
                   _.._     |0) ~ (0) |    _.---'`__.-( (_.
            __.--'`_.. '.__.\    '--. \_.-' ,.--'`     `""`
           ( ,.--'`   ',__ /./;   ;, '.__.'`    __
           _`) )  .---.__.' / |   |\   \__..--""  """--.,_
          `---' .'.''-._.-'`_./  /\ '.  \ _.-~~~````~~~-._`-.__.'
                | |  .' _.-' |  |  \  \  '.               `~---`
                 \ \/ .'     \  \   '. '-._)lefrt
                 
                  \/ /        \  \    `=.__`~-.
                   / /\         `) )    / / `"".`\
            , _.-'.'\ \        / /    ( (     / /
             `--~`   ) )    .-'.'      '.'.  | (
                    (/`    ( (`          ) )  '-;
                     `      '-;         (-'

        ''')

        print("Game over son, sayonara")
        
    
else:
    print("\n------- You have chosen right or anything else------\n")            
    print("Oh no! You fall into a hole and get mauled by an army of bears")
    print(r'''
        _,-""""-._
        /           \
       |    DANGER   |
        \           /
         `-._   _.-'
             | |
          ___|_|___
         [_________]
             | |
             | |
             | |

        _   _     _   _     _   _     _   _     _   _
       ( ) ( )   ( ) ( )   ( ) ( )   ( ) ( )   ( ) ( )
      <_|___|_> <_|___|_> <_|___|_> <_|___|_> <_|___|_>
       |     |   |     |   |     |   |     |   |     |
       | O O |   | O O |   | O O |   | O O |   | O O |    <-- THE ARMY
       |  ^  |   |  ^  |   |  ^  |   |  ^  |   |  ^  |
        \_m_/     \_m_/     \_m_/     \_m_/     \_m_/

           \        \        |        /        /
            \        \       |       /        /


                >>> THEY ARE GETTING CLOSER <<<

                     _  / (HELP!)
                    ( )/
                   --+--
                    / \
                   /   \  <-- YOU
        ''')

    print("KO. Game over.")