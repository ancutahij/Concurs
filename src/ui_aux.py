'''
Created on Oct 31, 2017

@author: Ancuta
'''
 
def runUI ():
    menu='''
Alege o optiune:
    1. Adaugare scor participant.
    2. Tipariri lista participanti
    3. Operatii cu subset de participanti.
    4. Iesire
     
     '''   
    valid=True
    list=[]
    while valid is True:
        print (menu)

        op=int(input("Optiune menu: "))
        if op==1: 
            submenu='''
            1. Adaugă scor pentru un nou participant (ultimul participant).
            2. Inserare scor pentru un participant.
            3. Intoarcere menu principal.'''
            while True: 
                print (submenu)
                op = int(input("Alege optiune submeniu: "))
                if op == 1:
                    new_score = read_score()
                    list = add_newScore(list, new_score)
                elif op == 2:
                    participant = int(input("Alegeti un participant al carui scor sa fie inserat"))
                    new_score = read_score()
                    list = inserare_scor_participant(list, participant, new_score)
                elif op == 3:
                    break
                else:
                    print ("Optiune invalida")
        elif op ==2:
            submenu='''
            1. Tipărește participanții care au scor mai mic decât un scor dat. 
            2. Tipărește participanții ordonat după scor 
            3. Tipărește participanții cu scor mai mare decât un scor dat, ordonat după scor.
            4. Intoarcere menu principal.
            '''
            while True: 
                print( submenu)
                op=int(input("Alege optiune submeniu: "))
                if op==1:
                    score=int(input("Dati un scor pentru a fi afisati participantii cu scor mai mic: "))
                    print ("Participantii cu scor mai mic sunt: ",display_smaller_score(list,score))
                elif op==2:
                    print ("Participantii ordonati dupa scor sunt: ", create_ascendingList(list))
                elif op==3:
                    scor =int(input ("Dati un scor pentru a fi afisati toti participantii cu scorul mai mare: "))
                    l=create_ascendingList(list)
                    print ("Participantii ordonati crescator cu scorul mai mare decat scorul dat sunt : ",l[return_startPosition(list, scor):])
                elif op==4:
                    break
                else:
                    print ("Optiune invalida")
        elif op==3:
            submenu='''
            1. Calculează media scorurilor pentru un interval dat (ex. Se da 1 și 5 se tipărește media scorurilor participanților 1,2,3,4 și 5 
            2. Calculează scorul minim pentru un interval de participanți dat.
            3. Tipărește participanții dintr-un interval dat care au scorul multiplu de 10.
            4. Intoarcere meniu principal
                     '''
            while True:
                print( submenu)
                op=int(input("Alege optiune submeniu: "))
                if op==1:
                    start=int(input ("Dati inceput interval: "))
                    end=int(input ("Dati sfarsit interval: "))
                    print ("Media scorurilor in intervalul dat este: ", get_Average(start, end, list))
                elif  op==2:
                    start=int(input ("Dati inceput interval: "))
                    end=int(input ("Dati sfarsit interval: "))
                    print ("Cel mai mic scor in intervalul dat este:",the_smallest_ScoreInterval(start, end, list))
                elif op==3:
                    start=int(input ("Dati inceput interval: "))
                    end=int(input ("Dati sfarsit interval: "))
                    print ("Participantii care au scorul multiplu de 10 dintr-un interval dat sunt: ",multiple_ofsomething(start, end, list) )
                elif op==4:
                    break
                else:
                    print ("Optiune invalida")
        elif op==4:
            print ("la revedere")
            break
        else:
            print ("Optiune invalida")


if __name__=="__main__":
    runUI()