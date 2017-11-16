// Confirm the Ending
//
// Task:
// Check if a string (first argument, str) ends with the given 
// target string (second argument, target).
//
// This challenge can be solved with the .endsWith() method, 
// which was introduced in ES2015. But for the purpose of this 
// challenge, we would like you to use one of the JavaScript 
// substring methods instead.

function confirmEnding(str, target) {
    // compare(string, end) = true or false
    var test = true;
    var sLen = str.length;
    var tLen = target.length;
    var sub = str.substring((sLen-tLen),sLen);
    //console.log(sub);
    if (sub == target) {
        test = true;
    } else {
        test = false;
    }
    return test;
    //console.log(test);
  }
  
  confirmEnding("Bastian", "n");
  