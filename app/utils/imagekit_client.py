import requests
from ..config import settings
from typing import Dict

IMAGEKIT_UPLOAD_URL = "https://upload.imagekit.io/api/v1/files/upload"

def upload_file_to_imagekit(file_bytes: bytes, file_name: str, folder: str | None = None) -> Dict:
    """
    Upload raw bytes to ImageKit. Returns JSON response on success.
    Raises RuntimeError on config problems, or requests.HTTPError on non-2xx response.
    """
    if not settings.IMAGEKIT_PRIVATE_KEY:
        raise RuntimeError("ImageKit private key is not configured (IMAGEKIT_PRIVATE_KEY).")

    files = {
       
        "file": (file_name, file_bytes),
    }

    data = {
        "fileName": file_name
    }
    if folder:
        data["folder"] = folder


    auth = (settings.IMAGEKIT_PRIVATE_KEY, "")

    resp = requests.post(IMAGEKIT_UPLOAD_URL, auth=auth, files=files, data=data, timeout=30)
    try:
        resp.raise_for_status()
    except requests.HTTPError as e:
        body = resp.text
        raise requests.HTTPError(f"{e} -- response body: {body}", response=resp) from None

    return resp.json()
