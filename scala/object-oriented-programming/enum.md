## Enum

```scala
enum Permissions {
  case READ, WRITE, EXECUTE, NONE
}

val somePermission = Permissions.READ
```

### Enum APIs

1. `ordinal`: the index of enum

   ```scala
   println(somePerission.ordinal) // 0. Because it's the first enum in Permissionss.
   ```

2. `values`: the list of all enums

   ```scala
   val allEnums = Permissions.values
   ```

3. `valueOf`: the Enum get from `String`

   ```scala
   val readEnum = Permission.valueOf("READ") // Permissions.READ
   ```
