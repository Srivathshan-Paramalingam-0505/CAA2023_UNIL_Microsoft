import requests
from io import BytesIO
from PIL import Image
import base64

def FindLocation(request):
  # From our device, we'll do POST request with location parameters, then the cloud function will get the picture from a GET request
  if request.method != "POST":
    return "This API only accepts POST requests"
  
  center = request.form.get('center')
  zoom = request.form.get('zoom')
  size = request.form.get('size')
  key = 'yourKey'

  if center is None or zoom is None or size is None or key is None:
    return "One or more required parameters missing"

  url = f"https://maps.googleapis.com/maps/api/staticmap?center={center}&zoom={zoom}&size={size}&key={key}"

  response = requests.get(url)

  if response.status_code == 200:
      # Access the response content in bytes
      content = response.content
      # Use PIL to open the image from the bytes
      image = Image.open(BytesIO(content))
      # Save the image to a BytesIO object
      buffer = BytesIO()
      image.save(buffer, format="PNG")
      # Encode the image bytes as base64
      image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
      # Return the image as a base64-encoded string in the response
      return {'image': image_base64}
  else:
      return {'error': 'Failed to fetch URL'}