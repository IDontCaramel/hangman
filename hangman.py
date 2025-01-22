import random
from words import wordlist
import os
import time
from pystyle import Add
from pystyle import Colors, Colorate
from pystyle import Write, Colors


# Het scherm wordt leeggemaakt (Windows-specifiek commando)
os.system('cls')

# Een lijst voor geraden letters
geraden = []

# Aantal pogingen dat de speler mag raden 
tries = 0

# Scores voor de speler en de computer
u_score = 0
comp_score = 0

# Deze functie initialiseert het startmenu van het spel
def startup(u_score, comp_score):
    os.system("cls")

    # Het spel wordt gereset
    reset_game()

    # Startmenu wordt weergegeven
    print(hangman_visual)
    print("Welkom bij galgje! Welke gamemode wil je kiezen?")
    print("#############################################################################")
    print(score_visual)
    print(Add.Add(you_visual , allnums(u_score)))
    print(Add.Add(computer_visual, allnums(comp_score)))
    print("#############################################################################")
    print(Colorate.Vertical(Colors.purple_to_blue,'''
1. normaal galgje
2. twee speler galgje
3. eigen woord galgje
4. voeg een woord toe
5. regels
6. exit
7. author

'''))
    print("#############################################################################")


    # De gebruiker wordt gevraagd of ze willen beginnen
    user_input = input("wat will je gaan doen: ")
    woord = get_word()

    if user_input in ["1", "normaal", "one", "een"]:
        # Een willekeurig woord wordt gekozen
        awnser = ""
        hangman(awnser, woord)

    elif user_input in ["2", "multi", "twee", "two", "twee speler galgje"]:
        hangman_multiplayer()

    elif user_input in ["3", "drie", "eigen woord galgje"]:
        eigen_woord_hangman(awnser="")

                            
    elif user_input in ["4", "vier", "voeg een woord toe", "add"]:
        add_word_list()
        
    elif user_input in ["5", "regels", "vijf"]:
        os.system("cls")
        print('''
###################################################################################
REGELS:
het doel van het spel is om het woord te raden
je kan dit doen door elke keer een letter te raden
als je het woord denkt te weten dan kun je een heel woord raden
je kan zien welke letters je al geraden hebt en welke letters je goed hebt geraden
###################################################################################           
        ''')
        input("press enter to continue:")
        startup(u_score, comp_score)
    elif user_input in ["6", "exit", "zes"]:
        os.system("cls")
        exit()
    
    elif user_input in ["7", "author"]:
        author()
    
    elif user_input in ["monke", "Monke"]:
        monke()
        
    else:
        os.system("cls")
        print("u had", user_input, "ingevoerd")
        print("Kies een geldige optie.")
        time.sleep(1)
        startup(u_score, comp_score)

# Deze functie kiest een willekeurig woord uit de lijst met woorden (words.py)
def get_word():
    word = str(random.choice(wordlist))
    return word.lower()

# Deze functie verzorgt de normale versie van het galgje-spel
def hangman(awnser, woord):
    global hint

    os.system("cls")

    if tries == 6:
        # Speler heeft zes keer fout geraden, spel is voorbij
        game_over()

    else:
        # Spel is nog niet voorbij, de huidige status van het spel wordt weergegeven
        print(hanged(tries))
        print("Woord:", hint(woord, geraden))
        print("###############################################")
        print("Geraden:", *geraden)
        if awnser == "":
            print("Je hebt nog niets geraden.")
        else:
            print(*awnser)
        print("###############################################")
        guess = str(input("Welke letter wil je raden: "))
        
        if (guess.isalpha()) == True:
            # De ingevoerde tekst bevat alleen letters
                
            if guess == woord:
                # Als de speler het hele woord raadt, wint de speler
                game_win()

            else:
                # De speler heeft het woord nog niet geraden, de gok wordt gecontroleerd
                in_word(guess.lower(), woord)

        else:
            # De ingevoerde tekst bevat iets anders dan letters
            os.system('cls')
            print("Alleen letters zijn toegestaan.")
            time.sleep(2)
            hangman(awnser, woord)
            
def eigen_woord_hangman(awnser):
    global hint
    
    os.system("cls")

    woord = input("welk woord wil je gebruiken: ")
    
    woord = woord.lower()
    
    if (woord.isalpha()) == True:
        
        os.system("cls")

        if tries == 6:
            # Speler heeft zes keer fout geraden, spel is voorbij
            game_over()
            
        else:
            # Spel is nog niet voorbij, de huidige status van het spel wordt weergegeven
            print(hanged(tries))
            print("Woord:", hint(woord, geraden))
            print("###############################################")
            print("Geraden:", *geraden)
            if awnser == "":
                print("Je hebt nog niets geraden.")
            else:
                print(*awnser)
            print("###############################################")
            
            guess = str(input("Welke letter wil je raden: "))
            
            if (guess.isalpha()) == True:
                # De ingevoerde tekst bevat alleen letters
                
                if guess == woord:
                    # Als de speler het hele woord raadt, wint de speler
                    game_win()
                    
                else:
                    # De speler heeft het woord nog niet geraden, de gok wordt gecontroleerd
                    in_word(guess.lower(), woord)

            else:
                # De ingevoerde tekst bevat iets anders dan letters
                os.system('cls')
                print("Alleen letters zijn toegestaan.")
                time.sleep(2)
                hangman(awnser, woord)
    else:
        os.system("cls")
        print(woord)
        print("het woord dat je hebt ingevuled is ongeldig probeer opnieuw")
        time.sleep(1)
        eigen_woord_hangman(awnser)


player1_woord = ""
player2_woord = ""

player1_tries = 0
player2_tries = 0

player1_guess = ""
player2_guess = ""

player1_geraden = []
player2_geraden = []

beurt = 1 

def hangman_multiplayer():
    global player1_woord
    global player2_woord
    
    os.system("cls")
    print('''welkom bij multiplayer galgje
REGELS:
bijde spelers vullen een woord in die de andere speler moet raden
de persoon die als eerste het woord heeft geraden heeft gewonnen
veel succes en niet afkijken he ;)
''')
    input("press enter to continue")
    
    os.system("cls")
    print("player1")
    player1_woord = input("welk woord kies je: ")
    os.system("cls")
    print("player2")
    player2_woord = input("welk woord kies je: ") 
    player1()  
             
def player1():
    os.system("cls")
    global player1_guess
    
    if beurt == 1:
        
        print("player1")
        print(hanged(player1_tries))
        print("woord:", multiplayer_hint(player2_woord, player1_geraden))
        print("###############################################")
        print("geraden:", *player1_geraden)
        if player1_guess == "":
            print("je hebt nog niet geraden")
        else:
            print(multiplayer_check(player_guess))
        print("###############################################")

        player_guess = (input("welke letter will je raden:"))
        
        multiplayer_check(player_guess, player=1)
    else:
        player2()   
    
                         
def player2():
    print("player2")

def multiplayer_check(player_guess, player):
    
    player1_geraden.append(player_guess)
    
    if player_guess in player2_woord:
        awnser = (player_guess, "zit in het woord")
    elif player_guess in geraden:
        awnser = (player_guess, "heb ja al geraden")
    else:
        awnser = (player_guess, "zit niet in het woord")
    
    if player == 1:
        player1()
    else:
        player2()
    
    return awnser
    

def multiplayer_hint(woord, geraden):
    display = ""
    for letter in woord:
        if letter in geraden:
            display += letter
        else:
            display += "-"
    if "-" not in display:
        game_win()
    else:
        return display

# Deze functie zorgt dat de hint gemaakt wordt en dat als je een letter raad dat hij geupdate wordt         
def hint(woord, geraden):
    display = ""
    for letter in woord:
        if letter in geraden:
            display += letter
        else:
            display += "-"
    if "-" not in display:
        game_win()
    else:
        return display

# psuedo code 

# geraden = []

# functie letter_check (letter woord)
# als letter in geraden
#   print je hebt deze letter al geraden
# zo niet
#   als letter in woord 
#       print je hebt de letter goed geraden
#       voeg letter toe aan geraden lijst
#   zo niet 
#       print je hebt de letter fout
#       voeg letter to aan geraden lijst


# Deze functie controleert of de gegokte letter in het woord voorkomt
def in_word(guess, woord):
    global tries
    if guess in geraden:
        # De letter is al eerder geraden
        awnser = ("Deze letter heb je al geraden",)
        hangman(awnser, woord)

    else:
        geraden.append(guess)
        # De letter is nog niet eerder geraden
        if guess in woord:
            awnser = ("De letter", guess, "zit in het woord")
            hangman(awnser, woord)

        else:
            awnser = ("De letter", guess, "zit niet in het woord")
            tries += 1
            hangman(awnser, woord)
                      
def add_word_list():
    os.system("cls")
    woord = input("Welk woord wil je toevoegen: ")
    if (woord.isalpha()) == True:
        print("Toegevoegd :)")
        # Het nieuwe woord wordt toegevoegd aan de lijst in words.py
        wordlist.append(woord)
        print(wordlist)
        time.sleep(1)
    else:
        print("Ongeldige invoer probeer opnieuw")
        time.sleep(1)
        add_word_list()
    startup(u_score, comp_score)

# Deze functie splitst het woord in letters
def split(woord):
    return list(woord)

# Deze functie reset alle variabelen die het spel nodig heeft
def reset_game():
    global tries
    global geraden
    tries = 0
    geraden = []
    
def author():
    os.system("cls")
    print(Colors.red + '#######################################################################################################')
    print(Colorate.Vertical(Colors.purple_to_blue,''' ██████╗ ███████╗███╗   ███╗ █████╗  █████╗ ██╗  ██╗████████╗    ██████╗  ██████╗  ██████╗ ██████╗    
██╔════╝ ██╔════╝████╗ ████║██╔══██╗██╔══██╗██║ ██╔╝╚══██╔══╝    ██╔══██╗██╔═══██╗██╔═══██╗██╔══██╗██╗
██║  ███╗█████╗  ██╔████╔██║███████║███████║█████╔╝    ██║       ██║  ██║██║   ██║██║   ██║██████╔╝╚═╝
██║   ██║██╔══╝  ██║╚██╔╝██║██╔══██║██╔══██║██╔═██╗    ██║       ██║  ██║██║   ██║██║   ██║██╔══██╗██╗
╚██████╔╝███████╗██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██╗   ██║       ██████╔╝╚██████╔╝╚██████╔╝██║  ██║╚═╝
 ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝   
                                                                                                      
██╗     ██╗   ██╗ ██████╗ █████╗ ███████╗    ██╗  ██╗ ██████╗  ██████╗ ████████╗       ██████╗        
██║     ██║   ██║██╔════╝██╔══██╗██╔════╝    ██║ ██╔╝██╔═══██╗██╔═══██╗╚══██╔══╝    ██╗██╔══██╗       
██║     ██║   ██║██║     ███████║███████╗    █████╔╝ ██║   ██║██║   ██║   ██║       ╚═╝██║  ██║       
██║     ██║   ██║██║     ██╔══██║╚════██║    ██╔═██╗ ██║   ██║██║   ██║   ██║       ██╗██║  ██║       
███████╗╚██████╔╝╚██████╗██║  ██║███████║    ██║  ██╗╚██████╔╝╚██████╔╝   ██║       ╚═╝██████╔╝       
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝          ╚═════╝        '''))
    print(Colors.red + '#######################################################################################################')
    input("press enter to continue")
    print(Colors.white)
    startup(u_score, comp_score)
    

def game_over():
    global comp_score
    global u_score
    os.system("cls")
    print(hanged(tries))
    print(game_over_visual)
    comp_score += 1
    time.sleep(2)
    startup(u_score, comp_score)

def game_win():
    global comp_score
    global u_score
    os.system("cls")
    print(gewonnen_visual)
    u_score += 1
    time.sleep(2)
    startup(u_score, comp_score)


def monke():
    os.system("cls")
    monke = '''███╗   ███╗ ██████╗ ███╗   ██╗██╗  ██╗███████╗
████╗ ████║██╔═══██╗████╗  ██║██║ ██╔╝██╔════╝
██╔████╔██║██║   ██║██╔██╗ ██║█████╔╝ █████╗  
██║╚██╔╝██║██║   ██║██║╚██╗██║██╔═██╗ ██╔══╝  
██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║  ██╗███████╗
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
'''
    Write.Print(monke, Colors.blue_to_green, interval=0.01)
    input("press enter to continue:")
    startup(u_score, comp_score)
    
# Deze functie verzorgt de graphics van de galg
def hanged(man):
    graphic = [
        '''
       +------+
       |
       |
       |
       |
       |
    ==============
    ''',
        '''
       +------+
       |      |
       |      O
       |
       |
       |
    ==============
    ''',
        '''
       +------+
       |      |
       |      O
       |      |
       |
       |
    ==============
    ''',
        '''
       +------+
       |      |
       |      O
       |     -|
       |
       |
    ==============
    ''',
        '''
       +------+
       |      |
       |      O
       |     -|-
       |
       |
    ==============
    ''',
        '''
       +------+
       |      |
       |      O
       |     -|-
       |     /
       |
    ==============
    ''',
        '''
       +------+
       |      |
       |      O
       |     -|-
       |     / \\
       |
    ==============
    '''
    ]
    return graphic[man]

gewonnen_visual = (Colorate.Horizontal(Colors.green_to_cyan,'''####################################################################################################################################

     ██╗███████╗    ██╗  ██╗███████╗██████╗ ████████╗     ██████╗ ███████╗██╗    ██╗ ██████╗ ███╗   ██╗███╗   ██╗███████╗███╗   ██╗
     ██║██╔════╝    ██║  ██║██╔════╝██╔══██╗╚══██╔══╝    ██╔════╝ ██╔════╝██║    ██║██╔═══██╗████╗  ██║████╗  ██║██╔════╝████╗  ██║
     ██║█████╗      ███████║█████╗  ██████╔╝   ██║       ██║  ███╗█████╗  ██║ █╗ ██║██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██╔██╗ ██║
██   ██║██╔══╝      ██╔══██║██╔══╝  ██╔══██╗   ██║       ██║   ██║██╔══╝  ██║███╗██║██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██║╚██╗██║
╚█████╔╝███████╗    ██║  ██║███████╗██████╔╝   ██║       ╚██████╔╝███████╗╚███╔███╔╝╚██████╔╝██║ ╚████║██║ ╚████║███████╗██║ ╚████║
 ╚════╝ ╚══════╝    ╚═╝  ╚═╝╚══════╝╚═════╝    ╚═╝        ╚═════╝ ╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═══╝
 
####################################################################################################################################'''))

game_over_visual = (Colorate.Horizontal(Colors.yellow_to_red,'''###########################################################################

 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
 
###########################################################################'''))

hangman_visual = (Colorate.Vertical(Colors.red_to_white,'''██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
'''))

score_visual = (Colorate.Vertical(Colors.red_to_white,'''███████╗ ██████╗ ██████╗ ██████╗ ███████╗   
██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╗
███████╗██║     ██║   ██║██████╔╝█████╗  ╚═╝
╚════██║██║     ██║   ██║██╔══██╗██╔══╝  ██╗
███████║╚██████╗╚██████╔╝██║  ██║███████╗╚═╝
╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝   
'''))

you_visual = (Colorate.Vertical(Colors.white_to_red,'''  _   _    ___    _   _                                          _ 
 | | | |  / _ \  | | | |                                        (_)
 | |_| | | (_) | | |_| |                                         _ 
  \__, |  \___/   \__,_|                                        (_)
  |___/  '''))

computer_visual = (Colorate.Vertical(Colors.white_to_red,'''                                             _                     
   ___    ___    _ __ ___    _ __    _   _  | |_    ___   _ __   _ 
  / __|  / _ \  | '_ ` _ \  | '_ \  | | | | | __|  / _ \ | '__| (_)
 | (__  | (_) | | | | | | | | |_) | | |_| | | |_  |  __/ | |     _ 
  \___|  \___/  |_| |_| |_| | .__/   \__,_|  \__|  \___| |_|    (_)
                            |_|                                    '''))

def allnums(num):
    numbers = [
        '''   ___  
  / _ \ 
 | | | |
 | |_| |
  \___/ ''','''  _ 
 / |
 | |
 | |
 |_|''','''  ____  
 |___ \ 
   __) |
  / __/ 
 |_____|''','''  _____ 
 |___ / 
   |_ \ 
  ___) |
 |____/''','''  _  _   
 | || |  
 | || |_ 
 |__   _|
    |_|''','''  ____  
 | ___| 
 |___ \ 
  ___) |
 |____/''','''   __   
  / /_  
 | '_ \ 
 | (_) |
  \___/''','''  _____ 
 |___  |
    / / 
   / /  
  /_/  ''','''   ___  
  ( _ ) 
  / _ \ 
 | (_) |
  \___/''','''   ___  
  / _ \ 
 | (_) |
  \__, |
    /_/ '''
    ]
    
    return numbers[num]

# Het spel wordt gestart met de scores van de speler en de computer
os.system('mode con: cols=150 lines=40')
startup(u_score, comp_score)





