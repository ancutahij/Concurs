
'''
Created on Oct 27, 2017

@author: Ancuta
'''

from infrastructure import *
def test_add_newScore():
    assert add_newScore([[10,1,10,1,1,1,1,3,5,7]], [10,1,10,1,1,1,1,3,5,7])==[[10,1,10,1,1,1,1,3,5,7],[10,1,10,1,1,1,1,3,5,7]]

def test_inserare_scor_participant():
    assert inserare_scor_participant([[10,1,10,1,1,1,1,3,5,7], [10,1,10,1,1,1,1,3,5,7]], 1,[2,6,4,6,8,4,10,2,1,3] )==\
    [[2,6,4,6,8,4,10,2,1,3],[10,1,10,1,1,1,1,3,5,7]]

def test_getScore():
    """
        Does tests for the function getScore defined upper.
    """
    assert getScore([10,1,10,1,1,1,1,3,5,7])==40
    assert getScore([2,6,4,6,8,4,10,2,1,3])==46
    
    
def test_display_smaller_score():
    """
         Does tests for the function display_smallee_score defined upper.
    """
    assert display_smaller_score([[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10]],50)==[1]
    assert display_smaller_score([[10,1,10,1,1,1,1,3,5,7],[10,1,4,2,7,8,3,5,2,10]],2)==[]

def test_getMinimum():
    """
        Test whether the function getMinimum works properly.
    """
    assert getMinimum([[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10]])==0
    assert getMinimum([[10,1,10,1,1,1,1,3,5,7],[10,1,4,2,7,8,3,5,2,10]])==0
 
def test_create_ascendingList():
    '''
        Make tests for the function create_ascendingList defined upper.
    '''
    assert create_ascendingList([[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,1]]) ==[3,1,2]
    assert create_ascendingList([[10,1,10,1,1,1,1,3,5,7],[10,10,4,2,7,8,3,5,2,10]])==[1,2]

def test_return_startPosition():
    """
        Check whether the function return_startPosition works properly
    """

    assert return_startPosition([[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,1]], 1)==0
    # pentru lista de mai sus lista crescatoarea este: 3,1,2 . Returnam  0 deoarece lista scorul participantului de pe pozitia 2 este cel mai mic scor mai mare decat 1.
    assert return_startPosition([[10,1,10,1,1,1,1,3,5,7],[10,10,4,2,7,8,3,5,2,10]], 41)==1



def test_getAverage():
    assert get_Average(1, 3, [[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,1]])==51
    assert get_Average(3,3 , [[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,1]])==14


def test_smallest_ScoreInterval():
    assert the_smallest_ScoreInterval(1, 3,[[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,1]] )==14
    assert the_smallest_ScoreInterval(1,2,[[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,1]])==40

def test_multiple_of10():
    assert multiple_ofsomething(1, 3, [[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,1]],10)==[1,2]
    assert multiple_ofsomething(1, 4, [[11,1,2,1,1,1,1,3,5,1],[1,1,1,1,1,1,1,1,1,2],[2,2,2,2,1,1,1,1,1,1],[1,2,3,4,5,6,7,8,9,10]],10)==[]

def test_delete_score_participant ():
    assert delete_score_participant([[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,1]],3)==\
    [[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10]]
    assert delete_score_participant([[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,1]],4)==\
    [[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,1]]
    assert delete_score_participant([[10,1,10,1,1,1,1,3,5,7]], 1)==[]
    
def test_delete_interval_participants ():
    assert delete_interval_participants([[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,1]], 1, 3)==[]
    assert delete_interval_participants([[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,1]], 0, 2)== \
    [[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,1]]
def test_replace_score_participant ():
    assert replace_score_participant([[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,1]], 1, [2,6,4,6,8,4,10,2,1,3])==\
    [[2,6,4,6,8,4,10,2,1,3],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,1]]
    assert replace_score_participant([[10,1,10,1,1,1,1,3,5,7],[10,1,4,2,7,8,3,5,2,10]], 3, [2,2,2,2,1,1,1,1,1,1])==\
    [[10,1,10,1,1,1,1,3,5,7],[10,1,4,2,7,8,3,5,2,10]]
 
 
 
def test_filter_multiple_ofsomething():
    assert filter_multiple_ofsomething([[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,2]], 5)==[]
    assert filter_multiple_ofsomething([[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,2]], 10)==[[2,2,2,2,1,1,1,1,1,2]]
    
def test_filter_participants_smaller_score():
    assert filter_participants_smaller_score([[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,2]], 101)==[]
    assert filter_participants_smaller_score([[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,1,1,1,1,1,2]], 16)==[[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10]]

def test_delete_undo():
    assert delete_undo([[],\
                        [10,1,10,1,1,1,1,3,5,7],\
                        [[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10]],\
                        [[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[10,1,10,1,1,1,1,3,5,7]]], 2)==[[], \
                                                                                                                [10,1,10,1,1,1,1,3,5,7],\
                                                                                                                [[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10]]]
    assert delete_undo([[],\
                        [10,1,10,1,1,1,1,3,5,7],\
                        [[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10]],\
                        [[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[10,1,10,1,1,1,1,3,5,7]]], 4)==[[]]
    assert delete_undo([[],\
                        [10,1,10,1,1,1,1,3,5,7],\
                        [[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10]],\
                        [[10,1,10,1,1,1,1,3,5,7],[10,10,10,10,10,10,10,10,10,10],[10,1,10,1,1,1,1,3,5,7]]], 5)==[]
                        


def test_return_undo():
    assert return_undo([[], [10,1,10,1,1,1,1,3,5,7]], 1)==[10,1,10,1,1,1,1,3,5,7]

test_add_newScore()
test_inserare_scor_participant()  
test_getScore()    
test_display_smaller_score()
test_getMinimum()
test_create_ascendingList()
test_return_startPosition()
test_getAverage()
test_smallest_ScoreInterval()
test_multiple_of10()
test_delete_score_participant()
test_delete_interval_participants()
test_replace_score_participant()
test_filter_multiple_ofsomething()
test_filter_participants_smaller_score()
test_delete_undo()
test_return_undo()

