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