class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_file_name = defaultdict(list)
        for path in paths:
            path, *files = path.split(' ')
            for f in files:
                name, content = f.split('(')
                content_to_file_name[content].append(path + '/' + name)
        return [c for c in content_to_file_name.values() if len(c) > 1]

