# You are given an integer array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
#  Check if these points make a straight line in the XY plane.

from typing import List
from fractions import Fraction

def checkStraightLine(coordinates: List[List[int]]) -> bool:

    if coordinates[0][0] == coordinates[1][0]:
        stright_line = coordinates[0][0]
        for cord in coordinates:
            if cord[0] != stright_line:
                return False
        
        return True
        
    else:
        first_slope = Fraction(coordinates[1][1] - coordinates[0][1] , coordinates[1][0] - coordinates[0][0])

        for i in range(len(coordinates)-1):
            
            if coordinates[i+1][0] - coordinates[i][0] == 0:
                return False

            slope = Fraction(coordinates[i+1][1] - coordinates[i][1] , coordinates[i+1][0] - coordinates[i][0])
            if slope != first_slope:
                return False

        return True



# print(checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))


# print(checkStraightLine([[0,0],[0,1],[0,-1]]))
print(checkStraightLine([[2,1],[4,2],[6,3]]))
