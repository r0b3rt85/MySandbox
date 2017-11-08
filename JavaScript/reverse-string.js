// Reverse a provided string.
// You must use arrays.
// Your result must be a string.

// Defining how the algorithm / function will work when called with a given parameter
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
