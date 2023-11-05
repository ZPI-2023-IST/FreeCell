
def __flatten_list(_list: list) -> list:
    return [elem for sublist in _list for elem in sublist]

board = [[1,2,3], [4,5,6], [7,8,9]]

print(__flatten_list(board))