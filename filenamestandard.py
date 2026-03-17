# filenamestandard.py
import os
from PIL import Image
from PIL.ExifTags import TAGS

folder_path = '/home/hawk/Pictures/a/'
print(f"Looking in directory: {folder_path}")

if not os.path.exists(folder_path):
    print("DNE")
else:
    file_dicts = {}

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.jpg'):
            image_path = os.path.join(folder_path, filename)
            with Image.open(image_path) as image:
                file_dicts[filename] = image
                
                with Image.open(image_path) as image:
                    file_dicts[filename] = image_path
                    info_dict = {
                        "Filename": image.filename,
                        "Image Size": image.size,
                        "Image Height": image.height,
                        "Image Format": image.format,
                        "Image Mode": image.mode,
                        "Image is Animated": getattr(image, "is_animated", False),
                        "Frames in Image": getattr(image, "n_frames", 1)
                    }

                    for label,value in info_dict.items():
                        print(f"{label:25}: {value}")

                    exifdata = image.getexif()
                    for tag_id in exifdata:
                        tag = TAGS.get(tag_id, tag_id)
                        data = exifdata.get(tag_id)
                        if isinstance(data, bytes):
                            data = data.decode()
                        print(f"{tag:25}: {data}")
