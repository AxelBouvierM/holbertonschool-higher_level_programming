#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    i = 0
    for count in range(0, list_length):
        try:
            i = my_list_1[count] / my_list_2[count]
        except (TypeError):
            i = 0
            print("wrong type")
        except (ZeroDivisionError):
            i = 0
            print("division by 0")
        except (IndexError):
            i = 0
            print("out of range")
        finally:
            pass
        result.append(i)
    return(result)
