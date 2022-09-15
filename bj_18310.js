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
const houses = input().split(" ").map(Number);

houses.sort((a, b) => a - b);

console.log(houses[Math.floor((N - 1) / 2)]);
