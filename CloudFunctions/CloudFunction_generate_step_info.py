import requests
import json

def generate_step_info2(request):
    request_json = request.get_json()
    origin = request_json.get("origin")
    destination = request_json.get("destination")
    mode = "bicycling"
    key = "AIzaSyDZftPI4XyWSVRfcfkxBxHaydWC_4VzfXg"

    # Make a request to the Directions API to get the polyline
    directions_url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&mode={mode}&key={key}"
    directions_response = requests.get(directions_url)

    # Parse the response content as JSON
    directions_data = json.loads(directions_response.content)

    step_info = []
    for step in directions_data["routes"][0]["legs"][0]["steps"]:
        distance = step["distance"]["text"]
        duration = step["duration"]["text"]
        maneuver = step.get("maneuver", "N/A")
        start_lat = round(step["start_location"]["lat"], 5)
        start_lng = round(step["start_location"]["lng"], 5)
        step_info.append((distance, duration, maneuver, start_lat, start_lng))

    return json.dumps(step_info)