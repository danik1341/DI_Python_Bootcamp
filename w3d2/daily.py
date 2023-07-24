import math


class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items is not None else []
        self.pageSize = int(pageSize)
        self.totalPages = math.ceil(len(self.items) / self.pageSize)
        self.currentPage = 1 if self.totalPages > 0 else 0

    def getVisibleItems(self):
        start_idx = (self.currentPage - 1) * self.pageSize
        end_idx = start_idx + self.pageSize
        return self.items[start_idx:end_idx]

    def nextPage(self):
        self.currentPage = min(self.currentPage + 1, self.totalPages)
        return self

    def prevPage(self):
        self.currentPage = max(self.currentPage - 1, 1)
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum, pageSize=None):  # Add pageSize as a parameter
        self.totalPages = math.ceil(
            len(self.items) / (self.pageSize if pageSize is None else pageSize))
        self.currentPage = max(min(int(pageNum), self.totalPages), 1)
        return self


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.getVisibleItems())  # Output: ['a', 'b', 'c', 'd']

p.nextPage().nextPage()
print(p.getVisibleItems())  # Output: ['i', 'j', 'k', 'l']

p.prevPage().prevPage()
print(p.getVisibleItems())  # Output: ['a', 'b', 'c', 'd']

p.firstPage()
print(p.getVisibleItems())  # Output: ['a', 'b', 'c', 'd']

p.lastPage()
print(p.getVisibleItems())  # Output: ['y', 'z']

p.goToPage(10, 4)  # Update the pageSize to 4
print(p.getVisibleItems())  # Output: ['y', 'z']
print(p.currentPage)  # Output: 7
