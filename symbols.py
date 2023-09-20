LOGO = [
    """   ____                                          _ 
  / ___|___  _ __ ___  _ __ ___   __ _ _ __   __| |
 | |   / _ \\| '_ ` _ \\| '_ ` _ \\ / _` | '_ \\ / _` |
 | |__| (_) | | | | | | | | | | | (_| | | | | (_| |
  \\____\\___/|_| |_| |_|_| |_| |_|\\__,_|_| |_|\\__,_|""",
    """        ____                            _   
       |  _ \\ _ __ ___  _ __ ___  _ __ | |_ 
       | |_) | '__/ _ \\| '_ ` _ \\| '_ \\| __|
       |  __/| | | (_) | | | | | | |_) | |_ 
       |_|   |_|  \\___/|_| |_| |_| .__/ \\__|
                                 |_|        """,
    """ _____ _         _____             _____          
|_   _(_) ___   |_   _|_ _  ___   |_   _|__   ___ 
  | | | |/ __|____| |/ _` |/ __|____| |/ _ \\ / _ \\
  | | | | (_|_____| | (_| | (_|_____| | (_) |  __/
  |_| |_|\\___|    |_|\\__,_|\\___|    |_|\\___/ \\___|"""
]
board_symbols = {
    "x": """ X       X 
   X   X   
     X     
   X   X   
 X       X 
""",
    "x_vertical_line": """ X   |   X 
   X | X   
     X     
   X | X   
 X   |   X 
""",
    "x_horizontal_line": """ X       X 
   X   X   
-----X-----
   X   X   
 X       X 
""",
    "x_diagonal_nesw": """ X      /X/
   X  /X/  
    /X/    
  /X/  X   
/X/      X 
""",
    "x_diagonal_nwse": """\\X\\      X 
  \\X\\  X   
    \\X\\    
   X  \\X\\  
 X      \\X\\
""",
    "o": """    OOO    
  O     O  
 O       O 
  O     O  
    OOO    """,
    "o_vertical_line": """   OO|OO   
  O  |  O  
 O   |   O 
  O  |  O  
   OO|OO   """,
    "o_horizontal_line": """   OOOOO   
  O     O 
-O-------O-
  O     O 
   OOOOO   """,
    "o_diagonal_nesw": """   OOO//   
 O   // O  
O   //   O 
 O //   O  
  //OOO    """,
    "o_diagonal_nwse": """  \\\\OOO    
 O \\\\   O  
O   \\\\   O 
 O   \\\\ O  
   OOO\\\\   """,
    "_": "".join([11 * " " + "\n" if i < 4 else 11 * " " for i in range(5)])
}
board_positions = {
    "1":
    """      _    
     / |   
     | |   
     | |   
     |_|   """,
    "2":
    """   ____    
  |___ \\   
    __) |  
  / ___/   
  |_____|  """,
    "3":
    """   _____   
  |___ /   
    |_ \\    
   ___) |  
  |____/   """,
    "4":
    """   _  _    
  | || |   
  | || |_  
  |__   _| 
     |_|   """,
    "5":
    """   ____    
  | ___|   
  |___ \\   
   ___) |  
  |____/   """,
    "6":
    """    __     
   / /_    
  | '_ \\   
  | (_) |  
   \\___/   """,
    "7":
    """   _____   
  |___  |  
     / /   
    / /    
   /_/     """,
    "8":
    """    ___    
   ( _ )   
   / _ \\   
  | (_) |  
   \\___/   """,
    "9":
    """    ___    
   / _ \\   
  | (_) |  
   \\__, |  
     /_/   """
}

for key in board_symbols:
    print(board_symbols[key])