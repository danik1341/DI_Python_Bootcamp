class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items is not None else []
        self.pageSize = int(pageSize)
        self.currentPage = 1
        self.totalPages = len(self.items) // self.pageSize + 1

    def getVisibleItems(self):
        if self.currentPage < 1:
            self.currentPage = 1
        if self.currentPage > self.totalPages:
            self.currentPage = self.totalPages
        start_idx = (self.currentPage - 1) * self.pageSize
        end_idx = start_idx + self.pageSize
        return self.items[start_idx:end_idx]

    def firstPage(self):
        self.currentPage = 1

    def lastPage(self):
        self.currentPage = len(self.items) // self.pageSize + 1

    def nextPage(self):
        self.currentPage += 1

    def prevPage(self):
        self.currentPage -= 1

    def goToPage(self, pageNum):
        self.currentPage = max(min(int(pageNum), self.totalPages), 1)


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

# Test getVisibleItems()
print(p.getVisibleItems())  # Output: ['a', 'b', 'c', 'd']
# Test nextPage() and getVisibleItems()
p.nextPage()
print(p.getVisibleItems())  # Output: ['e', 'f', 'g', 'h']
# Test prevPage() and getVisibleItems()
p.prevPage()
print(p.getVisibleItems())  # Output: ['a', 'b', 'c', 'd']
# Test firstPage() and getVisibleItems()
p.firstPage()
print(p.getVisibleItems())  # Output: ['a', 'b', 'c', 'd']
# Test lastPage() and getVisibleItems()
p.lastPage()
print(p.getVisibleItems())  # Output: ['y', 'z']
# Test goToPage() and getVisibleItems()
p.goToPage(10)
print(p.getVisibleItems())  # Output: ['y', 'z']
print(p.currentPage)  # Output: 5
# Test goToPage() with an invalid page number and getVisibleItems()
p.goToPage(-2)
print(p.getVisibleItems())  # Output: ['a', 'b', 'c', 'd']
print(p.currentPage)  # Output: 1
# Test an empty list of items and getVisibleItems()
empty_list = []
p = Pagination(empty_list, 5)
print(p.getVisibleItems())  # Output: []
# Test a single page and getVisibleItems()
single_page_list = [1, 2, 3, 4, 5]
p = Pagination(single_page_list, 5)
print(p.getVisibleItems())  # Output: [1, 2, 3, 4, 5]
# Test items less than pageSize and getVisibleItems()
short_list = [1, 2, 3]
p = Pagination(short_list, 5)
print(p.getVisibleItems())  # Output: [1, 2, 3]
