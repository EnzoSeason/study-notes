## First interview

### Reconstruct CRM robot

We have a CRM Application, Pipedrive. It tracks all the projects of our company. I've created a CRM robot. It used pipedrive webhooks to listen all the events on the pipedrive. and then it will make reactions, such as sending an email, assigning an activity to the people.

At the beginning, CRM rotbot is designed for a single pipeline. As the bussiness grows, our companies more and more projects, so I reconstructed the entire system to fit multi-pipelines.

I changed the coding style, from Oriented Process to Oriented Object. Before, the robot had only one class to do all the work. Now, I split it into 3 types of classes, webhooks controllers, pipelines controllers and content controllers.

Webhooks controllers are created according to webhooks endpoints. For exemple, there is an endpoint for updated deals on the Pipedrive. Then I created an UpdateDealController. These classes need to check whether the event can be processed by the robot, if yes, they pass the events to to the proper pipelines controllers. To do that, first, I created an abstract class, put the event check method in it, and let all webhooks controllers inherit it. So that, all of them can check event. Then, I initialized the instances of pipelines controllers in the webhooks controllers, let webhooks controllers compose pipelines controllers. So that, they can pass the data.

Pipelines controllers are created according to the pipelines on the pipedrive. For exemple, we have a pipeline called Order to Cash. So I've created a OrderToCashController. There are no common method can be shared between the Pipelines controllers.However, there are common types of method need to be implemented in each classes, such as dealChangeReaction, OrgnizationChangeReaction, etc. So, I create an interface, which makes sure these methods are well implemented.

Once the event is passed into a method, such as dealChangeReaction. A deal controller will take the job. It will make the reaction, like sending an email, assigning the activity, updating the deal both in the Pipedrive and Database, etc. These are classes are created according to data type on the pipedrive, such as deals, orgnizations, persons, etc. and we've got the same data type in our database. There are common methods to communicate with the Pipedrive and the database. So I create an abstract class for them. To pass the events into these controllers, I let the pipeline controller to compose them.

With this architecture, it's very easy to add a pipeline or add the new reaction in a pipeline. To sum up, there are 3 roles when I designe this system.

1. If there have common methods can be shared among the classes, I will create an abstract class.
2. If there have common methods need to be implemented by the classes, I will create an interface.
3. If I need to pass the data from one class to another, I will let a class to compose another one.

### Signature Detection

It's an application to detect signatures in a PDF file or an image.

#### Backend

If it's a PDF file, we transform it into images, and deal with the images one by one.

The image is process by following class in order. Loader, Extractor, Cropper, and Judger.

#### Loader
The loader reads the file and creates a mask. The mask is a numpy array. The bright parts are set to 255, the rest is set to 0. It contains ONLY these 2 numbers.

#### Extractor
The extractor, first, generates the regions from the mask. Then, it removes the small and the big regions because the signature is neither too big nor too small. The process is as followed.

1. label the image
2. calculate the average size of regions: `nb_pixels / nb_regions`
3. calculate the size of the small outlier: `small_size_outlier = average * outlier_weight + outlier_bias`
4. calculate the size of the big outlier: `big_size_outlier = small_size_outlier * amplfier`
5. remove the small and big outliers

##### Cropper

The cropper finds the contours of regions in the labeled masks and crop them. If the regions are overlapped, merge them.

##### Judger 

The judger reads the cropped mask and identifies if it's a signature or not.

I use 2 metrics: the ratio of height and width, the ratio of pixels.

##### Frontend

It's created by React. It allows

- show the detection results. (use svg, learn from AWS Textract)
- modify the region. They are chips in another card. We can drag a chip from signature zone to not signature zone, or simply delete the chip. So that, the region is removed.
- Add a region. open a canvas and draw a retangle.

##### Structure

The application has a frontend interface created by React, a backend api used Fastapi as the framework. The request is proxyed by Nginx. The entire app is shipped by Docker.

What's more, the online demo has a database to store the results. The regions and metadata of image are save in MySQL, and the file is saved in S3 of AWS.


