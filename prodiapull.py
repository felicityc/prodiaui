from prodiapy import Prodia
import os
import requests
import datetime
import random
import math

def prodia_generation(recursion_depth=0):
    if recursion_depth > 99:
        print ("You've reached the repetition depth limit of 99. This is a limit of python and not a user error, and is not related to API limits or credits. Please restart the script. *smiles*")
        return

def download_image(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print("Image downloaded successfully to prodia_output\\*.png.")  # Fixed backslash
    else:
        print("Failed to complete a download of the output image, please check your network connection or firewall. *smiles*")

# this define is so it can loop basically
def prodia_generation(recursion_depth=0):
    if recursion_depth > 99:
        print("You've reached the repetition depth limit of 99. This is a limit of python and not a user error, and is not related to API limits or credits. Please restart the script. *smiles*")
        return

    # read the hecking readme.md for instructions on how to set the api key in env variables
    prodia = Prodia(api_key=os.getenv('PRODIA_API_KEY'))

    # job: model, prompt, negative_prompt, style_preset, steps, cfg_scale, seed, upscale, sampler, width, height
    job = prodia.sd.generate(prompt=input("Enter a prompt string: "))

    print("Please wait a moment... meow.")
    lucky = str(round(math.sqrt(random.randint(1, 9999)), 2))
    target = str(44.44)
    print("Today's lucky number is: " + lucky)
    print("The target number was: " + target)
    if lucky == target:
        print("You won! That's a 1 in 10,000! Don't gamble today, you already wasted it! Please be patient, your image is still being generated. *smiles*")
    else:
        print("You lost! Maybe next time. Please be patient while your image is still being generated. *smiles*")
    result = prodia.wait(job)

    # the result url
    image_url = result.image_url

    # preparing the output folder
    script_dir = os.path.dirname(__file__)
    folder_name = "prodia_output"
    folder_path = os.path.join(script_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # the... base filename of the output image
    base_filename = 'imggen.png'
    filename = os.path.join(folder_path, base_filename)

    # it will create a new folder in the same directory as the py file, download the result image to the new folder, with a timestamp in the filename
    print(filename)
    counter = 1
    timestr = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    while os.path.exists(filename):
        filename = os.path.join(folder_path, f"{os.path.splitext(base_filename)[0]}_{counter}_{timestr}.png")
        counter += 1    

    download_image(image_url, filename)

    # loop until user quits
    repeat = input("Enter another prompt? y/n:")
    if repeat == "y":
        prodia_generation(recursion_depth + 1) 
    else:
        print("Closing.")
        quit()

prodia_generation()