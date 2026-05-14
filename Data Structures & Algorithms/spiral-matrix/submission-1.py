class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        res = []
        top , right , bottom , left = 0, n-1 , m-1, 0
        while top<=bottom and  left<=right:
            for j in range(left,right+1):
                res.append(matrix[top][j])
            top+=1
            if top>bottom:
                break
            for i in range(top ,bottom+1):
                res.append(matrix[i][right])
            right-=1
            if left>right:
                break
            for j in range(right , left-1 , -1):
                res.append(matrix[bottom][j])
            bottom -=1
            if top>bottom:
                break
            for i in range(bottom ,top-1 , -1):
                res.append(matrix[i][left])
            left+=1
            if left>right:
                break
        return res