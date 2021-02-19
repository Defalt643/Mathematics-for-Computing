# import numpy as np
# matrix=np.array(([[-9,-2,18,8],[10,-4,1,9],[11,2,13,10]]))
# A=matrix.min(axis=1)
# print(A)


# from fysom import Fysom
# fsm = Fysom({'initial' : 's0', 'events' :[
#     {'name': 'a', 'src': 's0', 'dst': 's1'},
#     {'name': 'b', 'src': 's0', 'dst': 's0'},
#     {'name': 'a', 'src': 's1', 'dst': 's0'},
#     {'name': 'b', 'src': 's1', 'dst': 's1'}]})
# print(fsm.current)
# fsm.b()
# print(fsm.current)
# fsm.a()
# print(fsm.current)
# fsm.a()
# print(fsm.current)

# import numpy as np
# A = np.array (['0', '10'])
# B = np.array (['1', '10'])
# P = [[x,y] for x in A for y in A]
# Q = [[x,y] for x in P for y in A]
# R = [[x,y] for x in P for y in B]
# print(R)
# print(P)
# print(Q)
# import numpy as np
#
# # input_array
# arr1 = np.arange(8)
# exponent = 2
# print("arr1         : ", arr1)
#
# # output_array
# out = np.power(arr1, exponent)
# print("\nOutput array : ", out)

