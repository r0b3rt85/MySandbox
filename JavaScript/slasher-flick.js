// Slasher Flick
//
// Task:
// Return the remaining elements of an array after chopping off 
// 'n' elements from the head.
// 
// The head means the beginning of the array, or the zeroth index.

function slasher(arr, howMany) {
    // [arr] remove [howMany] and export.
    var newArr = [];
    if (arr.length > howMany) {
        newArr = arr.slice(howMany, arr.length);
        console.log(newArr);
    } else {
        newArr = [];
    }
    return newArr;
}

// The call method with the string that is to be capitalized   
slasher([1, 2, 3], 3);