#  Use Github webhooks

# #  Set up

# #  Github webhooks JSON response

We need to check the **markdown** files in github.

The url of raw markdown file is as follow:

```url
https://raw.githubusercontent.com/EnzoSeason/study-notes/main/{folder}/{markdown}.md
```

I want to map:

- folder => `Topic`
- markdown => `Note`

So, I need check 3 props in json response:

- `pusher`: We should asign `Note` to the `pusher`

- `commits`: 

  There are 3 different props in it, `added`, `removed`, `modified`. 
  
  There are arrays. Each item in array is `{folder}/{markdown}.md`.