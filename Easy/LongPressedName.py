class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        groups_name = []
        groups_name_count = []
        prev = None
        for c in name:
            if c != prev:
                groups_name.append(c)
                prev = c
                groups_name_count.append(1)
            else:
                groups_name_count[-1] = groups_name_count[-1] + 1

        groups_typed = []
        prev = None
        groups_typed_count = []
        for c in typed:
            if c != prev:
                groups_typed.append(c)
                prev = c
                groups_typed_count.append(1)
            else:
                groups_typed_count[-1] = groups_typed_count[-1] + 1

        if groups_name != groups_typed:
            return False

        for i, j in zip(groups_name_count, groups_typed_count):
            if i > j:
                return False

        return True