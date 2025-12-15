class table:
    def __init__(self, name: str, col: int):
        self.col = col
        self.name = name
        self.idx = 0
        self.rows = {}

    def insert(self, row: List[str]):
        self.idx += 1
        self.rows[self.idx] = row

    def remove(self, row_id: int):
        if row_id in self.rows:
            del self.rows[row_id]


class SQL:
    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {}
        for i in range(len(names)):
            tab = table(names[i], columns[i])
            self.tables[names[i]] = tab

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.tables:
            return False

        if self.tables[name].col != len(row):
            return False

        self.tables[name].insert(row)

        return True

    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.tables:
            return

        return self.tables[name].remove(rowId)

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables:
            return "<null>"

        if rowId not in self.tables[name].rows:
            return "<null>"

        if 0 <= columnId <= self.tables[name].col:
            row = self.tables[name].rows[rowId]
            return row[columnId - 1]

        return "<null>"

    def exp(self, name: str) -> List[str]:
        if name not in self.tables:
            return []

        output = []
        for k, v in self.tables[name].rows.items():
            out = str(k)
            for cell in v:
                out += "," + cell
            output.append(out)

        return output


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)
