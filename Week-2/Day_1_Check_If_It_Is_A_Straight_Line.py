class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        try:
            slope=(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        except:
            slope=0
        for i in range(1,len(coordinates)-2):
            try:
                m=(coordinates[i+1][1]-coordinates[i][1])/(coordinates[i+1][0]-coordinates[i][0])
                if(m!=slope):
                    return False
            except:
                m=0
                if(m!=slope):
                    return False
        return True
            
