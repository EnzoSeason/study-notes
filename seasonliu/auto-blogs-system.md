# A blogs system with github webooks

As a developer, I like learning and sharing new technology. However, I find it wastes a lot time to copy my notes and post them on blogs websites like medium. So, I decide to create my own blog site.

My blog site should **publish my notes automatically**, without posing them by hand. That means, when I take some notes, these notes should be presented in my blog sites without extra action. Awesome, right ? Let's do it.

## Structure

Beforing coding, let's think about what I gonna build.

First of all, I need a place to store my notes. **Github** is the best choice. We can push any file to Github easily, and Github shares them. So, I just need to do `git push`, then my notes are available online. That's it, job is done.

ahah, I'm kinding. There are some limits of Github to show the blogs. 

First, It can't clearly show the extra information, such as the author, the updated date, the topic of notes, etc. We need a **back office** to track these.

Secondly, UI of the Github isn't suitable for blogs. I want to a nice UI like that of *Medium*. So, I should create a **front page**, too.

In conclusion, I need to build:

- a public Github repository to store my notes

- a back-end to track my notes

- a front-end to present my notes

## Needs

I've known what I want to build. It's time to discuss what we need to do.

First, I need to decide **the format of my notes**. Although Github can serve all kinds of file, it isn't easy to share some of them, such as word, excel, etc. 

I use **markdown**. There are 2 reasons.

1. Github serves the pure markdown file. There isn't any extra information in it.

2. Markdown file can be parsed into html file easily. It reduces a lot of work at the front-end.

Then, I need a **back-end**. It should: 
 
- listen to my Github repository

  When there is a `git push`, it should know.

- keep `push events` in records

  It should know who creates the note, when it's created, what is the note url, etc, and keep the records in database.

- share records

  These records should be sent to front-end.

Finally, **Front-end**. It needs to parse markdown into html and present them.

## Tools

Since I've figured out the needs. I should choose my tools.

I use `Django` to build back-end. Django is written by Python. It makes development so fast. I love Python, and I love this framework.

`Next js` is my front-end framework. It uses `React`. The interesting point of this framework is that it **creates html files when it's built**. It reduces the size of the site and time of the response. Downside is it isn't real-time updated. We need to rebuild the site to show the new blogs. 

`Next js` provides Server-Side-Rendering to do instant update. That makes this framework more interesting. But, I don't really need it because my blog site don't need the real-time update. A update a week is fine.

## Details

There are a lot of details to build a website, and most of them are boring. However, some points are very interesting.

### Listen to Github repository

The repository of Github provides **webhooks**. When there is a `push event`, webhooks will send this event to all the listener. That's the key point of the whole blog system.

To build it, I did 3 things:

1. create a listener in **back-end**

   The listener includes decrypting webhooks secret key, reading events, save events' info to database. I may write another article to present all the details.

2. regirster the listener in **webhooks**

3. setting the **secret key** of the webhooks

### Send notification to site admin

Once a `push event` is traited by back-end, back-end will send a notification to site admin. It reminds admin to rebuild the front-end. 

The notification can be an email. I use **slack incoming webhooks** to send a message in slack.

### Parse markdown files into html

When an admin rebuilds the front-end, front-end does a couple of things:

1. call back-end to get records of all the notes

   The records contains all the details of the notes, such as author, updated date, topic, etc. Most importantly, the **url of markdown file** in Github repository

2. call Github repository to fetch all the markdown file

3. parse markdown into html

   It's important to understand that this action ONLY happens when building the site. New notes in Github repository won't presented in blog site util the site is rebuilt.
  
4. create urls of all the html files

   In production, I need to `node server` to serve this front-end. The server will send the html files according to the client resquests.

## Conclusion

I built a blog site using Github webhooks. 

I pushed all my **markdown** notes to my public Github repository. Then Github will send the `push event` to my **back-end** through **webhooks**. 

My **back-end** saves the event into database. Once it's done, back-end will send a notification in **slack**. It tells site admin to rebuild the front-end.

When front-end is rebuilt, it will get notes' details from back-end and notes' markdown files from Github repository. It parses all the data and generates the html files.

Volia, It's how my blog site works. Thanks for reading and see you next time.

