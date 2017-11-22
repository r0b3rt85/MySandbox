// Chunky Monkey
//
// Task:
// Write a function that splits an array (first argument) into 
// groups the length of size (second argument) and returns them 
// as a two-dimensional array.


function chunkArrayInGroups(arr, size) {
    // [arr] split into length of [size] and [push] results onto another array
    var newArr = [];
    
    for (var a = 0; a < arr.length; a += size) {
        newArr.push(arr.slice(a, a + size));        
    }
    
    return newArr;
}
// The call method with the string that is to be capitalized 
chunkArrayInGroups(["a", "b", "c", "d"], 2); 