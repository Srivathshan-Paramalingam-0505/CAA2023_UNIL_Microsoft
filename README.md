# CAA2023_UNIL_Microsoft Cloud x IoT : GPS for bikers
*This is our attempt to develop a GPS for bikers using the M5Stack Core2 device connected to the GPS unit and APIs from the Google Cloud Platform*

<img width="649" alt="Screenshot 2023-05-25 at 11 21 08" src="https://github.com/Srivathshan-Paramalingam-0505/CAA2023_UNIL_Microsoft/assets/83650518/74967780-58ee-4243-9e4a-c4a76ba07e32">

## Summary
This project aimed to implement a GPS within the M5Stack Core2 device for the bikers to travel around without being distracted by the overflowing informations coming from a smartphone. Here is a list of the different files we created for this project.
* Colab notebook
* Micropython files
* Cloud functions
* LinkedIn
* YouTube video

This project is a really challenging one. At the end, we did not end up with a solution that satisfies us, but with the informations we are providing, we hope to shorten the gap to come up with a solution that goes in the line of Google Maps.

## Colab Notebook
The colab notebook contains every attempt to get to our expected results. The notebook is documented enough so the experiments can be reproduced.
<img width="1309" alt="Screenshot 2023-05-31 at 20 31 56" src="https://github.com/Srivathshan-Paramalingam-0505/CAA2023_UNIL_Microsoft/assets/83650518/d313d0d2-bfac-4816-8934-b8d04e58eca6">
 
## Micropython files 
In this file, you will have the code for the different functionalities we tried using the M5Stack Core2 device (https://flow.m5stack.com/). 
We had the opportunity to add the GPS unit to the device to retrieve GPS data (Latitude, Longitude, Altitude, Speed converted from knots to km/h). 
The interface file is more focused about the display we wanted to set in our device.
Whereas the final file implements the Google Cloud function with the interface.


## Cloud Functions on GCP
In that folder, you will find 3 Google Cloud functions, that we used to make our tests, in order to extract an image from Google APIs and open it in our IoT device.

However, the main function we progress with is "CloudFunction_generate_step_info", that we will use in our final MicroPython file to retrieve useful information for the directions that our bikers will follow.
We progressed in our idea with that function, as we could fetch the right data within our IoT device and use them to start coding what we intended to calculate and display on the screen device.

## Limitations
### Maps imports
Depending on the Iot device that is used, it is quite possible to find some issues since those devices do not support every image format. Furthermore, it is important to consider not surcharge the device with uncontrolled loop or too much information generation since you will lose precision on what you decide to display.

### M5stack core2 and sensors units
It is also rather important to consider the GPS unit precision since coordinates can be very precise but you need to ensure the bikers will get the accurate informations from their GPS unit at the right time.
The main device performance itself need to be considered since it has a very low battery and may be not appropriate depending on the duration of a biker's route.

### Time limit
As students, we had 14 weeks to progress in that project. During that time, we unfortunately had some other projects to manage and we had to plan definite time to progress with that project.

### Required knowledge
Depending on your objectives, you can be very quickly asked to know a bit of a lot of different services, that you need to understand at least at a high-level scale. To improve that, spending more time learning on different services that Google Cloud provides could be very interesting in order to get a better overview of the possibilities. Indeed, that could even avoid using non relevant services, depending on the fixed objectives.

## LinkedIn Post
Link to the post : 

## YouTube Video
Link to the video : 
