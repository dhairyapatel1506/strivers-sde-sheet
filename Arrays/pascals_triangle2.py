class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        for i in range(rowIndex+1):
            row = []
            for j in range(i+1):
                if(j==0 or j==i):
                    row.append(1)
                else:
                    row.append(oldRow[j-1]+oldRow[j])
            oldRow = row[:]
        return row
