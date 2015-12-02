goog.provide('cloud');
goog.require('goog.dom');

/**
 *  OAuth2Client definitions
 *
 */
cloud.OAuth2Client = function(){
  /*
   * @param {string} api key.
   * @param {string} client id.
   * @param {array} scopes.
   * @param {function} function to call after authentication request.
   */
  this.Authenticate = function(clientId, apiKey, scopes, callbackFunc){
    this.clientId = clientId;
    this.apiKey = apiKey;
    this.scopes = scopes;

    gapi.client.setApiKey(this.apiKey);
    gapi.auth.authorize({
      client_id: this.clientId,
      scope: this.scopes,
      immediate: true
    }, callbackFunc);
  };
};
