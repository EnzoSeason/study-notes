# First interview

## Reconstruct CRM robot

We have a CRM Application, Pipedrive. It tracks all the projects of our company. I've created a CRM robot. It used pipedrive webhooks to listen all the events on the pipedrive. and then it will make reactions, such as sending an email, assigning an activity to the people.

At the beginning, CRM rotbot is designed for a single pipeline. As the bussiness grows, our companies more and more projects, so I reconstructed the entire system to fit multi-pipelines.

I changed the coding style, from Oriented Process to Oriented Object. Before, the robot had only one class to do all the work. Now, I split it into 3 types of classes, webhooks controllers, pipelines controllers and content controllers. 

Webhooks controllers are created according to webhooks endpoints. For exemple, there is an endpoint for updated deals on the Pipedrive. Then I created an UpdateDealController. All these classe need to check whether the event can be traited by the robot. We have a whitelist for deals and orgnizations. Therefore, I create an abstract class to provide this check method. All the webhooks controllers inherit this class. After checking, the events will be send to proper pipelines controllers. That means webhooks controllers compose pipelines controllers.

Pipelines controllers are created according to the pipelines on the pipedrive. For exemple, we have a pipeline called Order to Cash. So I've created a OrderToCashController. There are no common method can be shared between the Pipelines controllers, so there is no abstract class. However, there are common types of method need to be implemented in each classes, such as dealChangeReaction, OrgnizationChangeReaction, etc. So, I create an interface, which makes sure these methods are well implemented.

Once the event is passed into a method of a pipedrive controller, such as dealChangeReaction. A deal controller will take the job. It will make the reaction happen, like sending an email, assigning the activity, updating the deal both in the Pipedrive and Database, etc. These are classes are created according to data type on the pipedrive, such as deals, orgnizations, persons, etc. and we've got the same data type in our database. There are common methods to communicate with the Pipedrive and the database. So I create an abstract class for them. To pass the events into these controllers, I let the pipeline controller to compose them.

With this architecture, it's very easy to add a pipeline or add the new reaction in a pipeline. To sum up, there are 3 roles when I designe this system.

1. If there have common methods can be shared among the classes, I will create an abstract class.
2. If there have common methods need to be implemented by the classes, I will create an interface.
3. If I need to pass the data from one class to another, I will let a class to compose another one.
