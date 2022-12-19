#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(0, list_length):
        try:
            solution = my_list_1[i] / my_list_2[i]
        except TypeError:
            solution = 0
            print("wrong type")
        except IndexError:
            solution = 0
            print("out of range")
        except ZeroDivisionError:
            solution = 0
            print("division by 0")
        finally:
            res.append(solution)
    return res
