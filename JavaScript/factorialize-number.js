// Factorialize a Number
// Return the factorial of the provided integer.
// If the integer is represented with the letter n, a factorial is the product of all positive integers less than or equal to n.

// Defining how the algorithm / function will work when called with a given parameter
function factorialize(num) {
  // Define output variables (initial value = 1)
  var numOut = 1;

  // Create loop to iterate through values
  for (var n = 1; n < num + 1; n++){
    numOut = numOut * n;
  }

  // Output final / updated values
  return numOut;
}

// Test command
factorialize(5);
