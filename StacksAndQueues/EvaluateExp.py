class Solution:
	# @param A : list of strings
	# @return an integer
    def evalRPN(self, A):
        tempArr = []
        for i in range(0, len(A)):
            char = A[i]
            if(char == '+' or char == '-' or char == '/' or char == '*'):
                operand1 = tempArr[- 2]
                operand2 = tempArr[- 1]
                del tempArr[-1]
                del tempArr[-1]
                if(char == '+'):
                    result = operand1 + operand2
                    tempArr.append(result)
                elif(char == '-'):
                    result = operand1 - operand2
                    tempArr.append(result)
                elif(char == '/'):
                    result = operand1 // operand2
                    tempArr.append(result)
                elif(char == '*'):
                    result = operand1 * operand2
                    tempArr.append(result)
            else:
                tempArr.append(int(char))
        return tempArr[0]

A = ['4', '13', '5', '/', '+']
Solution().evalRPN(A)