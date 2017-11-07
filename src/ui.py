'''
Created on Oct 24, 2017

@author: Ancuta
'''
from infrastructure import *
import tests

def read_variable(mesaj):
    while True:
        try:
            x= int(input(mesaj ))
            break   
        except ValueError :
            print ("Alegeti un numar. ")
    return x

def print_message (message, list):
    print (message, list)
    
def read_score():
    """
        Functia citeste un scor complet, asta insemand ca citeste scorul la cele 10 probe si il memoreaza in lista l.
    """
    l=[]
    print("Dati scor (intre 1 si 10)  pentru fiecare proba: ")
    for i in range(0, 10):
        while  True:
            print ("Proba", i+1, ": ",)
            try:
                aux=int(input())
                if aux<1 or aux>10:
                    raise ValueError
                break
            except ValueError:
                print ("Invalid choice. Type a number between 1 and 10.")
        l.append(aux)
        
       
    return l



def menu_adaugare (list, undo):

    meniu_adaugare='''
            1. Adauga scor pentru un nou participant (ultimul participant).
            2. Inserare scor pentru un participant.
            3. Printeaza lista scorurilor participantiilor.
            0. Intoarcere menu principal.
            '''
    valid=True
    while valid is True:
        print (meniu_adaugare)
        op=read_variable("Alege o optiune: ")
        if op==1:
            new_score = read_score()
            undo.append(list[:])
            list = add_newScore(list, new_score)
        elif op==2:
            participant=read_variable("Alege un participant: ")
            new_score = read_score()
            undo.append(list[:])
            list = inserare_scor_participant(list, participant, new_score)
        elif op==3: 
            print_message("Lista actuala cu scorurile participantiilor este: ", list)
        elif op == 0:
            valid=False
        else:
            print ("Optiune invalida")
        

        
def menu_modificare_scor(list, undo ):
    

    meniu_modificare ="""
            1. Sterge scorul pentru un participant dat. 
            2. Sterge scorul pentru un interval de participanti. 
            3. Inlocuieste scorul de la un participant.
            4. Printeaza lista scorurilor participantiilor.
            0. Intoarcere la meniul principal.
            
    """
    valid= True
    while valid is True:
        print (meniu_modificare)
        op=read_variable("Alege o optiune: ")
        if op==1:
            participant=read_variable("Alege un participant: ")
            undo.append(list[:])
            print_message("Lista actuala a scorurilor  este: ", delete_score_participant(list, participant))
        elif op==2:
            start=read_variable("Alege un inceput de interval: ")
            end= read_variable("Alege un capat de interval: ")
            undo.append(list[:])
            print_message("Lista actuala a scorurilor este: ", delete_interval_participants(list, start, end))
        elif op==3:
            participant=read_variable("Alege un participant: ")
            score=read_score()
            undo.append(list[:])
            print_message("Lista actuala a scorurilor este: ", replace_score_participant(list, participant, score))
        elif op==4: 
            print_message("Lista actuala cu scorurile participantiilor este: ", list)
        elif op==0:
            valid=False
        else :
            print ("Optiune invalida")  

            

def menu_afisari(list, undo):


    meniu_afisare='''
            1. Tipareste participantii care au scor mai mic decat un scor dat.
            2. Tipareste participantii ordonat dupa scor 
            3. Tipareste participantii cu scor mai mare decat un scor dat, ordonat dupa scor.
            4. Printeaza lista scorurilor participantiilor.
            0. Intoarcere la meniul principal.
            
            
'''
    valid=True
    while valid is True: 
        print (meniu_afisare)
        op=read_variable("Alege o optiune: ")
        if op ==1 :
            score=read_variable("Citeste un scor: ")
            print_message("Participantii cu scor mai mic decat un scor dat sunt: ", display_smaller_score(list, score))
        elif op==2:
            print_message("Participantii ordonati dupa scor sunt: ", create_ascendingList(list)) 
        elif op==3:
            score=read_variable("Citeste un scor: ")
            l=create_ascendingList(list)
            print_message("Participantii ordonati cu scor mai mare decat un scor dat: ", l[return_startPosition(list, score):])
        elif op==4: 
            print_message("Lista actuala cu scorurile participantiilor este: ", list)
        elif op==0:
            valid=False
        else:
            print ("Optiune invalida")  

        
def menu_operatii (list, undo):
    

    meniu_operatii='''
            1. Calculeaza media scorurilor pentru un interval dat.
            2. Calculeaza scorul minim pentru un interval de participanti dat.
            3. Tipareste participantii dintr-un interval dat care au scorul multiplu de 10.
            4. Tipareste lista scorurilor participantiilor.
            0. Intoarcere la meniul principal.

     '''
    valid=True
    while valid is True:
        print (meniu_operatii)
        op=read_variable("Alege o optiune: ")
        if op ==1 :
            start=read_variable("Alege un inceput de interval: ")
            end= read_variable("Alege un capat de interval: ")
            print_message("Media scorurilor pe intervalul dat este: ", get_Average(start, end, list))
        elif op==2:
            start=read_variable("Alege un inceput de interval: ")
            end= read_variable("Alege un capat de interval: ")
            print_message("Cel mai mic scor in intervalul dat este:", the_smallest_ScoreInterval(start, end, list))
        elif op==3:
            start=read_variable("Alege un inceput de interval: ")
            end= read_variable("Alege un capat de interval: ")
            print_message("Participantii dintr-un interval dat care au scorul multiplu de 10 sunt: ", multiple_ofsomething(start, end, list, 10))
        elif op==0:
            valid=False
        elif op==4: 
            print_message("Lista actuala cu scorurile participantiilor este: ", list)
        else:    
            print ("Optiune invalida")  

def menu_filtrare(list, undo):
    

    meniu_filtrare="""
            1. Filtrare participanti care au scorul multiplu unui numar dat. 
            2. Filtrare participanti care au scorul mai mic decat un scor dat.
            3. Printeaza lista scorurilor participantiilor.
            0. Intoarcere la meniul principal
            
    """
    
    valid =True 
    while valid is True:
        print (meniu_filtrare)
        op=read_variable("Alege o optiune: ")
        if op ==1 :
            numar=read_variable("Alege un multiplu: ")
            undo.append(list[:])
            print_message("Lista actuala a participantiilor este ", filter_multiple_ofsomething(list, numar))
        if op==2:
            numar=read_variable("Alege un scor: ")
            undo.append(list[:])
            print_message("Lista actuala a participantiilor este ", filter_participants_smaller_score(list, numar))
        elif op==0:
            valid=False
        elif op==3: 
            print_message("Lista actuala cu scorurile participantiilor este: ", list)
        else:    
            print ("Optiune invalida")

def menu_undo(list, undo):
    
    meniu_filtrare="""
            1. Reface a n operatie (lista scorurilor devine lista scorurilor inainte de cele n operatii)
            2. Printeaza lista undo
            3. Printeaza lista scorurilor participantiilor.
            0. Intoarcere la meniul principal
            
    """
    valid=True
    while valid is True:
        print (meniu_filtrare)
        op=read_variable("Alege o optiune: ")
        
        if op==1:
            x=[]
            number=read_variable("Citeste un numar: ")
            x.append(return_undo(undo, number))
            if len(x)==1 :
                list[:]=[] # pentru a nu avea paranteze suplimentare
                list[:]= x
        elif op==2:
            print_message("Lista undo este: ", undo) 
        elif op==3:
            print_message("Lista actuala cu scorurile participantiilor este:", list) 
        elif op==0:
            valid=False
        else:    
            print ("Optiune invalida")  
          
    
def run_UI ():
    list=[]
    undo=[]
    menu=''' 
    Alege optiunea dorita:
        1. Adauga un scor la un participant.
        2. Modificare scor.
        3. Tipareste lista de participanti.
        4. Operatii pe un subset de participanti.
        5. Filtrare
        6. Undo
        0. Iesire
        
    '''
    options={1:menu_adaugare,2:menu_modificare_scor,3:menu_afisari,4:menu_operatii,5:menu_filtrare,6:menu_undo}
    valid=True
    while valid is True:
        print (menu)
        try:
            op=int (input("Optiunea: "))
            if op ==0:
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
   
undo=[[], [[1, 2, 2, 3, 3, 3, 3, 3, 4, 4]], [[1, 2, 2, 3, 3, 3, 3, 3, 4, 4], [5, 6, 6, 5, 6, 5, 6, 4, 6, 5]]]
list=[[1, 2, 2, 3, 3, 3, 3, 3, 4, 4], [5, 6, 6, 5, 6, 5, 6, 4, 6, 5], [4, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
#menu_undo(list, undo)
