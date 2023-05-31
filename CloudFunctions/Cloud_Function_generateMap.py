from google.cloud import storage
import requests
from PIL import Image
from io import BytesIO
import polyline

def generate_map(request):
    if request.method not in ["POST", "PUT"]:
        return "This API only accepts POST and PUT requests"

    # Get the origin, destination, mode, and API key from the request
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    mode = request.args.get('mode')
    key = request.args.get('key')

    if origin is None or destination is None or mode is None or key is None:
        return "One or more required parameters missing"

    # Make a request to the Directions API to get the polyline
    directions_url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&mode={mode}&key={key}"
    directions_response = requests.get(directions_url)
    polyline_points = directions_response.json()["routes"][0]["overview_polyline"]["points"]

    # Decode the polyline into a list of latitudes and longitudes
    decoded_polyline = polyline.decode(polyline_points)

    # Create a path parameter with the encoded polyline
    encoded_polyline = polyline.encode(decoded_polyline)
    path_param = f"enc:{encoded_polyline}"

    # Create the URL for the static map with the path parameter
    url = f"https://maps.googleapis.com/maps/api/staticmap?size=320x240&maptype=roadmap&markers=color:black%7C{origin}&markers=color:red%7C{destination}&path=color:0x0000ff|weight:5|{path_param}&key={key}"

    # Get the image from the URL
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    # Save the image to a file in PNG format
    img_file_name = 'map_image.png'
    img.save(img_file_name, 'PNG')

    # Upload the image file to Google Cloud Storage
    storage_client = storage.Client()
    bucket_name = 'maps_bucket'
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(img_file_name)
    blob.upload_from_filename(img_file_name)

    # Delete the local image file
    os.remove(img_file_name)