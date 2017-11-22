// Falsy Bouncer
//
// Task:
// Remove all falsy values from an array.
// 
// Falsy values in JavaScript are false, null, 0, "", undefined, 
// and NaN.

function bouncer(arr) {
    // filter [arr] and return values [!bool].
    var newArr = [];

    newArr = arr.filter(Boolean);

    return newArr;
} 
// The call method used to test the function
bouncer([7, "ate", "", false, 9]);
