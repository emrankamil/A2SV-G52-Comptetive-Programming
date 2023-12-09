class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        allFiles = {}

        for singlePath in paths:
            parts = singlePath.split()
            directory = parts[0]
            for file in parts[1:]:
                index1, index2 = file.find("("), file.find(")")
                fileName = file[index1:index2 + 1]
                if fileName in allFiles:
                    allFiles[fileName].append(directory + '/' + file[:index1])
                else:
                    allFiles[fileName] = [directory + '/' + file[:index1]]

        output = [values for values in allFiles.values() if len(values) > 1]

        return output
