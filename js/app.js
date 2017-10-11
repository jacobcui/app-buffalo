// ES6 module demonstrating how to calling google closure library.
import _ from 'lodash';
import Sha1 from 'google-closure-library/closure/goog/crypt/sha1';

let sha = new Sha1();
let result = sha.digest();
console.log(result);
