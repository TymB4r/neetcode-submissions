class TimeMap:

    def __init__(self):
        self.key_to_record = {} # str -> List[(int, str)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_to_record:
            self.key_to_record[key] = []
        self.key_to_record[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_record:
            return ""

        record = self.key_to_record[key]

        if record[0][0] > timestamp:
            return ""
        if record[-1][0] <= timestamp:
            return record[-1][1]

        left, right = 0, len(record) - 1
        while right - left > 1:
            mid = (left + right) // 2

            if record[mid][0] == timestamp:
                return record[mid][1]
            if record[mid][0] > timestamp:
                right = mid
            else:
                left = mid

        return record[left][1]