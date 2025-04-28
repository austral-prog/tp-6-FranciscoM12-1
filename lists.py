# Replace the "ANSWER HERE" with your answer
from math import trunc


def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) > 5:
        del list_to_remove_elements[0]
        del list_to_remove_elements[4]
        del list_to_remove_elements[5]
    elif len(list_to_remove_elements) ==5:
        del list_to_remove_elements[0]
        del list_to_remove_elements[4]
    elif len(list_to_remove_elements) <5:
        del list_to_remove_elements[0]
    else:
        list_to_remove_elements = []
    return list_to_remove_elements  # Remove this line and implement


def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, "pink")
    list_to_add_elements.apend("yellow")
    return list_to_add_elements # Remove this line and implement


def is_empty(list_to_check):
    if list_to_check == []:
        return True
    else:
        return False # Remove this line and implement


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >2 and len(list_to_compare2) >2:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
    return False


def list_of_lists(list_of_lists_to_modify):
    if len(list_of_lists_to_modify[0]) > 2:
        list_of_lists_to_modify[0] = list_of_lists_to_modify[0][0:2]
    if len(list_of_lists_to_modify[1])< 2:
        list_of_lists_to_modify[1] = []
    elif 5 > len(list_of_lists_to_modify[1]) > 1:
        list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:len(list_of_lists_to_modify[1])]
    else:
        list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:4]
    if len(list_of_lists_to_modify[2]) > 2 :
        list_of_lists_to_modify[2] = list_of_lists_to_modify[2][len(list_of_lists_to_modify[2])-2:len(list_of_lists_to_modify[2])]
    return list_of_lists_to_modify
