from typing import List


class File:
    def __init__(self):
        self.is_file = False
        self.content = ""
        self.files = dict()


class FileSystem:
    """
    https://leetcode.com/problems/design-in-memory-file-system/
    """

    def __init__(self):
        self.root = File()

    def ls(self, path: str) -> List[str]:
        node = self.root

        #  find the lowest dir or file
        if path != "/":
            dirs = path.split("/")
            for d in dirs[1:]:
                node = node.files[d]
            if node.is_file:
                return [dirs[-1]]

        files = list(node.files.keys())
        return sorted(files)

    def mkdir(self, path: str) -> None:
        node = self.root
        dirs = path.split("/")

        for d in dirs[1:]:
            if d not in node.files:
                node.files[d] = File()
            node = node.files[d]

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root
        dirs = filePath.split("/")
        file = dirs.pop()

        for d in dirs[1:]:
            node = node.files[d]

        if file not in node.files:
            node.files[file] = File()

        node = node.files[file]
        node.is_file = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root
        dirs = filePath.split("/")
        file = dirs.pop()

        for d in dirs[1:]:
            node = node.files[d]

        return node.files[file].content


#  Your FileSystem object will be instantiated and called as such:
#  obj = FileSystem()
#  param_1 = obj.ls(path)
#  obj.mkdir(path)
#  obj.addContentToFile(filePath,content)
#  param_4 = obj.readContentFromFile(filePath)