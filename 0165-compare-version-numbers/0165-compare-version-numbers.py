class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_set=version1.split(".")
        version2_set=version2.split(".")
        max_length=max(len(version1_set),len(version2_set))
        version1_set += ['0'] * (max_length - len(version1_set))
        version2_set += ['0'] * (max_length - len(version2_set))
        # print(version1_set,version2_set)
        for i in range(len(version1_set)):
            if int(version1_set[i])< int(version2_set[i]):
                return -1
            elif int(version1_set[i])> int(version2_set[i]):
                return 1
        return 0
            