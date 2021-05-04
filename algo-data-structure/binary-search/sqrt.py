# https://leetcode.com/problems/sqrtx/
def sqrt_binary_search(x: int) -> int:
    if x == 0 or x == 1:
        return x
    left, right = 1, x
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            if (mid + 1) *  (mid + 1) > x:
                return mid
            left = mid + 1
        else:
            right = mid - 1

def sqrt_newton(target: int) -> int:
    """
    Newton:
    
    Suppose y = f(x), then
    y = f'(x - xn)x + f(xn)
    
    f(xn+1) = 0, then
    xn+1 = xn - f(xn)/f'(xn)

    This question can be transformed into finding the root of the function
    y = x^2 - target

    The recursion is:
    x0 = target (This init makes sure xn+1 < xn.)
    xn+1 = (xn + target/xn) / 2
    """
    root = target
    while root * root > target:
        root = (root + target // root) // 2
    return root