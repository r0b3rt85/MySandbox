// Check for Palindromes
//
// Task:
// Return true if the given string is a palindrome. Otherwise, return false.
//
// A palindrome is a word or sentence that's spelled the same way both forward and backward, ignoring punctuation, case, and spacing.
//
// Note:
// You'll need to remove all non-alphanumeric characters (punctuation, spaces and symbols) and turn everything lower case in order to check for palindromes.

function palindrome(str) {
  // #1 Define the forward and reverse strings by removing unwanted charcters
  var strFor = str.replace(/[\W_]/g, '').toLowerCase();
  var strRev = str.replace(/[\W_]/g, '').toLowerCase().split('').reverse().join('');

  // #2 Compare the strings in an if statement
  if (strFor === strRev) {
    return true;
  } else {
    return false;
  }
}

// Testing the function
palindrome("0_0 (: /-\ :) 0-0");
