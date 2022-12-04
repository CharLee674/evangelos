import requests

# The base url of your photo file, found by inspecting the elements of the page (don't include the filename)
image_base_url = ""
# The first few numbers and letters in your filename that doesn't increment over files 
image_file_name_starter = "" 
# Download location
download_location = "C:/Users/Charls/Pictures/Grad/"

start = 26
end = 38

for i in range(start,end):
    filename = image_file_name + f"{i}" + ".jpg"
    img_data = requests.get(image_base_url + filename).content
    with open(download_location + f'{filename}.jpg', 'wb') as f:
        f.write(img_data)
