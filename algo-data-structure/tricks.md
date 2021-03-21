# Tricks

## Slow-Fast pointers

We can use 2 pointers to traverse a **linked list**. That can reduce complexity.

The **interval** between 2 pointers is important.

- fixed interval
    
    For example, [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/). 
    
    We set the interval as `n`. When `fast` pointer is None, we return the `slow` pointer. 
    
    > `slow` pointer should be initialized as a dummy node pointed to the head of the list.

- varied interval

    For example, [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/).

    The step of the `fast` pointer should be **twice** as the `slow` one.