// Reverse a provided string.
//
// Task:
// You must use arrays.
// Your result must be a string.

function reverseString(str){
  // Define the variables needed for the calculations (str is defined as a parameter)
  var stringOut = "";
  var stringArray = str.split("");

  // Manipulate the array to reverse all the values
  stringArray.reverse();
  stringOut = stringArray.join("");

  // Return the value after it has been converted back into a single string
  return stringOut;
}

// The call method with the string that is to be reversed
reverseString("hello");
