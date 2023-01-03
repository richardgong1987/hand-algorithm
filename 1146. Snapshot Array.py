from collections import defaultdict


class SnapshotArray:
    def __init__(self, length: int):
        self.snaps = defaultdict(dict)
        self.snap_cnt = 0

    def set(self, index: int, val: int) -> None:
        self.snaps[self.snap_cnt][index] = val

    def snap(self) -> int:
        self.snap_cnt += 1
        return self.snap_cnt - 1

    def get(self, index: int, snap_id: int) -> int:
        cur = snap_id
        while cur > 0 and index not in self.snaps[cur]:
            cur -= 1
        if index in self.snaps[cur]:
            return self.snaps[cur][index]
        return 0


snapshotArr = SnapshotArray(3)

command = ["SnapshotArray", "set", "snap", "snap", "snap", "get", "snap", "snap", "get"]
values = [[1], [0, 15], [], [], [], [0, 2], [], [], [0, 0]]
Expected = [None, None, 0, 1, 2, 15, 3, 4, 15]
Output = [None, None, 0, 1, 2, 0, 3, 4, 15]

for i, val in enumerate(command):

    if val == 'SnapshotArray':
        snapshotArr = SnapshotArray(values[i][0])
    if val == 'set':
        snapshotArr.set(values[i][0], values[i][1])
    if val == 'snap':
        rs = snapshotArr.snap()
        print(Expected[i] == rs, f'snap i={i}')
    if val == 'get':
        rs = snapshotArr.get(values[i][0], values[i][1])
        print(Expected[i] == rs, f'get i={i}')
