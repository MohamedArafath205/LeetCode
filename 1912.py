from sortedcontainers import SortedList
class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.movie = defaultdict(SortedList)
        self.rented = SortedList()
        self.price_map = {}
        for s, m, p in entries:
            self.movie[m].add((p,s))
            self.price_map[(s,m)] = p

    def search(self, movie: int) -> List[int]:
        res = []
        for p,s in self.movie[movie][:5]:
            res.append(s)
        return res

    def rent(self, shop: int, movie: int) -> None:
        p = self.price_map[(shop, movie)]
        self.movie[movie].remove((p,shop))
        self.rented.add((p,shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        p = self.price_map[(shop, movie)]
        self.rented.remove((p,shop,movie))
        self.movie[movie].add((p,shop))

    def report(self) -> List[List[int]]:
        res = []
        for p,s,m in self.rented[:5]:
            res.append([s,m])
        return res
