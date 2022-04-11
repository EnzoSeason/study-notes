# Asynchrony

Dart libraries are full of functions that return `Future` or `Stream` objects.

The `async` and `await` keywords support asynchronous programming.

## Handling Futures

```dart
Future<void> checkVersion() async {
  var version = await lookUpVersion();
  // Do something with version
}
```

## Handling Stream

```dart
Future<void> main() async {
  // ...
  await for (final request in requestServer) {
    handleRequest(request);
  }
  // ...
}
```
