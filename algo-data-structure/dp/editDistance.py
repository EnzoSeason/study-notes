class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # minDis[i][j] means
        # the minimum number of operations required to convert
        #  word1[0:i] to word2[0:j]
        minDis = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # word1 = "abc"
        # word2 = ""
        # delete all the characters
        for i in range(m + 1):
            minDis[i][0] = i
        
        # word1 = ""
        # word2 = "abc"
        # insert all the characters
        for j in range(n + 1):
            minDis[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # covert word1[0:i] to word1[0:j]

                if word1[i - 1] == word2[j - 1]:
                    # do nothing
                    minDis[i][j] = minDis[i - 1][j - 1]
                else:
                    # covert word1[0:i] to word2[0:j-1], 
                    # then insert in word2 
                    insert = minDis[i][j - 1] + 1
                    # covert word1[0:i-1] to word2[0:j], 
                    # then delete a character in word2 
                    delete = minDis[i - 1][j] + 1
                    # covert word1[0:i-1] to word2[0:j-1], 
                    # then replace a character of word2[j-1]
                    replace = minDis[i - 1][j - 1] + 1
                    
                    minDis[i][j] = min(insert, delete, replace)

        return minDis[m][n]