# NSFW-Sense

This program uses Machine Learning Algorithms to identify whether an image is ‘NSFW’ (Not Safe For Work) and returns probability scores on the likelihood that an image contains any kind of nudity. This model is great for anyone trying to automatically moderate or filter offensive content from their platform.

This program can often be used to protect online businesses and communities and specially children from the trust & safety risks associated with user-generated content.

## How it works?

It uses an image as its input, to be passed in the **`sense-url`** variable. Next, you have to insert correct values in the following functions, refer to the help comments in the actual code:
  * **`send_sms()`**
     * **`request_payload{}`**
     
  * **`make_call()`**
     * **`client.calls.create()`**
     
## Requirements

This program uses [Clarifai](https://clarifai.com) for making reverse image search for tags, [Twilio](https://www.twilio.com) for sending Alert SMS and making calls, and finally [Hasura](https://hasura.io/) for storing the NSFW probability scores as parameters in a table (Still in Beta, can be used to store user details to send SMS & make Calls). It is better if you create _free_ accounts at [Clarifai](https://clarifai.com), [Twilio](https://www.twilio.com) and [Hasura](https://hasura.io/), and setup your PC according to their Docs, API Keys & Configurations. This will ensure that the program runs without any errors.
_Make sure to change the API Keys and sepcific authentication variables, according to your account credentials in the NSFW-Sense.py program before running it._

Also make sure to pip install the following packages on your CLI in advance:

**```pip install clarifai```**
> This will install Clarifai API

**```pip install twilio```**
> This will install Twilio API

**```curl -L https://hasura.io/install.sh | bash```**
> This will install Hasura CLI module

If something doesn't works, try to sudo install, check their respective docs, or else raise an issue in the issue tracker.

## Future Propects

Develop a Chrome Extension to monitor this program.

##### Don't forget to Star this Repo, make sure to Fork it, tinker with it, raise your Pull Request and finally come up with better versions of this program. :)
