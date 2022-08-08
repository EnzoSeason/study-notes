# Delegate

Delegate is a pointer to **a method** or a **group of the methods**.

```c#
public class PhotoProcessor
{
  public delegate void PhotoFilterHandler(Photo photo);

  public void Process(string path, PhotoFilterHandler handler)
  {
    var photo = Photo.Load(path);
    handler(photo);
    photo.save();
  }
}
```

There are 2 delegates in `.NET` (`Action` and `Func`).

- Action: It can point to the **method which doesn't return a value**.
- Func: It can point to the **method which returns a value**.

```c#
public class PhotoProcessor
{
  public void Process(string path, Action<Photo> handler)
  {
    var photo = Photo.Load(path);
    handler(photo);
    photo.save();
  }
}
```

## Lambda expression

```c#
Func<int, int> square = num => num * num;
```

## Event

Event is a design for communicating between classes.

There are 3 steps:

1. define a delegate
2. create an event based on the delegate
3. raise the event

```c#
public class VideoEncoder
{
  // 1. define a delegate
  public delegate void VideoEncodedEventHandler(object source, EventArgs args);

  // 2. create an event based on the delegate
  public event VideoEncodedEventHandler VideoEncoded;

  // 3. raise the event
  protected virtual void OnVideoEncoded()
  {
    if (VideoEncoded != null)
    {
      VideoEncoded(this, EventArgs.Empty);
    }
  }
}
```

The subscriber is:

```c#
public class MailService
{
  public void OnVideoEncoded(object source, EventArgs args)
  {
    // TODO
  }
}
```

```c#
// publisher
var videoEncoder = new VideoEncoder();
// subscriber
var mailService = new MailService();

// MailService subscribes the VideoEncoded event of videoEncoder.
videoEncoder.VideoEncoded += mailService.OnVideoEncoded;
```

To make it easier, we can use the delegate in `.NET`.

```c#
// public delegate void VideoEncodedEventHandler(object source, EventArgs args);
// public event VideoEncodedEventHandler VideoEncoded;
public event EventHandler VideoEncoded;
```

This is also a generic type. `EventHandler<TEventArgs>`.
