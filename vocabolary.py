import re 
class vocabolary:
    #- dictionary char to morse -
    switch = {
        '1':'_----',
        '2':'__---',
        '3':'___--',
        '4':'____-',
        '5':'_____',
        '6':'-____',
        '7':'--___',
        '8':'---__',
        '9':'----_',
        '0':'-----',
        'a':'_-',
        'b':'-___',
        'c':'-_-_',
        'd':'-__',
        'e':'_',
        'f':'__-_',
        'g':'--_',
        'h':'____',
        'i':'__',
        'j':'_---',
        'k':'-_-',
        'l':'_-__',
        'm':'--',
        'n':'-_',
        'o':'---',
        'p':'_--_',
        'q':'--_-',
        'r':'_-_',
        's':'___',
        't':'-',
        'u':'__-',
        'v':'___-',
        'w':'_--',
        'x':'-__-',
        'y':'-_--',
        'z':'--__',
        ' ':' ',
        '\n':' '
    }

    #- convert morse code in char -
    def msTxt(self, charatter:str) -> str:
        regex = r"'(.a*)': '"+ str(charatter) +"'," #make a rege
        search = re.search(regex, str(self.switch)) #make a inverse research morse --> char
        if search != None: 
            return search.group(1)
        else:
            return None

    #- convert char in to morse code -
    def txtMs(self, charatter:str) -> str:
        charatter = charatter.lower()
        return self.switch[charatter]
        
# ==============================================================================================================================================                                                    
# |                                                                                         | Double Trouble                                   |
# |                                           #                                             |     project: morse and text conversion           |
# |                                          ###                                            |     date: 2021-08-08                             |
# |                                         #####                                           |     file description:                            |
# |                     ############        #####        ###########                        |       two reasons motivate the existence of      |
# |               ######################   #######   #########################              |       this class: first and minor python dont    |
# |           ####################################################################          |       has the switch construct, second reason    |
# |       ############################################################################      |       is to handle i little of string digesting  |
# |    #################################################################################    |                                                  |
# |            ######   #################  #######  #################   #######             |                                                  |
# |                                         #####                                           |--------------------------------------------------|
# |                                         #####                                           | Social                                           |
# |                                        #######                                          |     Github: http://github.com/DoubleTroublePy    |
# |                                       #########                                         |     Twitter: @DoubleTroublePy                    |
# |                                                                                         |                                                  |
# ==============================================================================================================================================

