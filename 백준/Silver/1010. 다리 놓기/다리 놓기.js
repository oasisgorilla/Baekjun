const fs = require('fs'); 

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n'); 

const T = Number(input[0].trim());
const MAX = 30; 

const dp = Array.from({ length: MAX + 1 }, () => Array(MAX + 1).fill(0n)); 

for (let m = 0; m <= MAX; m++) { 
    dp[0][m] = 1n; 
    dp[m][m] = 1n; 
} 

for (let m = 1; m <= MAX; m++) { 
    for (let n = 1; n < m; n++) { 
        dp[n][m] = dp[n][m - 1] + dp[n - 1][m - 1]; 
    } 
} 

let out = []; 
for (let t = 1; t <= T; t++) { 
    const [n, m] = input[t].split(' ').map(Number);  
    out.push(String(dp[n][m])); 
} 
console.log(out.join('\n'));