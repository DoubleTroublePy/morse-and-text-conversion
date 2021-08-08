import re
from vocabolary import vocabolary

class conversion:
    #- convert text to morse code -
    def txtMs(self, text, times = 1):
        voc = vocabolary() #call the constructor
        morse = ""
        text = str(text)
        for tim in range(times): #scan the code and conver charater by charatter text in morse code
            for letter in text:
                if letter != ' ':
                    morse += str(voc.txtMs(letter)) #call the class and add it to the morse string
                    morse += " " #add a space
                else:
                    morse += "       " #add a space
        morse = re.sub(r"(_)", ".", morse) #replace underscore whit dot (compatibiliti problems)
        return morse

    #- conversion morse to text -
    def msTxt(self, morse, times = 1):
        voc = vocabolary()#call the constructor
        morse += '  '
        morseBuffer = ''
        text = ''
        flag = 0
        for charatter in morse: #scan the morse strng charatter by charatter
            if charatter == ' ' and flag == 0: #if is the frist space convert the buffe in a char
                textBuffer = str(voc.msTxt(morseBuffer))
                if textBuffer != 'None': 
                    text += textBuffer
                morseBuffer = '' #buffer reset
                flag += 1 #add a space
            else:
                if charatter == '.': #conver dot in underscore
                    morseBuffer += '_'
                elif charatter != '' and charatter != ' ': #else add the char
                    morseBuffer += charatter

            if flag < 7 and charatter == ' ': #count the spaces after the frist
                flag += 1
            else:
                flag = 0 #flag reset

            if flag == 7: #after seven morse spaces add a char space
                text += ' '      
        return text

# ==============================================================================================================================================                                                    
# |                                                                                         | Double Trouble                                   |
# |                                           #                                             |     project: morse and text conversion           |
# |                                          ###                                            |     date: 2021-08-08                             |
# |                                         #####                                           |     file description:                            |
# |                     ############        #####        ###########                        |       main class, here happens                   |
# |               ######################   #######   #########################              |       the bigger magic                           |
# |           ####################################################################          |                                                  |
# |       ############################################################################      |                                                  |
# |    #################################################################################    |                                                  |
# |            ######   #################  #######  #################   #######             |                                                  |
# |                                         #####                                           |--------------------------------------------------|
# |                                         #####                                           | Social                                           |
# |                                        #######                                          |     Github: http://github.com/DoubleTroublePy    |
# |                                       #########                                         |     Twitter: @DoubleTroublePy                    |
# |                                                                                         |                                                  |
# ==============================================================================================================================================