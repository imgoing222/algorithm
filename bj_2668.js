"strict mode";
const stdin = require("fs")
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
	.toString()
	.split("\n");

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

function calc(x) {
	visited[x] = 1;
	firstLine.push(x);
	secondLine.push(numbers[x]);
	if (visited[numbers[x]]) return;
	calc(numbers[x]);
}

function isSame(arr1, arr2) {
	arr1.sort((a, b) => a - b);
	arr2.sort((a, b) => a - b);
	if (JSON.stringify(arr1) === JSON.stringify(arr2)) return true;
}

function initialize() {
	firstLine = [];
	secondLine = [];
	visited = new Array(N + 1).fill(0);
}

const N = Number(input());
let numbers = [0];
let visited = new Array(N + 1).fill(0);

for (let i = 0; i < N; i++) {
	numbers.push(Number(input()));
}

let firstLine = [];
let secondLine = [];
let res = [];

for (let i = 1; i < N + 1; i++) {
	calc(i);
	if (isSame(firstLine, secondLine)) {
		res.push(...firstLine);
	}
	initialize();
}

const ans = [...new Set(res)];
ans.sort((a, b) => a - b);
console.log(ans.length);
ans.forEach((num) => console.log(num));
