"strict mode";

const stdin = require("fs")
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
	.toString()
	.split("\n");

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

const N = Number(input());
const board = input().split(" ").map(Number);
const record = Array(N).fill(Infinity);
record[0] = 0;

let jump = 1;
for (let i = 0; i < N; i++) {
	for (let j = i + 1; j <= i + board[i]; j++) {
		record[j] = Math.min(record[j], jump);
	}
	jump = record[i + 1] + 1;
}
console.log(record);
console.log(record[N - 1] === Infinity ? -1 : record[N - 1]);
