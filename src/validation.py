'''
Created on Oct 27, 2017

@author: Ancuta
'''

def existance_participant  ( str, participant ):
    """
        Check out if a participant takes part of our list.
        srt= all participants'  grades list
        participant- the variable which contains the participant
    """
    if participant>len(str):
        return False
    return True



def validation_interval ( scr , start , end):
    """
        We verify if an interval exist in our participants' list.
        We check out if the start of given interval is greater or equal than 1 and if the end of given interval is smaller than the length of list.
        srt= all participants'  grades list
        start= start of given interval
        end=  end -------||------        
    """
    if start >end or start <1 or end >len(scr):
        return False
    return True

def validation_list (scr):
    """
        We check out if a list has exactly 10 elements and all elements are numbers between 1 and 10.
    """
    if len(scr)<10:
        return False
    for item in scr:
       if item>10 or item<1:
           return False
    return True

def validation_length(list, number):
    if number>len(list):
        return False
    return True
   