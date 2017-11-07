'''
Created on Oct 25, 2017

@author: Ancuta
'''

from validation import validation_list
from infrastructure import * 
from ui import read_variable
import tests

def convertire (l):
    aux=[]
    for item in l:
        aux.append(int(item))
    return aux

def print_message (message, list):
    print (message, list)
    
    
    
def menu_adaugare (list, undo):

    meniu_adaugare='''
            ________________________________________________________________________________________________________________________________
            |                                                             |                                                                 |   
            |                   CERINTE                                   |                        INSTRUCTIUNI                             |
            |_____________________________________________________________|_________________________________________________________________|
            |    "Adaugare"+lista scoruri [10 numere separate prin "+"]   |    - pentru adaugarea unui scor ultimului participant           |
            |    "Inserare"+participant + lista scoruri                   |    - pentru inserarea unui scor particpantului citit            |
            |    "Afisare"                                                |    - pentru afisarea listei curente                             |
            |    "Iesire"                                                 |    - pentru intoarcerea la meniul principal                     |
            |_____________________________________________________________|_________________________________________________________________|    
            '''
    valid=True
    while valid is True:
        print (meniu_adaugare)
        op=input ("Citeste:")
        l=[]
        l=op.split("+")
        
        if l[0].lower()=="adaugare":
            aux=convertire(l[1:11])
            if validation_list(aux) is False:
                print ("Elementele citite sunt invalide.")
                
            else:
                undo.append(list[:])
                list = add_newScore(list, aux)
        elif l[0].lower()=="inserare":
            participant=int(l[1])
            aux=convertire(l[2:12])
            if validation_list(aux) is False:
                print ("Elementele citite sunt invalide.")
            else:
                undo.append(list[:])
                list = inserare_scor_participant(list, participant, aux)
        elif l[0].lower()=="afisare":
                print("Lista actuala cu scorurile participantiilor este: ", list)
        elif l[0].lower()=="iesire":
            valid =False
        else:
            print(  "Optiune invalida")
        
          
          
                    
def menu_modificare_scor(list, undo):

    meniu_adaugare='''
               
                 _________________________________________________________________________________________________________________________
                |                                                       |                                                                |
                |                    CERINTE                            |                       INSTRUCTIUNI                             | 
                |_______________________________________________________|________________________________________________________________|                                   
                |    "Stergere"+participant                             |     - pentru stergerea scorului unui participant               |
                |    "Stergere multipla"+start + end                    |     - pentru stergerea scorului unui interval de participanti  |
                |    "Inlocuire"+participant +score                     |     - pentru inlocuirea spcr                                   |
                |    "Afisare                                           |     - pentru afisarea listei curente                           |
                |    "Iesire"                                           |     - pentru intoarcerea la meniul principal                   |
                |_______________________________________________________|________________________________________________________________|
            '''
    valid=True
    while valid is True:
        print (meniu_adaugare)
        op=input ("Citeste:")
        l=[]
        l=op.split("+")
        
        if l[0].lower()=="stergere":
            participant=int(l[1])
            undo.append(list[:])
            print_message("Lista actuala a scorurilor  este: ", delete_score_participant(list, participant))
        elif l[0].lower()=="stergere multipla":
            start=int(l[1])
            end=int (l[2])
            undo.append(list[:])
            print_message("Lista actuala a scorurilor este: ", delete_interval_participants(list, start, end))
        elif l[0].lower()=="inlocuire":
            participant=int(l[1])
            aux=convertire(l[2:12])
            if validation_list(aux) is False:
                print ("Elementele citite sunt invalide.")
            else:
                undo.append(list[:])
                print_message("Lista actuala a scorurilor este: ", replace_score_participant(list, participant, aux))
        elif l[0].lower()=="afisare":
                print("Lista actuala cua scorurile participantiilor este: ", list)
        elif l[0].lower()=="iesire":
            valid =False
        else:
            print(  "Optiune invalida")
        
        
        
        
        
def menu_afisari(list, undo):

    meniu_adaugare='''
                 _______________________________________________________________________________________________________________________________
                |                                              |                                                                               |
                |                    CERINTE                   |                       INSTRUCTIUNI                                            | 
                |______________________________________________|_______________________________________________________________________________|                                   
                |     "Tiparire" +  scor                       |   - pentru tiparirea participantiilor cu un scor mai mic decat un scor dat    |
                |     "Tiparire crescatoare "                   |   - pentru tiparirea ordonata a  participantiilor                             |
                |     "Tiparire multipla "+  scor              |   - pentru tiparirea participantiilor cu un  scor mai mare, ordonat dupa scor |
                |     "Afisare"                                |   - pentru afisarea listei curente                                            |
                |     "Iesire"                                 |   - pentru intoarcerea la meniul principal                                    |
                |______________________________________________|_______________________________________________________________________________|
           
            '''
    valid=True
    while valid is True:
        print (meniu_adaugare)
        op=input ("Citeste:")
        l=[]
        l=op.split("+")
        
        if l[0].lower()=="tiparire":
            score=int(l[1])
            print_message("Participantii cu scor mai mic decat un scor dat sunt: ", display_smaller_score(list, score))
        elif l[0].lower()=="tiparire crescatoare":
            print_message("Participantii ordonati dupa scor sunt: ", create_ascendingList(list))
            #vezi acasa
            
        elif l[0].lower()=="tiparire multipla":
            ''' score=int(l[1])
            aux=convertire(l[1:12])
            if validation_list(aux) is False:
                print ("Elementele citite sunt invalide.")
            else:
                print_message("Lista actuala a scorurilor este: ", replace_score_participant(list, participant, aux))
            '''
            score= int(l[1])
            l=create_ascendingList(list)
            print_message("Participantii ordonati cu scor mai made decat un scor dat sunt:  ", l[return_startPosition(list, score):])
            
        elif l[0].lower()=="afisare":
                print("Lista actuala cu scorurile participantiilor este: ", list)
        elif l[0].lower()=="iesire":
            valid =False
        else:
            print(  "Optiune invalida")
            
            
            
def menu_operatii(list, undo):

    meniu_adaugare='''
            _______________________________________________________________________________________________________________________________________________
            |                                                         |                                                                                   |
            |                COMENZI:                                 |                                        INSTRUCTIUNI                               |
            |_________________________________________________________|___________________________________________________________________________________|
            |    "Medie interval"+start+end                           |    - pentru calcularea mediei ep un interval dat                                  |
            |    "Scor minim"+start + end                              |    - pentru calcularea scorului minim pentru un interval de participanti         |
            |    "Tiparire"+start+end                                 |    - pentru tiparirea participantiilor cu scorul multiplu de 10                   |
            |    "Afisare                                             |    - pentru afisarea listei curente                                               |
            |    "Iesire"                                             |     - pentru intoarcerea la meniul principal                                      |
            |_________________________________________________________|___________________________________________________________________________________|
                                                                              
            '''
    valid=True
    while valid is True:
        print (meniu_adaugare)
        op=input ("Citeste:")
        l=[]
        l=op.split("+")
        
        if l[0].lower()=="medie interval":
            start=int (l[1])
            end= int (l[2])
            print_message("Media scorurilor pe intervalul dat este: ", get_Average(start, end, list))
        elif l[0].lower()=="scor minim":
            start=int(l[1])
            end=int (l[2])
            print_message("Cel mai mic scor in intervalul dat este:", the_smallest_ScoreInterval(start, end, list))
        elif l[0].lower()=="tiparire":
            start=int(l[1])
            end=int (l[2])
            print_message("Participantii dintr-un interval dat care au scorul multiplu de 10 sunt: ", multiple_ofsomething(start, end, list, 10))
        elif l[0].lower()=="afisare":
                print("Lista actuala cu scorurile participantiilor este: ", list)
        elif l[0].lower()=="iesire":
            valid =False
        else:
            print(  "Optiune invalida")
        
def menu_filtrare(list, undo):

    meniu_adaugare='''
    
            _______________________________________________________________________________________________________________________________________________
            |                                                         |                                                                                   |
            |                COMENZI:                                 |                                        INSTRUCTIUNI                               |
            |_________________________________________________________|___________________________________________________________________________________|
            |    "Filtrare multiplu"+ multiplu                        |      - pentru filtrarea participantiilor care au scorul multiplu unui numar dat   |
            |    "Filtrare scor"+scor                                 |      - pentru filtrarea participantiilor cu scor mai mic decat scorul dat         |
            |    "Afisare                                             |      - pentru afisarea listei curente                                             |
            |    "Iesire"                                             |      - pentru intoarcerea la meniul principal                                     |
            |_________________________________________________________|___________________________________________________________________________________|
                                                                              
            '''
    valid=True
    while valid is True:
        print (meniu_adaugare)
        op=input ("Citeste:")
        l=[]
        l=op.split("+")
        
        if l[0].lower()=="filtrare multiplu":
            score=int(l[1])
            undo.append(list[:])
            print_message("Lista actuala a participantiilor este ", filter_multiple_ofsomething(list, score))
        elif l[0].lower()=="filtrare scor":
            score=int(l[1])
            undo.append(list[:])
            print_message("Lista actuala a participantiilor este ", filter_participants_smaller_score(list, score))
        elif l[0].lower()=="afisare":
            print("Lista actuala cu scorurile participantiilor este: ", list)
        elif l[0].lower()=="iesire":
            valid =False
        else:
            print(  "Optiune invalida")
     
     
def menu_undo(list, undo):  
    meniu_undo ='''
            _______________________________________________________________________________________________________________________________________________
            |                                                         |                                                                                   |
            |                COMENZI:                                 |                                        INSTRUCTIUNI                               |
            |_________________________________________________________|___________________________________________________________________________________|
            |    "Undo operatii"+ numar                               |      - pentru refacerea a n operatii                                              |
            |                                                         |        (lista redevine lista scorurilor inainte de cele n operatii)               |
            |    "Afisare undo"                                       |      - pentru afisarea listei undo                                                |
            |    "Afisare"                                            |      - pentru afisarea listei curente cu scoruri                                  |
            |    "Iesire"                                             |      - pentru intoarcerea la meniul principal                                     |
            |_________________________________________________________|___________________________________________________________________________________|
                                                                              
    ''' 
    valid=True
    while valid is True:
        print (meniu_undo)
        
        op=input ("Citeste:")
        l=[]
        l=op.split("+")
        if l[0].lower()=="undo operatii":
            x=[]
            x.append(return_undo(undo, int(l[1])))
            if len(x)==1:
                list[:]=[]
                list[:]=x
        elif l[0].lower()=="afisare undo":
            print_message("Lista undo este: ", undo)
        elif l[0].lower()=="afisare":
            print_message("Lista de scoruri este: ", list)
        elif l[0].lower()=="iesire":
            valid=False
        else:
            print ("Optiune invalida ")   
            

def run_UI ():
    list=[]
    undo=[]
    menu='''             
            _________________________________________________________________________________________________________________
            |                                                                                                               |
            |                                     ~MENIU PRINCIPAL~                                                         |
            |_______________________________________________________________________________________________________________|
            |                                               |                                                               |
            |                COMENZI:                       |                          INSTRUCTIUNI                         |
            |_______________________________________________|_______________________________________________________________|
            |        "Adaugare"                             |          - pentru submenu-ul de adaugare                      |
            |        "Modificare"                           |          - pentru submenu-ul de modificare                    |
            |        "Tiparire"                             |          - pentru submenu-ul de tiparire                      |
            |        "Operatii"                             |          - pentru submenu-ul de operatii                      |
            |        "Filtrare"                             |          - pentru submenu-ul de filtrare                      |    
            |        "Undo"                                 |          - pentru operatia de undo                            | 
            |        "Iesire"                               |          - pentru parasire                                    |
            |_______________________________________________|_______________________________________________________________|
                                                                              

    '''
    
    options={"adaugare" :menu_adaugare,"modificare":menu_modificare_scor,"tiparire" :menu_afisari,"operatii":menu_operatii,"filtrare":menu_filtrare,"undo":menu_undo}
    
    valid=True
    while valid is True:
        print (menu)
        try:
            op= input("Optiunea: ")
            op=op.lower()
            if op =="iesire":
                valid=False
                print("La revedere")
            else:
                options[op](list, undo)
        except ValueError:
            print(" Nu ati introdus o instructiune valida..")
        except KeyError:
            print(" Nu ati introdus o instructiune valida.")

  
if __name__=="__main__":
    run_UI()


 
