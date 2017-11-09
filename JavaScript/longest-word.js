// Find the Longest Word in a String
//
// Task:
// Return the length of the longest word in the provided sentence.
//
// Your response should be a number.

function findLongestWord(str) {
  // Split the words into an array
  var arr = str.split(" ");
  // Iterate throught the array using .map to return the length of each string
  var arrLen = arr.map(function(val){
    return val.length;
  });
  // Reduce the array to the maximum value usinf the Math.max and .reduce methods
  var maxLength = arrLen.reduce(function(a, b) {
    return Math.max(a, b);
  });
  // Output the results
  return maxLength;
}

// Test the script using this command
findLongestWord("The quick brown fox jumped over the lazy dog");
