from collections import defaultdict

class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:



        # TC: O(n)

        # initialize match to check how many characters are matching at a point

        match = 0

        n = len(s)



        pDict = defaultdict(int)

        for c in p:

            pDict[c] += 1

        left = 0

        res = []



        # Logic for the next character in the window

        for i in range(n):

            if s[i] in pDict:

                pDict[s[i]] -= 1

                if pDict[s[i]] == 0:

                    match += 1



            # Logic for the character which is excluded from the window once we move forward one character at a time

            if i >= len(p):

                if s[left] in pDict:

                    pDict[s[left]] += 1

                    if pDict[s[left]] == 1:

                        match -= 1

                left += 1

            

            if match == len(pDict):

                res.append(left)

        return res





        # TC: O(n^2)

        ns = len(s)

        np = len(p)

        p = ''.join(sorted(p))

        res = []



        for i in range(0, ns - np + 1):

            aLen = s[i: i+np]

            aLen = ''.join(sorted(aLen))



            if aLen == p:

                res.append(i)



        return res





