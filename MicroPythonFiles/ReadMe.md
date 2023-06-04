 # Interface.py
 In this file, you will have the code for the different functionalities we tried using the M5Stack Core2 device. We had the opportunity to add the GPS unit to the device to retrieve GPS data (Latitude, Longitude, Altitude, Speed converted from knots to km/h). We set a timer so the data does not overflow. We decided to implement the remote feature to start and stop the device with the GPS unit.
 <img width="699" alt="Screenshot 2023-06-04 at 16 52 39" src="https://github.com/Srivathshan-Paramalingam-0505/CAA2023_UNIL_Microsoft/assets/83650518/2b871107-54f6-460b-973d-b8c30701d10a">



# Final_GpsApplication
In this file, the idea is to merge the graphical elements from the first file, with the external functionality we want to use, such as our Cloud function "generate_step_info".
We used a loop to process the information retrieved from the cloud function. With that loop, we are able to display the right informations (distance, duration, maneuver) when the biker will reach the next area of the next step, based on the GPS coordinates.
![IMG_3663](https://github.com/Srivathshan-Paramalingam-0505/CAA2023_UNIL_Microsoft/assets/83650518/7b144398-a6cd-467c-8064-a9c8b753e1cf)


## Limitation
For this to work, it would of course be necessary to take into consideration the precision of the GPS unit and make some tests to see if the bikers get the informations at the right time when riding their path.
