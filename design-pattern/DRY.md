# DRY

Don’t Repeat Yourself.

- Logical duplication: Solving by abstracting into a **more fine-grained function**.

  For example: Both `isValidUsername()` and `isValidPassword()` can use the fine-grained function `canContain()`.

- Functional semantic duplication: Solving by removing the duplicated function.

- Duplicate code execution: Solving by removing the duplicated execution.

## Code Reusability

When we develop new features, we try to reuse existing code as much as possible.

The difference between **reusability and not duplication** is that "not duplication" doesn't make sure reusability.

To improve the code reusability:

- decouple the codes

- use single responsibility principle

- encapsulate into modules

- split bussiness and non-bussiness logic

- put the generic codes to lower layer, avoid the low layer class to use high layer class.

- use OOP and design pattern

However, Code Reusability costs time to design. We can apply **the rule of three**:

When we write the code for the first time, we don’t consider reusability.
When we encounter the reuse scene for the second time, we refactor to make it reuse.
