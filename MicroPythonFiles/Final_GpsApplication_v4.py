from m5stack import *
from m5stack_ui import *
from uiflow import *
import urequests as requests
import ujson as json
import unit

#Initialization of components
screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
gps_0 = unit.get(unit.GPS, unit.PORTC)

#Variables definition
current_latitude = gps_0.latitude_decimal
current_longitude = gps_0.longitude_decimal
Speed_knot_ = 0
Speed_km_h_ = 0

#Labels initialization
messageError = M5Label('', x=0, y=200, color=0x000, font=FONT_MONT_14, parent=None)
statusLabel = M5Label('', x=0, y=57, color=0x000, font=FONT_MONT_14,parent=None)
initialLabel = M5Label('', x=0, y=77, color=0x000, font=FONT_MONT_14,parent=None)
distanceLabel = M5Label('', x=0, y=97, color=0x000, font=FONT_MONT_14,parent=None)
durationLabel = M5Label('', x=0, y=117, color=0x000, font=FONT_MONT_14,parent=None)
maneuverLabel = M5Label('', x=0, y=137, color=0x000, font=FONT_MONT_14,parent=None)
time = M5Label('time', x=253, y=7, color=0x000, font=FONT_MONT_14, parent=None)
altitude = M5Label('altitude', x=253, y=22, color=0x000, font=FONT_MONT_14, parent=None)
longitude = M5Label('longitude', x=0, y=22, color=0x000, font=FONT_MONT_14, parent=None)
speed = M5Label('speed', x=120, y=214, color=0x000, font=FONT_MONT_26, parent=None)
latitude = M5Label('latitude', x=0, y=7, color=0x000, font=FONT_MONT_14, parent=None)

#Here the user will be able to select his own path
origin = "46.522640908185, 6.584987401404577"
destination = "46.521880860162064, 6.567944879588675"
url = "https://us-central1-projectiot-380815.cloudfunctions.net/generate_step_info2"
# Split the destination string into latitude and longitude
dest_lat, dest_lng = map(float, destination.split(", "))

#Parameters that will be used to make the POST request
payload = {
    "origin": origin,
    "destination": destination
}
headers = {"Content-Type": "application/json"}

#The request is sent to the cloud function
response = requests.post(url, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    step_info = json.loads(response.content)
    
    #Separate step_info into different content, so we can manage how they display
    latitude_list = [step[3] for step in step_info]
    longitude_list = [step[4] for step in step_info]
    informations_step = [step[0:3] for step in step_info]

else:
    # Handle error condition
    statusLabel.set_text('Error')
    messageError.set_text(str(response.status_code))

#Functions
def buttonC_wasPressed():
  global Speed_knot_, Speed_km_h_, current_latitude, current_longitude
  timerSch.stop('GPS_timer1')
  pass
btnC.wasPressed(buttonC_wasPressed)

#We did not call that timer to realize our test, since it led to issues regarding the while loop below
@timerSch.event('GPS_timer1')
def tGPS_timer1():
  global current_latitude, current_longitude
  gps_0.set_time_zone(2)
  time.set_text(str(gps_0.gps_time))
  altitude.set_text(str(gps_0.altitude))
  latitude.set_text(str(gps_0.latitude_decimal))
  longitude.set_text(str(gps_0.longitude_decimal))
  current_latitude = gps_0.latitude_decimal
  current_longitude = gps_0.longitude_decimal
  
  try :
    Speed_knot_ = float((gps_0.speed_knot))
    pass
  #As the speed sensor is pretty volatile, we set it to 0 for the cases it cannot provide a reliable data
  except:
    Speed_knot_ = 0
  Speed_km_h_ = Speed_knot_ * 1.852
  speed.set_text(str(Speed_km_h_))
  if Speed_km_h_ > 0:
    rgb.setColorAll(0x33ff33)
  else:
    rgb.setColorAll(0xff0000)
  pass

#We define a loop to iterate through each step of the selected path
for i in range(len(latitude_list)-1):
  
  statusLabel.set_text("Below, you'll find info for each step")
  
  #In that loop, we calculate regularly our sensor data until the below condition if fulfilled
  while abs(current_latitude - latitude_list[i]) > 0.0001 or abs(current_longitude - longitude_list[i]) > 0.0001:
    initialLabel.set_text('Waiting until the next step is reached')
    gps_0.set_time_zone(2)
    time.set_text(str(gps_0.gps_time))
    altitude.set_text(str(gps_0.altitude))
    latitude.set_text(str(gps_0.latitude_decimal))
    longitude.set_text(str(gps_0.longitude_decimal))
    current_latitude = gps_0.latitude_decimal
    current_longitude = gps_0.longitude_decimal
    try :
      Speed_knot_ = float((gps_0.speed_knot))
      pass
    except:
      Speed_knot_ = 0
    Speed_km_h_ = Speed_knot_ * 1.852
    speed.set_text(str(Speed_km_h_))
    if Speed_km_h_ > 0:
      rgb.setColorAll(0x33ff33)
    else:
      rgb.setColorAll(0xff0000)
    wait_ms(2)

  #Display the next step informations when the biker reaches the defined range above
  speaker.playTone(220, 1, volume=5)
  distanceLabel.set_text('Distance: '+ str(informations_step[i][0]))
  durationLabel.set_text('Duration: '+ str(informations_step[i][1]))
  maneuverLabel.set_text('Maneuver: '+ str(informations_step[i][2]))

  #Check if the biker reached the destination
  if abs(current_latitude - dest_lat) < 0.0001 and abs(current_longitude - dest_lng) < 0.0001: 
    speaker.playTone(220, 2, volume=5)
    statusLabel.set_text("Great, you've reached your destination!")
    distanceLabel.set_text('')
    durationLabel.set_text('')
    maneuverLabel.set_text('')

def button_1_callback():
  global Speed_knot_, Speed_km_h_, gps_0, current_latitude, current_longitude
  timerSch.run('GPS_timer1', 1000, 0x00)

def button_2_callback():
  global Speed_knot_, Speed_km_h_, gps_0, current_latitude, current_longitude
  timerSch.stop('GPS_timer1')

timerSch.setTimer('GPS_timer1', 1000, 0x00)