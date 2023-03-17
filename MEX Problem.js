/**
 * https://www.geeksforgeeks.org/maximize-mex-by-adding-or-subtracting-k-from-array-elements/
 *
 * MEX Problem:
 *
 * Given an array arr containing n non-negative integers and an element x, in one operation, x can be added to or subtracted from any element of the array. MEX of an array is defined as the smallest non-negative integer which is not present in the array. For example, the MEX of [0, 1, 1, 3] is 2, and the MEX of [1, 2, 4] is 0. Find the maximum possible MEX of the array that can be achieved by doing the above operation any number of times.
 *
 * Example arr = [0, 1, 2, 1, 3] x = 3 If we add x to arr[1] we get arr = [0, 4, 2, 1, 3] having MEX equal to 5. This is the maximum possible MEX that can be achieved
 *
 *
 * Example arr = [0, 1, 2, 1, 3] x = 3 If we add x to arr[1] we get arr = [0, 4, 2, 1, 3] having MEX equal to 5. This is the maximum possible MEX that can be achieved
 * Function Description Complete the function getMaximumMex in the editor below. getMaximumMex has the following parameters: int arr[n]: an array of n non-negative integers int x: an integer that can be added to or subtracted from any element of the array Returns int: the maximum possible MEX of arr

 */

function getMaximumMex(arr, K) {
    n = arr.length
    let mp = new Map();
    for (let i = 0; i < n; i++) {
        mp[arr[i] % K]++;
    }

    for (let i = 0; i < n; i++) {
        if (mp.has(i % K)) {
            return i;
        }

        mp[i % K]--;
        if (mp[i % K] === 0) mp.delete(i % K);
    }

    return n;
}
