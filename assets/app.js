/**
 * @fileoverview Controller for web application.
 */
goog.provide('app');
goog.require('app.template');
goog.require('goog.dom');
goog.require('cloud');

app.displayMessage = function(message, clear) {
  var msg = goog.dom.getElement('message');
  var timestamp = new Date();
  if (msg) {
    if (typeof(clear) == 'undefined') {
      clear = false;
    }
    message = timestamp + " " + message + '<BR>';
    if (clear) {
      msg.innerHTML = message;
    } else {
      msg.innerHTML += message;
    }
  }
};

app.processAuthResults = function(authResult) {
  if (authResult && !authResult.error) {
    app.displayMessage('Authentication successed.');
    var key = { path: [{ kind: 'config'
                         }] };
    var requestParams = {
      datasetId: 'emu-io',
      keys: [ key ]
    };

    var path='https://www.googleapis.com/datastore/v1beta1/datasets/emu-io/lookup';
    var theParams = {
      'path': path,
      'method': 'POST',
      'params': { 'keys': [key] },
      'headers': {
        'Content-Type': 'application/json'
      }
    };

    gapi.client.request(theParams).then(
      function(response) {
        console.log('success');
        console.log(response);
        // Handle response
      }, function(reason) {
        console.log('fail');
        console.log(reason);
        // Handle error
      });
/*    
    gapi.client.load('datastore', 'v1beta1').then(
      function(response){
        console.log(response);
        gapi.client.datastore.datasets.lookup(requestParams).then(
          function(res){
            app.displayMessage(res);
          },
          function(res){
            app.displayMessage(res);
          }
        );
      },
      function(res){
        app.displayMessage(res.error);
      }
    );
*/
  } else {
    app.displayMessage('Authentication failed.');
    app.displayMessage(authResult);
  }


};

window.onload = function(){
  var PROJECT = 'jiac-999';
//  var clientId = '153121532196-mr9tgoqp9q4iad0cj0n9cth4dcfvvefg.apps.googleusercontent.com';
  var clientId = '445802052391-4tvs2ebbfiap1vjfgma81oq709oa7m67.apps.googleusercontent.com';
//  var apiKey = 'U9D3jQzw-so5wU6iqJRsCKUI';
  var apiKey = 'L2YfHFshYtHWGatdjUF8iaKV';
  var scopes = [
    // View and manage your data across Google Cloud Platform services
    'https://www.googleapis.com/auth/cloud-platform',
    // View and manage your Google Cloud Datastore data
    'https://www.googleapis.com/auth/datastore',
    // View your email address
    'https://www.googleapis.com/auth/userinfo.email'
  ];
  app.displayMessage('Authenticating');
  var client = new cloud.OAuth2Client();
  client.Authenticate(clientId, apiKey, scopes,
                      app.processAuthResults);
};
