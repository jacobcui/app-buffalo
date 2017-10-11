# App Buffalo 

App engine + webapp2 + jinja2 + Endpoints + Bootstrap + Google closure.

[Live Demo](https://twoyap-182511.appspot.com/)

# Installation on Linux/Mac
  Install Google Cloud SDK from https://cloud.google.com/sdk/docs/
  ```
  $ cd ~
  $ tar -jxvf google-cloud-sdk-174.0.0-darwin-x86_64.tar.gz
  $ google-cloud-sdk/install.sh
  $ google-cloud-sdk/bin/gcloud components install app-engine-python
  ```

# Initialize the SDK:
  ```
  $ google-cloud-sdk/bin/gcloud init
  ```
# Install npm for javascript compiling.Google Closure Library
  ```
  $ npm i -g npm
  $ npm install
  ```

# Set up application in ``settings.py``:

  * Project name
  * reCAPTCHA_SITEKEY & reCAPTCHA_SECRET
    Read https://www.google.com/recaptcha/admin on how to get the site key and secret.

# Run Local Server
  ```
  $ cd <to your application directory>
  $ npm run watch
  $ ~/google-cloud-sdk/bin/dev_appserver.py .
  ```

# Deploy
  ```
  $ ~/google-cloud-sdk/bin/gcloud app deploy --version prod --project <Your Project Id>
  ```
  Please note, the Project Id is not the project name that you created via cloud console. It's in the ``Project Info`` tab and it looks like ``your-project-name-12345`` 

# Other notes

  You can stream logs from the command line by running:

  ``
  $ gcloud app logs tail -s default
  ``

  To view your application in the web browser run:

  ``
  $ gcloud app browse
  ``

Contact: jacobcui123@gmail.com