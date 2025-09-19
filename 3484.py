class Spreadsheet:
    def __init__(self, rows: int):
        self.ss = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.ss[cell] = value

    def resetCell(self, cell: str) -> None:
        self.ss[cell] = 0

    def getValue(self, formula: str) -> int:
        expr = formula[1:]
        match = re.match(r"([A-Z]+\d+|\d+)\+([A-Z]+\d+|\d+)", expr)

        left, right = match.groups()

        left_val = int(left) if left.isdigit() else self.ss[left]
        right_val = int(right) if right.isdigit() else self.ss[right]

        return left_val + right_val
