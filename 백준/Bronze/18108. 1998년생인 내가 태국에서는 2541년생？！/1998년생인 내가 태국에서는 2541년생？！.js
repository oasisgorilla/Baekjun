const fs = require('fs'); // 모듈을 불러올 때 사용하는 함수 require, fs는 내장 파일시스템 모듈을 불러온다.

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const thai_standard_gap = 2541 - 1998;

const result = Number(input[0]) - thai_standard_gap;

console.log(result);