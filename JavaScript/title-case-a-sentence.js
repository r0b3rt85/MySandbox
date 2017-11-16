// Title Case A Sentence.
//
// Task:
// Return the provided string with the first letter of 
// each word capitalized. Make sure the rest of the word 
// is in lower case.
//
// For the purpose of this exercise, you should also 
// capitalize connecting words like "the" and "of".

function titleCase(str) {
    // #1 - Split the sentence into an array of words
    // #2 - Convert each word to LowerCase
    var arr = str.toLowerCase().split(" ");
    console.log(arr);

    // #3 - Replace the 1st letter to an UpperCase
    var words = arr.map(function(x){
        return x.replace(x.charAt(0), x.charAt(0).toUpperCase());
    });

    // #4 - Join the words together and output the result
    return words.join(" ");
  }

// The call method with the string that is to be capitalized
titleCase("I'm a little tea pot");