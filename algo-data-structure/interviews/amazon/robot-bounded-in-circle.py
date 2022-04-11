class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dx, dy = 0, 1  ## orientation vector

        for ins in instructions:
            ## rotation matrix
            ## new_x = consO * old_x - sinO * old_y
            ## new_y = sinO * old_x + consO * old_y
            if ins == "L":
                dx = 0 * dx - 1 * dy
                dy = 1 * dx + 0 * dy
            elif ins == "R":
                dx = 0 * dx - (-1) * dy
                dy = (-1) * dx + 0 * dy
            elif ins == "G":
                x, y = x + dx, y + dy

        return (x, y) == (0, 0) or (dx, dy) != (0, 1)