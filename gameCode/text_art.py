import random
text_art = {}
text_art_other = {}

#____________________________MAIN CHARACTERS_______________________________________

dracula = r"""
                   __,-----,,,,  ,,,--------,__ 
                _-/|\\/|\\/|\\\|\//\\\//|/|//|\\_ 
               /|\/\//\\\\\\\\\\//////////////\\\\ 
             //|//           \\\///            |\\|\ 
            ///|\/             \/               \|\|\ 
           |/|//                                 |\\|\  
          |/|/                                    \|\|\
          ///;    ,,=====,,,  ~~-~~  ,,,=====,,    ;|\|\
         |/|/   '"          `'     '"          "'   ;|\|
         ||/`;   _--~~~~--__         __--~~~~--_   ;/|\|
         /|||;  :  /       \~~-___-~~/       \  :  ;|\| 
         /\|;    -_\  (o)  / ,'; ;', \  (o)  /_-    ;|| 
         |\|;      ~-____--~'  ; ;  '~--____-~      ;\| 
          ||;            ,`   ;   ;   ',            ;|| 
        __|\ ;        ,'`    (  _  )    `',        ;/|__ 
    _,-~###\|/;    ,'`        ~~ ~~        `',    ;|\###~-,_ 
  ,'#########||;  '                           '  ;\|/#######`, 
 .############; ,         _--~~-~~--_           ;#############'.
,-' `;-,########;        ,; |_| | |_| ;,       ;;########,-;' `-,
      ;@`,######;       ;_| :%`~'~'%: |_;       ;######,'@;
       ;@@`,#####;     :%%`\/%%%%%%%\/'%%:     ;#####,'@@;
        ;@@@`,####;     :%%%%%%%%%%%%%%%;     ;####,'@@@;
         ;@@@@`,###;     ;./\_%%%%%_/\.;     ;####,@@@@;
      _-'@@@@@@@@;-~;     ~~--|~|~|--~~     ;~--;@@@@@@@'-_
  _,-'@@@@@@@@@@@@;  ;        ~~~~~        ;   ;@@@@@@@@@@@`-,_
,~@@@@@@@@@@@@@@@@@;  \`~--__         __--~/  ;@@@@@@@@@@@@@@@@~,
@@@@@@@@@@@@@@@@@@@@;   \   ~~-----~~    /   ;@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@~-_  \  /  |  \   /  _-~@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@~~-\/   |   \/ -~~@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@(=)=;==========;=(=)@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@;    |     ;@@@@@@@@@@@@@@@@@@@@@@@@@@                                         
                                                               """                   
                                                                               
                                                                                                          
                                                               

freddy = r"""     
                15111111111111123                 
                13             33                 
                12             31                
               7157           7237               
               4171111111111111714               
               47               74               
  7354517 3534241               1424323 7154537  
151333317227232211117       711112232735713333151
43      174 143325217 77777 712523341 471      14
411     14142                       34141     714
 531  715367                         743517  1357
  32313454                             45431323  
     1715                               51717    
       23     746665         566641     15       
      721   7699999995     5999999967   757      
      727   33 732222657  56222237 13   757      
       21     49    2937   736    294     75       
       23    796122325     523221697    32       
      357     69313355     55331369     753      
     75        2466427133317346642        51     
     32     7542311967 19996991132457     22     
      41   22        59999957       32   147     
       25715            4            51752       
        7654            9            5461        
        76 43           9           34767        
         41165         797         56314         
         76 3234455421     7245544323 47         
          15 73241731172 27113715537 53          
           357   712545444545217    53           
             547                 744             
               7255233332333325527 """

grim = r"""
                                         .""--..__
                     _                     []       ``-.._
                  .'` '``.                  ||__           `-._
                 /    ,-.\\                 ||_ ```---..__     `-.
                /    /:::\\               /|//}          ``--._  `.
                |    |:::||              |////}                `-. \.
                |    |:::||             //'///                    `.\.
                |    |:::||            //  ||'                      `|
                /    |:::|/        _,-//\  ||
               /`    |:::|`-,__,-'`  |/  \ ||
             /`  |   |'' ||           \\   |||
           /`    \   |   ||            |  /||
         |`       |  |   |)            \\ | ||
        |          \ |   /      ,.__    \\| ||
        /           `         /`    `\\   | ||
       |                     /        \\  / ||
       |                     |        | /  ||
       /         /           |        `(   ||
      /          .           /          )  ||
     |            \          |     ________||
    /             |          /     `-------.|
   |\            /          |              ||
   \\/`-._       |           /              ||
    //   `.    /`           |              ||
   //`.    `. |             \\              ||
  ///\ `-._  )/             |              ||
 //// )   .(/               |              ||
 ||||   ,'` )               /              //
 ||||  /                    /             || 
 `\\` /`                    |             // 
     |`                     \\            ||  
    /                        |           //  
  /`                          \\         //   
/`                            |        ||    
`-.___,-.      .-.        ___,'        (/    
         `---'`   `'----'`"""

slenderman = r"""
                                        717                                        
                                      3     3                                      
                                     2      71                                     
                                     277  7771                                     
                                     2   77 77                                     
                                     11    71                                      
                                      13  111                                      
                                       177771                                         
	                               7713213   73 12377                                
                               37    337713733     3                               
                               3     1173 37177    37                              
                              77     71 777 371    77                              
                              7  77  2173 3172  7   7                              
                              1   1 77 33 11 77 1   1                              
                              3   17 7373 3771 17   3                              
                              3   75   17313   31   3                              
                             71   17    721    31   17                             
                             17   17    77     317   1                             
                             1   777    767    3 3   1                             
                             1   1 7    757    371   17                            
                            17   1 3    773    7177  71                            
                            1   7117     7      1 3   1                            
                            1   3 1     77717   3 1   7                            
                           17   373  137    737 1777  77                           
                           3    73137          73373   3                           
                          71   77 1             1  3   37                          
                          77   2  1             1  77  77                          
                          17  73  1             1   1  77                          
                          3   7   1     72      1   3   3                          
                         73   1   1     75      1   1   3                          
                         7    3   1     72      1   77  17                         
                         7   71   1     737     1    1  77                         
                         3   1    1     777     1    1   7                         
                         3   1    1     777     1    1   7                         
                        77   1    1     177     1    1   1                         
                        737777    1     3 7     1    1   3                         
                        7   7     1     3 1     1     77 7                         
                        1   1     1     3 3     1     3  1                         
                        1   3     1     3 3     1     3   1                        
                        1 7717    1    73 3     1     1 3 1                        
                        11133     1    71 3     1     71271                        
                         1277     1    1  17    1      1133                        
                          127     1    1  71    1       757                        
                                  1    1   1    1                                  
                                  1    1   1    1                                  
                                  1    1   1    1                                  
                                  1    3   1    1                                  
                                  1    3   1    1                                  
                                  1    3   1    1                                  
                                  1   71   1    1                                  
                                  1   17   17   1                                  
                                  1   1    71   1                                  
                                  1   1     3   1                                  
                                  1   1     3   1                                  
                                  1   1     3   1                                  
                                  17771     17771                                  
                                  1   1     1   1                                  
                                  37  1     31133                                  
                                   7777      77    """

pennywise = r"""
                                        317    53                                  
                                 7711117124441 742   17                            
                             34444444444444444444422445                            
                           544444444444444444444444444243                          
          77            7134444444444444444444444444444441               1         
       1443         72444444444444444444444444444444444444427            141       
      2441         54444444444444444444444444444444474444444443           541      
     34443       14444444444444442  3444444444444444 7444244444451       75447     
    744444427  344444444554435557    144444444444441  741  2444444445177244442     
    7444444444444444445773            5444444444442         744444444444444443     
    744444444444444441                14444444444             5444444444444441     
     2444444444444441                 2444442443               24444444444444      
    1244444444444445                7244443 142                 244444444444241    
     544444444444447           7132444427    33                 744444444444441    
     144444444444447            7777                            744444444444447    
      54444444444441                                            24444444444445     
      74444444444442                                            4444444444444      
       1444444444444                                           34444444444441      
       71544444444441                                          4444444444441       
       74444444444442                                         14444444444423       
        74444444444447                                        5444444444444        
         7444444444442             7                         74444444444447        
           344444444447           1             17           5444444444457         
             2444444215           2              5          353444444441           
               154444721 111111  51              12 317 71  5754444451             
               244444472       7241              153       12244451                
                 12444537    3421127      71    7523247    2344452                 
                     7525    766  1563  3 71  3617  65    7244427                  
                      7251     344217   311 7  7325547    523                      
                       335     753                  22    657                      
                        75    32                     33   4                        
                        12  752     74177  7715       34  4                        
                        47   32     54453444444       241 33                       
                        51     11      754457      7337   57                       
                         51       2537        1255      747                        
                          153      14444445444441    1227                          
                             143    7544    644    32                              
                                22   1124444447   57                               
                                  27  34454447  32                                 
                                   32          21                                  
                                     57      14                                    
                                      73222221      """

jack = """

                                1324664231                                     
                            41              16                                 
                         47                    15                              
                       4                         75                            
                      4                       88   5                           
                    71    0002                0006  3                          
                    2    000000              000006  5                         
                   2     000000003         200000007  9                        
                  3      00000000000       000000006                           
                  2      30000000000        00000005   5                       
                  3       2000000005   85 40 500008    9                       
                  3         5000098   14        717   38                       
                  67            4                     69                       
                  45 7                              7725                       
                   49                               6 3                        
                   1372                           731 1                        
                    753273                      117171                         
                      6  6 1                 4421  6                           
                        53   822 3  1 365337  7  4                             
                           44    4            97                               
                                12455555541                       2498002      
                                  7      3                  500000002          
                                   6      2             400000009              
  80000000000000002                       225       2000000000081              
            00000000000043         84      00    20000000000000000000000047    
          8000000000000000000004   100   3500  0000000000000000000000000000009 
       4000000000000000000000000000000000000000000000000000000008651           
    5000000000000000000000000000000000034095000000000000000008                 
               00000000000863         380009     73498000000004                
               00000001                  77                728006              
              00083                                              66            
             007                                                               
           79                                                                
"""

#_____________________________________EXTRAS___________________________________________

ghost = r"""
     .-.
   .'   `.
   :g g   :
   : o    `.
  :         ``.
 :             `.
:  :         .   `.
:   :          ` . `.
 `.. :            `. ``;
    `:;             `:'
       :              `.
        `.              `.     .
          `'`'`'`---..,___`;.-'

"""


#DISPLAY HOUSE AT START OF PROGRAM?
haunted_house = r"""
                                              ,           ^'^  _
                                              )               (_) ^'^
         _^_                    .---------. ((        ^'^
         (('>                    )`'`'`'`'`( ||                 ^'^
    _    /^|                    /`'`'`'`'`'`\\||           ^'^
    =>--/__|m---               /`'`'`'`'`'`'`\\|
         ^^           ,,,,,,, /`'`'`'`'`'`'`'`\\      ,
                     .-------.`|`````````````|`  .   )
                    / .^. .^. \\|  ,^^, ,^^,  |  / \ ((
                   /  |_| |_|  \\  |__| |__|  | /,-,\||
        _         /_____________\\ |")| |  |  |/ |_| \|
       (")         |  __   __  |  '==' '=='  /_______\     _
      (' ')        | /  \ /  \ |   _______   |,^, ,^,|    (")
       \  \        | |--| |--| |  ((--.--))  ||_| |_||   (' ')
     _  ^^^ _      | |__| |("| |  ||  |  ||  |,-, ,-,|   /  /
   ,' ',  ,' ',    |           |  ||  |  ||  ||_| |_||   ^^^
.,,|RIP|,.|RIP|,.,,'==========='==''=='==''=='=======',,....,,,,.,"""


#this skeletons just looks cool - could be extra enemy or ornament in the house?
skeleton1 = r"""

              .7
            .'/
           / /
          / /
         / /
        / /
       / /
      / /
     / /         
    / /          
  __|/
,-\__\,
|f-"Y\|
\()7L/
 cgD                            __ _
 |\(                          .'  Y '>,
  \ \                        / _   _   \,
   \\\\                       )(_) (_)(|}
    \\\\                      {  4A   } /
     \\\\                      \uLuJJ/\l
      \\\\                     |3    p)/
       \\\\___ __________      /nnm_n//
       c7___-__,__-)\,__)(".  \_>-<_/D
                  //V     \_"-._.__G G_c__.-__<"/ ( \.
                         <"-._>__-,G_.___)\   \\7\.
                        ("-.__.| \\"<.__.-" )   \ \.
                        |"-.__"\  |"-.__.-".\   \ \.
                        ("-.__"". \\"-.__.-".|    \_\.
                        \\"-.__""|!|"-.__.-".)     \ \.
                         "-.__""\_|"-.__.-"./      \ l
                          ".__''"">G>-.__.-">       .--,_

"""

#OBJECT INSIDE THE HOUSE?
skull = r"""
                           ,--.
                          {    }
                          K,   }
                         /  `Y`
                    _   /   /
                   {_'-K.__/
                     `/-.__L._
                     /  ' /`\_}
                    /  ' /     
            ____   /  ' /
     ,-'~~~~    ~~/  ' /_
   ,'             ``~~~%%',
  (                     %  Y
 {                      %% I
{      -                 %  `.
|       ',                %  )
|        |   ,..__      __. Y
|    .,_./  Y ' / ^Y   J   )|
\           |' /   |   |   ||
 \          L_/    . _ (_,.'(
  \,   ,      ^^""' / |      )
    \_  \          /,L]     /
      '-_`-,       ` `   ./`
         `-(_            )
             ^^\..___,.--`
"""

#USE FOR FIGHTING DRACULA?
vampire_attack = r"""     
        __   __
     .-'  "."  '-.
   .'   ___,___   '.
  ;__.-; | | | ;-.__;
  | \  | | | | |  / |
   \ \/`"`"`"`"`\/ /
    \_.-,-,-,-,-._/
     \`-:_|_|_:-'/
      '.       .'
        `'---'`
        """

#DISPLAY AT END OF GAME?
frankenstein = r"""
                         _,--~~~,
                       .'        `.
                       |           ;
                       |           :
                      /_,-==/     .'
                    /'`\*  ;      :      
                  :'    `-        :      
                  `~*,'     .     :      
                     :__.,._  `;  :      
                     `\\'    )  '  `,     
                         \-/  '     )     
                         :'          \ _
                          `~---,-~    `,)
          ___                   \     /~`\\
    \---__ `;~~~-------------~~~(| _-'    `,
  ---, ' \`-._____     _______.---'         \\
 \--- `~~-`,      ~~~~~~                     `,
\----      )                                   \\
\----.  __ /                                    `-
 \----'` -~____  
               ~~~~~--------,.___     
                                 ```\_
                                 """


text_art["dracula"] = dracula
text_art["freddy"] = freddy
text_art["grim"] = grim
text_art["slenderman"] = slenderman
text_art["pennywise"] = pennywise

#text_art_other["haunted_house"] = haunted_house
#text_art_other["frankenstein"] = frankenstein

def jumpscare():
    num = random.randint(0,4)
    array = []
    for key in text_art:
        array.append(text_art[key])
    print(array[num])
    print()
    print("BOO!!!")
        
def display_character(character):
    print(character["image"])
    

#extras:
#text_art["jack"] = jack
#text_art["skeleton1"] = skeleton1
#text_art["skull"] = skull
#text_art["vampire_attack"] = vampire_attack
#text_art["frankenstein"] = frankenstein