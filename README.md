# CAA2023_UNIL_Microsoft Cloud x IoT : GPS for bikers
*This is our attempt to develop a GPS for bikers using the M5Stack Core2 device connected to the GPS unit and APIs from the Google Cloud Platform*

<img width="649" alt="Screenshot 2023-05-25 at 11 21 08" src="https://github.com/Srivathshan-Paramalingam-0505/CAA2023_UNIL_Microsoft/assets/83650518/74967780-58ee-4243-9e4a-c4a76ba07e32">

## Summary
This project aimed to implement a GPS within the M5Stack Core2 device for the bikers to travel around without being distracted by the overflowing informations coming from a smartphone. Here is a list of the different files we created for this project
* m5f file
* colab notebook
* cloud functions
* LinkedIn
* YouTube video

 ## M5F file
 In this file, you will have the code for the different functionalities we tried using the M5Stack Core2 device. We had the opportunity to add the GPS unit to the device to retrieve GPS data (Latitude, Longitude, Altitude, Speed converted from knots to km/h). We set a timer so the data does not overflow. We decided to implement the remote feature to start and stop the device with the GPS unit.
 <img width="724" alt="Screenshot 2023-05-25 at 16 02 54" src="https://github.com/Srivathshan-Paramalingam-0505/CAA2023_UNIL_Microsoft/assets/83650518/9714da67-adad-4a82-b194-d3b5158373a1">


## Colab Notebook
The colab notebook contains every attempts to get to our expected results. The notebook is documented enough so the experiments can be reproduced.

## Cloud Functions on GCP
This section contains three different cloud functions we deployed through Google Cloud Platform

* *Cloud_Function_FindLocation.py*:  This Python function is designed to act as an endpoint for a web API that accepts POST requests. The purpose of this API is to fetch a map image from Google Maps based on specific input parameters (center of the map, zoom level, and size of the map), and return this image as a base64-encoded string.
* *Cloud_Function_generateMap.py:* This Python function receives HTTP POST or PUT requests containing parameters for origin, destination, and mode of a journey. It uses these parameters to query the Google Directions API for route details, including a polyline representing the route. After decoding and then re-encoding this polyline, the function creates a request for the Google Static Maps API to generate a static map image depicting the journey's path with markers for start and end points. The function fetches this image, saves it locally as a PNG, and then uploads this image to a Google Cloud Storage bucket named 'maps_bucket'. Lastly, it deletes the local image file. While the function doesn't return any explicit data, its operation results in the creation of a map image in cloud storage based on the journey details provided in the HTTP request.
* *Cloud_Function_generate_step_info.py:* The Python function generate_step_info2 takes an HTTP request, retrieves "origin" and "destination" from the request's JSON data, and uses these to call the Google Directions API for a bike-friendly route. The function processes the returned JSON data, iterating over each step in the route to extract information like distance, duration, maneuver, and starting coordinates (latitude and longitude). Each step's data is collected into a tuple and stored in a list, step_info. Finally, this list is converted into a JSON-encoded string and returned by the function. This string represents a list of tuples, each containing data for a single step of the proposed bike route. A valid Google Maps API key is required for the function to work.
## LinkedIn Post
Link to the post : 

## YouTube Video
Link to the video : 
