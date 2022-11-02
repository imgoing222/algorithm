"strict mode";

const stdin = require("fs")
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
	.toString()
	.split("\n");

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

function getCarNumbers(arr) {
	for (let i = 0; i < N; i++) {
		arr.push(input().trim());
	}
}

const N = Number(input());
const 대근 = [];
const 영식 = [];

getCarNumbers(대근);
getCarNumbers(영식);

let cnt = 0;

let start = 0;
for (const carNumber of 대근) {
	for (let i = start; i < 대근.length; i++) {
		if (carNumber === 영식[i]) {
			start = i + 1;
			cnt += 1;
		}
	}
}

console.log(N - cnt);
