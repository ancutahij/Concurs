'''
Created on Oct 24, 2017

@author: Ancuta
'''


from validation import *
from copy import deepcopy

def add_newScore(list,l):
    '''
        Functia adauga scor pentru un nou participant (ultimul participant)
        list=lista cu scorurile participantiilor
        l=noul scor pentru noul participant 
    '''
    
    list.append(l)
    return list


    
def inserare_scor_participant(list, participant, new_score):
    """
        Inserare scor pentru un participant dat.
        list reprezinta lista de scoruri ale participantiilor
        participant- participantul al carui scor trebuie inserat
        new_score- noul scor pentru participantul ales
    """
    
    list.pop(participant-1)
    list.insert(participant-1,new_score)
    return list


"Tipareste participantii care au scor mai mic decat un scor dat."
def getScore(l):
    '''
        Compute the given partipant's score.
        l= the participant's grades stored in a list
    '''
    return sum(l)



def display_smaller_score(scr, minimum):
    """
        Return all participants who have a smaller score than  the minimum variable.
        scr=all participant's list with their scores
        len= number of participants
        
    """
    
    auxiliary=[]
    for index,item in enumerate(scr):
        if getScore(item)<minimum:
            auxiliary.append(index+1)
            
    return auxiliary





"Tipărește participanții ordonat după scor."
def getMinimum(l):
    """
        Return the participant's index  with the smallest score.
        l= the participant's grades stored in a list
    """
    aux=100
    for index,item in enumerate(l):
        if aux >getScore(item):
            aux=getScore(item)
            var=index
    return var




def create_ascendingList(scr):
    """
        Create and return an ascending list with participants ordered by their score.
        scr=all participant's list with their scores
    """
    start=getMinimum(scr)#get only the index 
    score=101
    l=[]
    minimum=101
    while len(l)!=len(scr):
        for index, item in enumerate(scr):
            if getScore(item)==getScore(scr[start]):
                l.append(index+1)
            elif getScore(item)>getScore(scr[start]) and getScore(item)<minimum:
                minimum=getScore(scr[index])
                score=index
        start=score
        minimum=101
                
    return l    







"""Tipărește participanții cu scor mai mare decât un scor dat, ordonat după scor."""
def return_startPosition(scr, start ):
    """
        Return the start  position in the list create by function create_ascendingList.
        The start position means the one of participant's index who has a greater score than the start variable.
        scr=all participant's list with their scores
        start=the minimum score 
    """
    lista=create_ascendingList(scr)  
    for index, item  in enumerate(lista):
        if getScore(scr[item-1])>start:
            return index
        


"Calculează media scorurilor pentru un interval dat (ex. Se da 1 și 5 se tipărește media scorurilor participanților 1,2,3,4 și 5"
def get_Average(start, end, scr):
    """
        Return the scores' average for included participants between start and end. (inclusive)
        start=the start position for computing the average
        end= the end position for computing the average
        scr= all participants' list with their scores.
        
    """
    if validation_interval(scr, start, end) is True:
        suma=0
        for index in range(start-1, end):
            suma+=getScore(scr[index])
        return suma//(end-start+1)






"b. Calculează scorul minim pentru un interval de participanți dat."
def the_smallest_ScoreInterval(start,end, scr):
    """
        Return the smallest score into an interval of participants.
        start= the start index for interval
        end= the end index for interval
        scr=all participants' list with their scores.
        
    """
    if validation_interval(scr, start, end) is True:
        auxiliary=getMinimum(scr[start-1:end])
        return getScore(scr[auxiliary])





"c. Tipărește participanții dintr-un interval dat care au scorul multiplu de 10."
def multiple_ofsomething(start, end , scr, number):
    """
        Return the list of participants with score multiple of a given number .
        start= the start index position for interval
        end= the end index position for interval
        scr= all participant's grades stored in a list
    """
    l=[]
    if validation_interval(scr, start, end) is True:
        for index in range(start-1, end): 
            if getScore(scr[index])%number==0:
                l.append(index+1)
    return l


def delete_score_participant ( scr, participant):
    """
        Delete the given participant's score only if the partipant exists in our list.
        We verify if the participant takes part of our list.
        scr=all participant's grades stored in a list
        participant = the given participant 
    """
    if existance_participant(scr, participant) is True:
        del scr[participant-1]
    return scr


def delete_interval_participants (scr, start, end):
    """
        Delete the score for a given interval of participants.
        Firstly we check if the given interval is a valid one.
        scr=all participant's grades stored in a list
        start= start of given interval
        end=  end -------||------ 

        
    """
    if validation_interval(scr, start, end) is True:
        for index in range( end, start-1,-1):
            delete_score_participant(scr, index)
            
    return scr



def replace_score_participant(scr, participant, score  ):
    """
        Replace the given participant's score with a given score stored in score variable.
    """
    if existance_participant(scr, participant) is True:
        scr.pop(participant-1)
        scr.insert(participant-1,score)
    return scr



def filter_multiple_ofsomething ( scr, multiple):
    """
        Delete all participants that have their score multiple of a given number.
        The function makes calls to multiple_of_something() for finding the sub-list with participants with their scores being multiple of a given number.
        The function also calls to delete_score_participant for removing a participant's score.
        The list is traversed from the end to the beginning because if we delete the element from position 0, element from position one will decrease to position zero, 
            element from position two will decrease to position one ...
        In the end continueing the process in this way we will lose some elements for checking out.
        The solution for this problem is to starting to index from the end to 0.
    """
    l=multiple_ofsomething(1, len(scr), scr, multiple)
    for item in reversed(l):
        delete_score_participant(scr, item)
    return scr


    
    
def filter_participants_smaller_score (scr, score):
    """
        Delete all participants that have their score smaller than a given score.
    """
    l=display_smaller_score(scr, score)
    for item in reversed(l):
        delete_score_participant(scr, item)
    return scr


def delete_undo (undo, number):
    '''Delete the elements from undo list .
         !!!! THE  CURRENT LIST OF PARTICIPANTS IS NEVER STORED IN UNDO LIST. BEFORE A NEW OPERATION THE CURRENT LIST IS STORED, AFTER IT IS MODIFIED.
      ex: undo=[[],\
                [10,1,10,1,1,1,1,3,5,7],\
                 [[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10]],\
                 [[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10]],[10,1,10,1,1,1,1,3,5,7]], \
                 [[10,1,10,1,1,1,1,3,5,7],[10,1,10,1,1,1,1,3,5,7]]]
        Initially the list was empty,  we added a new scores 3 time in the row and we delete the participant 2's score.
        
        We want to see what values our list had before deleting operation.
        Our list was: [[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10]],[10,1,10,1,1,1,1,3,5,7]]
        The undo list now is: [[],\
                [10,1,10,1,1,1,1,3,5,7],\
                 [[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10]],\
                 [[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10]],[10,1,10,1,1,1,1,3,5,7]]|
                 
        We want to see what values our list had before 3 operations in a row (it doesn't matter what operations were, our list was modified every time)
        Before the last 3 operations in a row, our list was : [10,1,10,1,1,1,1,3,5,7] and our undo list now is [[],[10,1,10,1,1,1,1,3,5,7]]
        
    '''

    if number>1:
        undo=delete_interval_participants(undo, len(undo)-number+2, len(undo))
    return undo   

    

def return_undo( undo, number):
    """
        We check if we are able to do undo operation for given number. It's not allowed to do undo operation when our number in greater then the length of our list.
        If it is impossible we return unchanged undo list. 
        Else return the last element after the operation of deleting
        
    """
    
    if validation_length(undo, number) is True:
        undo=delete_undo(undo, number)
        x=[]
        x=undo[len(undo)-1]
        del undo[len(undo)-1]
        return x
    else:
        return undo
    
    
    

