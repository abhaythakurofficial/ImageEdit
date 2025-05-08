import requests
import base64
import io

# Initialize session once for background removal
def remove_bg(image_bytes):
    """Remove background from the image."""
    API_KEY = "e97d08a4-6e4d-4817-80dd-c02c99fa9308"
    url = "https://app.imggen.ai/v1/remove-background"

    headers = {
        "X-IMGGEN-KEY": API_KEY,
    }

    # Convert raw bytes into file-like object for requests
    files = {
        "image": ("image.png", image_bytes)
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        data = response.json()
        if data.get("success"):
            base64_img = data["image"]
            return base64.b64decode(base64_img)  # Return image bytes
        else:
            raise Exception(data.get("message", "Unknown error"))
    else:
        raise Exception(f"Upscale API failed with status: {response.status_code}")



def enhance_image(image_bytes):
    API_KEY = "e97d08a4-6e4d-4817-80dd-c02c99fa9308"
    url = "https://app.imggen.ai/v1/upscale-image"

    headers = {
        "X-IMGGEN-KEY": API_KEY,
    }

    # Convert raw bytes into file-like object for requests
    files = {
        "image": ("image.png", image_bytes)
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        data = response.json()
        if data.get("success"):
            base64_img = data["image"]
            return base64.b64decode(base64_img)  # Return image bytes
        else:
            raise Exception(data.get("message", "Unknown error"))
    else:
        raise Exception(f"Upscale API failed with status: {response.status_code}")
