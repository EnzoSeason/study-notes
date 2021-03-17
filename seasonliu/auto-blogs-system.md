# A blogs system with Github webhooks

As a developer, I like learning and sharing new technology. However, I find it wastes a lot of time to copy my notes and post them on blogs websites like medium. So, I decided to create my own blog site.

My blog site should **publish my notes automatically**, without posing them by hand. That means, when I take some notes, these notes should be presented on my blog sites without extra action. Awesome, right? Let's do it.

## Structure

Before coding, let's think about what I gonna build.

First of all, I need a place to store my notes. **Github** is the best choice. We can push any file to Github easily, and Github shares them. So, I just need to do `git push`, then my notes are available online. That's it, the job is done.

aha, I'm kidding. There are some limits of Github to show the blogs. 

First, It can't clearly show the extra information, such as the author, the updated date, the topic of notes, etc. We need a **back-office** to track these.

Secondly, the UI of Github isn't suitable for blogs. I want a nice UI like that of *Medium*. So, I should create a **front page**, too.

In conclusion, I need to build:

- a public Github repository to store my notes

- a back-end to track my notes

- a front-end to present my notes

## Needs

I've known what I want to build. It's time to discuss what we need to do.

First, I need to decide **the format of my notes**. Although Github can serve all kinds of files, it isn't easy to share some of them, such as word, excel, etc. 

I use **markdown**. There are 2 reasons.

1. Github serves the pure markdown file. There isn't any extra information in it.

2. Markdown files can be parsed into HTML files easily. It reduces a lot of work at the front-end.

Then, I need a **back-end**. It should: 
 
- listen to my Github repository

  When there is a `git push`, it should know.

- keep `push events` in records

  It should know who creates the note, when it's created, what is the note URL, etc, and keep the records in the database.

- share records

  These records should be sent to the front-end.

Finally, **Front-end**. It needs to parse markdown into html and present them.

## Tools

Since I've figured out the needs. I should choose my tools.

I use `Django` to build the back-end. Django is written by Python. It makes development so fast. I love Python, and I love this framework.

`Next.js` is my front-end framework. It uses `React`. The interesting point of this framework is that it **creates HTML files when it's built**. It reduces the size of the site and the time of the response. The downside is it isn't real-time updated. We need to rebuild the site to show the new blogs. 

However, `Next.js` provides Server-Side-Rendering to do instant updates. That makes this framework more interesting. But, I don't really need it because my blog site doesn't need real-time updates. An update a week is fine.

## Details

There are a lot of details to build a website, and most of them are boring. However, some points are very interesting.

### Listen to the Github repository

The repository of Github provides **webhooks**. When there is a `push event`, webhooks will send this event to all the listeners. That's the key point of the whole blog system.

To build it, I did 3 things:

1. create a listener in the **back-end**

   The listener includes decrypting webhooks secret key, reading events, save events' info to the database. I may write another article to present all the details.

2. register the listener in **webhooks**

3. setting the **secret key** of the webhooks

### Send notification to site admin

Once a push event is treated by the back-end, the back-end will send a notification to the site admin. It reminds the admin to rebuild the front-end.

The notification can be an email. I use **Slack incoming webhooks** to send a message in Slack.

### Parse Markdown files into HTML files

When an admin rebuilds the front-end, the front-end does a couple of things:

1. call the back-end to get records of all the notes

   The record contains all the details of the note, such as author, updated date, topic, etc. Most importantly, the **url of the markdown file** in the Github repository

2. call the Github repository to fetch all the Markdown files

3. parse Markdown files into HTML files

   It's important to understand that this action ONLY happens when building the site. New notes in the Github repository won't be presented on the blog site until the site is rebuilt.
  
4. create URLs of all the HTML files

   In production, I need to node server to serve this front-end. The server will send the Html files according to the clients' requests.

## Conclusion

I built a blog site using Github webhooks. 

I pushed all my **Markdown** notes to my public Github repository. Then Github will send the `push event` to my **back-end** through **webhooks**. 

My **back-end** saves the event into the database. Once it's done, the back-end will send a notification in **Slack**. It tells the site admin to rebuild the front-end.

When the front-end is rebuilt, it will get notes' details from the back-end and notes' markdown files from the Github repository. It parses all the data and generates the HTML files.

Voila, It's how my blog site works. Thanks for reading and see you next time.

