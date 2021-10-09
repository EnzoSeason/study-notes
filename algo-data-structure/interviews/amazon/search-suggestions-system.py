from typing import List


class SolutionBruteForce:
    """
    https://leetcode.com/problems/search-suggestions-system/
    """

    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        res = []

        for i in range(1, len(searchWord) + 1):
            prefix = searchWord[:i]
            suggestions = []
            for w in products:
                if w.startswith(prefix):
                    suggestions.append(w)
            res.append(sorted(suggestions)[:3])

        return res


class SolutionBinarySearch:
    def binarySearch_left(self, products: List[str], searchWord: str, lo: int) -> int:
        l, r = lo, len(products) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if products[mid] == searchWord:
                return mid
            if products[mid] < searchWord:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        products.sort()

        res = []
        prefix = ""
        lo = 0

        for char in searchWord:
            prefix += char
            #  lo = bisect.bisect_left(products, prefix, lo)
            lo = self.binarySearch_left(products, prefix, lo)
            suggestions = [
                word for word in products[lo : lo + 3] if word.startswith(prefix)
            ]
            res.append(suggestions)

        return res