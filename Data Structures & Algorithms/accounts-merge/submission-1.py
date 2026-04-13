from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # graph of  connected indexes
        emailSets = [set(accounts[i][1:]) for i in range(len(accounts))]
        setStatus = [0 for _ in range(len(accounts))] # 0 not processed, 1 kept, -1 merged (removed)
        for i in range(len(accounts)):
            if setStatus[i] != 0:
                continue
            setStatus[i] = 1
            j = i + 1
            while j < len(accounts):
                for email in emailSets[i]:
                    if email in emailSets[j]:
                        # merge them
                        setStatus[j] = -1
                        for jEmail in emailSets[j]:
                            emailSets[i].add(jEmail)
                        emailSets[j] = set()
                        j = i
                        break
                j += 1
        ans = []
        #print(emailSets)
        #print(setStatus)
        for i in range(len(emailSets)):
            if setStatus[i] == 1:
                accountEmails = sorted(list(emailSets[i]))
                ans.append([accounts[i][0]] + accountEmails)
        return ans
