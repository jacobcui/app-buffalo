# App Buffalo

App engine + webapp2 + jinja2 + Endpoints + Bootstrap + Google closure

Plus a shell script to install required development tools/libraries.


* Installation on Linux/Mac
  Install Google Cloud SDK from https://cloud.google.com/sdk/docs/
  $ cd ~
  $ tar -jxvf google-cloud-sdk-174.0.0-darwin-x86_64.tar.gz
  $ 
  $ google-cloud-sdk/install.sh
  $ google-cloud-sdk/bin/gcloud components install app-engine-python

* Run gcloud init to initialize the SDK:
  $ google-cloud-sdk/bin/gcloud init

* Install Google Closure Library
  $./install.sh

* Set up application
  Edit settings.py to set up:
  * Project name
  * reCAPTCHA_SITEKEY & reCAPTCHA_SECRET
    Read https://www.google.com/recaptcha/admin on how to register.

* Run Local Server
  $ cd <to your application directory>
  $ ~/google-cloud-sdk/bin/dev_appserver.py .

* Deploy
  $ ~/google-cloud-sdk/bin/ -A YOUR_APP_ID update .

Contact: jacobcui123@gmail.com