from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit
remoteInit()

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xfdfdfd)
gps_0 = unit.get(unit.GPS, unit.PORTC)


Speed_knot_ = None
Speed_km_h_ = None



image0 = M5Img("res/UNILdirections.png", x=0, y=0, parent=None)
time = M5Label('time', x=253, y=7, color=0x000, font=FONT_MONT_14, parent=None)
altitude = M5Label('altitude', x=253, y=22, color=0x000, font=FONT_MONT_14, parent=None)
longitude = M5Label('longitude', x=0, y=22, color=0x000, font=FONT_MONT_14, parent=None)
speed = M5Label('speed', x=120, y=214, color=0x000, font=FONT_MONT_26, parent=None)
latitude = M5Label('latitude', x=0, y=7, color=0x000, font=FONT_MONT_14, parent=None)



def buttonA_wasPressed():
  global Speed_knot_, Speed_km_h_
  timerSch.run('GPS_timer1', 1000, 0x00)
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonC_wasPressed():
  global Speed_knot_, Speed_km_h_
  timerSch.stop('GPS_timer1')
  pass
btnC.wasPressed(buttonC_wasPressed)

@timerSch.event('GPS_timer1')
def tGPS_timer1():
  global Speed_knot_, Speed_km_h_
  gps_0.set_time_zone(2)
  time.set_text(str(gps_0.gps_time))
  altitude.set_text(str(gps_0.altitude))
  latitude.set_text(str(gps_0.latitude_decimal))
  longitude.set_text(str(gps_0.longitude_decimal))
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
  pass



def button_1_callback():
  global Speed_knot_, Speed_km_h_, gps_0 
  timerSch.run('GPS_timer1', 1000, 0x00)

def button_2_callback():
  global Speed_knot_, Speed_km_h_, gps_0 
  timerSch.stop('GPS_timer1')

timerSch.setTimer('GPS_timer1', 1000, 0x00)
lcd.qrcode('https://flow.m5stack.com/remote?id=846571715705438208', 0, 150, 85)
