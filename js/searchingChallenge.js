// Searching Challenge
// Have the function
// SearchingChallenge (strArr) take the array of strings stored in strArr, which will be a 2D matrix of 0 and 1's, and determine how many holes, or contiguous regions of 0's, exist in the matrix. A contiguous region is one where there is a connected group of O's going in one or more of four directions: up, down, left, or right. For example: if strArr is ['10111", "10101", "11101", "11111"), then this looks like the following matrix:
// 1 0 1 1 1
// 10 101
// 1 1 10 1
// 1 1 1 1 1
// For the input above, your program should return 2 because there are two separate contiguous regions of 0's, which create
// "holes" in the matrix. You can assume the input will not be empty.
//
//   Examples
// Input: ["01111","01101","00011","11110"]
// Output : 3
//
// Input: ["1011", "0010"]
// Output : 2

function searchingChallenge(strArr) {
  let count = 0;

  function dfs(row, col) {
    if (row < 0 || col < 0 || row >= strArr.length || col >= strArr[row].length || strArr[row][col] === "1") {
      return;
    }

    strArr[row] = strArr[row].substr(0, col) + "1" + strArr[row].substr(col + 1);

    dfs(row - 1, col);
    dfs(row + 1, col);
    dfs(row, col - 1);
    dfs(row, col + 1);
  }

  for (let row = 0; row < strArr.length; row++) {
    for (let col = 0; col < strArr[row].length; col++) {
      if (strArr[row][col] === "0") {
        count++;
        dfs(row, col);
      }
    }
  }

  return count;
}

console.log(searchingChallenge(["1011", "0010"]));
