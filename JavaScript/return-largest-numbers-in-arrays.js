// Return Largest Numbers in Arrays
//
// Task:
// Return an array consisting of the largest number from 
// each provided sub-array. For simplicity, the provided 
// array will contain exactly 4 sub-arrays.


function largestOfFour(arr) {
    // Array[Index][Subindex]
    // arr [i] [sub]
    var result = [];
    for (var i = 0; i < arr.length; i++) {
        var lNum = arr[i][0];
        console.log(lNum);
        for (var sub = 0; sub < arr.length; sub++) {
            if (arr[i][sub] > lNum) {
                lNum = arr[i][sub];                
            }            
        }
        result[i] = lNum;
        console.log(result[i]);        
    }
    return result;
  }
  
largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
  