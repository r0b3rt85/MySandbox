// Mutations
//
// Task:
// Return true if the string in the first element of the array 
// contains all of the letters of the string in the second element 
// of the array.
//
// For example, ["hello", "Hello"], should return true because all 
// of the letters in the second string are present in the first, ignoring 
// case.
//
// The arguments ["hello", "hey"] should return false because the string 
// "hello" does not contain a "y".
//
// Lastly, ["Alien", "line"], should return true because all of the 
// letters in "line" are present in "Alien".

function mutation(arr) {
    // is each of [arr.2] included in [arr.1]
    var target = arr[0].toLowerCase();
    var test = arr[1].toLowerCase();
    
    for (var a = 0; a < test.length; a++) {
        if (target.indexOf(test[a]) === -1) {
            return false;
        }
    }
    return true;
}
// The call method with the string that is to be capitalized    
mutation(["hello", "hey"]);
