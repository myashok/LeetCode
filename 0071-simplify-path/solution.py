class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = path.split('/')
        ans = []
        for folder in folders:
            if folder == "" or folder == '.':
                continue

            if folder == '..':
                if ans:
                    ans.pop()
                    
            else:
                ans.append(folder)

        return "/" + "/".join(ans)
