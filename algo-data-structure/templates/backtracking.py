class Solution:
    """
    Backtracking can be seen as the traversal of a graph.

    It traverses horizontally and vertically.
    """

    def backtraking(self, params, res) -> None:
        #  The end condition of recursion.
        #  Collect the result.
        if self.isEnd(params):
            res.append(params)
            return
        
        #  The iteration here is the horizontal traversal.
        for item in params:
            new_item = self.process(item)
            #  The recursion here is the vertical traversal.
            self.backtraking(new_item, res)

    def isEnd(self, params) -> bool:
        pass

    def process(self, item) -> None:
        pass