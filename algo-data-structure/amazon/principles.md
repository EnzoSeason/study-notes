# Principles

## Why Amazon

I want to be an engineer who has deep understanding of the sofeware inductry. And I want to work and make friends with the best software engineers in the world. So, I need to go the top-class tech company, like Amazon.

## Principles

- **Customer Obsession**

  Pipedrive update button

  Situation: Product manager want to add feature, update deal's fields in Pipedrive. (Pipedrive is a CRM application.) The updated value is calculated by Doc generator which I created.

  Task: She wants a button below the data table. Once the user clicks it, it sends all the calculated value to the pipedrive.

  Action: I think a button is not enough. The user may want to modify some of the value. It's better to let them check or change the value before sending them to the Pipedrive. So, I told my product manage about this idea, waited her response before coding.

  Result: Product Manager was very happy about this idea. But, she didn't want our employées change the value, however, she let them chose which value to update

  Finally, I created diaglog, which lists all the calculated values. There is a checkbox in front of each value. All of them are selected by default. At the end of the diaglog, there is a button to send them to pipedrive.

- **Ownership**

  The sense of owner of a project.

  Situation: At the beginning, CRM rotbot works for a single pipeline. A pipeline represents a type of the projects. As the bussiness grows, our companies has different types of projects. However, the CRM is not designed for multi-pipelines. So I asked my tech leader to reconstrust the CRM robot.

  Task: The aim of the restruction is to split a single pipedrive webhooks controller into differents classes. There are 3 types of classes, webhooks controller, pipeline controller and context controller. webhooks controllers, they listens to the events, such as deal updated, activity updated, and send them to pipeline controllers. Pipeline controllers deal with all the events in its own line. There are 3 major events. updated deal, update activity and update organisation. I created deal controller, activity controller and orgnation controller to process them. They all inherit the context controller since some method is same, like get data from pipedrive, update the data in Pipedrive, save data in the database.

  Action: I told my tech leader about that, and wrote a report to explain how the new system works.

  Result: The tech leader is happy. He lets me do it. But he want to makes sure the new system works. I wrote unit tests for all the context controllers, 100% line coverage. It proves all the data processing is correct.


  situation: The component is more and more complex while more and more feature is added. It becomes difficult to maintain

  task: I encourage other developpers to split the giant components into small ones.

  Action: First, I created a exemple. At the list page, I split the list and filters into 2 differents components. I define how these two component communicate each other. Then, I wrote an article about how I created this exemple. Finally, I sent this article to my tech leader. He was happy to see it, and he shares it with the teams.

  Result: Our team use my method, it becomes easier to maintain the list component.

- **Invent** and **Simplify**

  Invent the stuff to simplify jobs.

  situation: When I coded a new doc generator, I copies the old codes of the old one. It's exusted. So, I want to build a Command Line Interface, to initialize the doc generator.

  Task: I need to tool to initialize the frontend and the backend together.

  Action: I found a node tool, Yeomen. It can read all kinds of template and create the new file according to the template and user input. That is exactly what I need. I learnt Yeoman, create a template of doc generator, and use it in my daily work.

  result: This tools reduce a huge amount of time. It improves my dev experience.

- **Are right, A Lot**

  Situation: In my first intership, my mentor let my do some research on Flutter, to see whether we can build a mobile app to show a list of our company tweets. Back then, Flutter is very new, Its version is 0.1.

  Action: I didn't hesited, and put my all effort into the research. Flutter uses a new language, Dart. It didn't stop me. I spent a morning to learn the basic usage and I use an afternoon to create a first demo according to the Flutter official tutorial. At the end of intership. This application show the tweets in different categories, and it opens a web view when the user taps on a tweet.

- **Learn** and **Be Curious**

  Situation: I've never stopped learning. I've been study everyday since the day I entered Enerlis, my current company.

  Action: When I entered Enerlis, I used 2 months to learn the tech-stacks: Angular, nignx, Api plateform (A PHP restful api framework) and MySQL, to make sure there is no problem to solve an issue individually. Then, I started to learn the knowledge systematically. I started from the front-end. I learned HTML, CSS, typescript, and forcused on valia JavaScript. I learnt not only its basic usage, but also some advanced technique, such as closure, prototype link, etc. Once I finished it, I moved to React. The reason I choose React. first, it's completely different to Angular, which is very interesting. Second, I want to have other tech-stack besides the one of my company. It's also why I choose Python as my backend language rather than PHP. After finish frontend, I studies backend. At the same time, I started to training the algorithmes and data structure.

  Result: I can build a web or mobile app independently. The trainning of the algorithmes and data structure improves my code quality.

- **Hire** and **Develop** the Best

- Insist on the **Highest Standards**

  Situation: coding the open-source python project

  Task: write readable and maintainable codes

  Action: use tying as much as possible. If one line of code can solve the problem and it's readable, never write the second line. When naming a variable and the function, think twice about its meaning. make README simple, clean and interesting (add gif image).

  Result: Everything is in order, I feel great.

- **Think Big**

  Situation: When I make the interface of signature-detection, I have no idea how to display the signature region. I know like the UI of Textract, a service of AWS.

  Task: I create the same UI as Textract.

  Action: I inspected the HTML file using chrome DevTool. I found it used svg and path element to display a retrangle. Then, I checked these elements on MDN website. And I found an easier way, rect element. It's a retrangle, amazing. Next, I checked the CSS of textractor's retrangle, and I modified a little to match my website primary and secondary color. Finally, I want the user can draw a retrangle. This feature isn't available on Textractor. But I found how to do by reading  MDN documents. I used canvas elements to pull it off.

  Result: I learnt from Textract and improved it by digging into MDN website.

- **Bias for Action**:

  Situation: It's my working style. I asked for the new and challenging projects, such as CRM robot, signature detecion, etc. There hasn't a perfect solution on Internet. I need to come out a way to solve them.

  Task: create a first demo as fast as possible, as simple as possible. but It must meet the basic need.

  Action: I'll, first, discussed with the tech leader to figure out the major features. Then, I focused on them only. Once finished, I'll show it to the tech leader, getting the feedback, then improve it. The prodution doesn't need to be perfect at once, but it should have frequent update.


- **Frugality**

- **Earn Trust**

  Situation: When I have a disagreement with my manager, I'll try to explain my idea to he and listen to his idea. Signature-detection was a company project at first. I've reached to crop the regions which may be the signature. I want to move to the next step, collect the labeled the regions to train a CNN classification model. I want to create a captcha. When our employées log in, they need to select the signature from the cropped images. I told this idea to my Tech Leader. He rejected it. He thought there is no need to move forware.

  Action: I was sad about that. My manager explaint we don't have enough time to do that. We needed to check all the contracts in 3 days. We've recruited some people to check the files mannually. It's a cool idea to build a CNN model, unfortunatly, company doesn't need it anymore. I accepted it. 
  
  Result: Then, I asked for him can I turn this project into my personnal project and make it open-source. He said OK. That's how we have current signature-detection.

- **Dive Deep**

  Dive Deep is what I miss, and I'm working on it.

  Situation: CRM robot uses pipedrive webhooks to listen to the event on the Pipedrive. Now, we use it only for making reaction, such as sending email, assigning an activity, and simply updating the status.

  Task: We can use it for monitoring the bussiness in the real-time. For exemple, We can know how many deals the commerical department receives in one day, or how much deal the condustor have done in one day.

  Action: For now, it's just my idea. I think I can add a function in the controller to do this statistic job. Since it's in real-time, I need to calculate and save the results quickly. There are no heavy calculation, but IO takes a lot of time. Especially saving data in MySQL database. Therefore, I need a cache system to save them. When CRM robot receives an event, I lanuch the calculation, and save results into the cache. What if the user want to know the statisque information in a long-term, a month, a year. Then cache is out. I should save the data into database. What I can do it create a process to write the data from cache to database periodically.


  Result: If we have the data of short-term, which is in the cache and long-term, which is in the database. We may have a better understanding of our bussiness.

- Have Backbone; Disagree and Commit

  say disgreement, the same exemple as before.

- Deliver Results

  situation: Previously, one of our developpers created a feature, list all the photovoltaique projects page by page. He fetched all the projects from the server and split them in pages at client-side. It becomes slower and slower while we had more and more projects. Finally, It takes more than 1 minutes to show the list. My manager let he to improve to, but he don't know how. I stood up.

  Task: instead of client-side pagination, use server-side pagination

  Action: The idea only fetch the project of current page and cache the projects of previous pages. To fetch the projects, I set itemPerPage and page number in the parameters query. Thank to api platform, the pagination at back-end is already implemented, no more code to write. To cache the projects, I use a list the save all fetched project, a hash map to track whether the projects of page i is fetched, and the variable, current page numbers, itemPerpage to show the projects.

  Result: I solve it in one days, recreate the filters in the second day. Our commercial team is happy about the result.