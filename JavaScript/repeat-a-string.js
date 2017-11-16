// Repeat a string repeat a string
//
// Task:
// Repeat a given string (first argument) num times 
// (second argument). Return an empty string if num 
// is not a positive number.

function repeatStringNumTimes(str, num) {
    // [string]*num
    var result = "";
    for (var i = 0; i < num; i++) {
         result += str;   
    }
    return result;
    console.log(result);
  }
  
  repeatStringNumTimes("abc", -2);
  