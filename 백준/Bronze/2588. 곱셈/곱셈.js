const fs = require('fs'); // 내장 파일시스템 불러오기
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const num_1 = Number(input[0].trim());
const arr_num_2 = input[1].trim().split('').map(Number);
const num_3 = num_1 * arr_num_2[2];
const num_4 = num_1 * arr_num_2[1];
const num_5 = num_1 * arr_num_2[0];

const num_6 = num_3 + (num_4 * 10) + (num_5 * 100);

console.log(num_3);
console.log(num_4);
console.log(num_5);
console.log(num_6);
