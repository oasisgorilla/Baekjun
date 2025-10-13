const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = input[0]; // 5
let arr_A = input[1].split(' ').map(Number); // [1, 1, 1, 6, 0]
let arr_B = input[2].split(' ').map(Number); // [2, 7, 8, 3, 1]

let ascending_A = [...arr_A].sort((a, b) => a - b); // 복사 후 오름차순 정렬
let descending_B = [...arr_B].sort((a, b) => b - a); // 복사 후 내림차순 정렬

let result = 0
for (let i = 0; i < N; i++) {
    to_result = ascending_A[i];
    index = arr_B.indexOf(descending_B[i]);
    result += to_result * arr_B[index]
    arr_B[index] = -1; // 중복방지를 위한 표시
}

console.log(result);



