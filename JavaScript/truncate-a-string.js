// Truncate a string
//
// Task:
// Truncate a string (first argument) if it is longer than 
// the given maximum string length (second argument). Return 
// the truncated string with a ... ending.
//
// Note that inserting the three dots to the end will add 
// to the string length.
// 
// However, if the given maximum string length num is 
// less than or equal to 3, then the addition of the three 
// dots does not add to the string length in determining the 
// truncated string.

function truncateString(str, num) {
  // [string]__reduce to [num] length + "...
  var len = str.length;
  var result = "";

  if (len > num && num > 3) {
    result = str.slice(0, (num-3)) + "...";
  } else if (len > num && num <= 3) {
    result = str.slice(0, num) + "...";
  } else {
    result = str;
  }
  return result;
}

// The call method with the string and number to test
truncateString("A-tisket a-tasket A green and yellow basket", 11);