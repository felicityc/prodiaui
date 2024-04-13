Updated: 13/04/2024

v0.1

by Felicity

*smiles*

concern of the day: maybe ill have to rewrite it in js anyway if im going to host it when its more complete

This was written with Python 3.11 but earlier versions should probably work fine as long as you install the pre-req

I would like to say I used this example prodiapy repo (https://github.com/zenafey/prodiapy) for its baseline code 

This assumes you have an API key already (https://app.prodia.com/api) and it will only work with prodia's api, not others

# Setup

Ensure you have a relatively modern version of python installed

```commandline
pip install prodiapy
```

Set your API key as an OS environment variable. This will let you set it and you will only need to include the name of the variable rather than the entire key every time, and you do not need to adjust anything within the script as it's already been set on the OS side. 

If you are going to use several API keys, you will probably change that yourself. 

    [b]Windows: Open the System Properties settings menu within the control panel (you can just search 'env' in the start menu and it will take you there)
        Click on 'Environment Variables' near the bottom
        Under user variables, click 'New...' 
        Variable name should be: `PRODIA_API_KEY`
        And the variable value should be the API key without any additional punctuation. It's good to restart your PC after making OS changes but it's not really crucial.

    Linux: Open your CLI and enter the command
    ```commandline
    export PRODIA_API_KEY='YOURAPIKEY'```
        To verify it was successful, enter 
            ```commandline
            printenv PRODIA_API_KEY```
                If this prints out YOURAPIKEY then you need to replace that text with **your own API key** into the previous command, otherwise, it worked.

# Usage

Either navigate to the folder containing the python file and open the CLI to the path and enter the command:

```commandline
py prodiapull.py```

Then write in your prompt. 
It will create a new folder in the same directory and download the resulting image (if successful) to it with a timestamp. 

_More Info_

Automatic1111 has a method to extract the prompt and parameters out of the raw png of an SD output. So if you forget you can always run a local SD even without any good hardware and use the pnginfo menu to get the prompts and settings. The settings are usually more important. 

You can continue to input prompts without reopening the script. 
The script will also generate a random number between 1 and 9999 and round the square root, and that is your lucky number. If it's equal to the target number, then you are really darn lucky. 

To come: dynamically changing other parameters it sends to the model in hopefully intuitive ways.



# Additional tools

I also set up a script that improved on Prodia's retriveal request, which resopnds with a list of models that can be used for the previous script. When I'm not lazy I'll add in options to do samplers, loras, embeddings, etc, since it's all just a request but cba right now *smiles*