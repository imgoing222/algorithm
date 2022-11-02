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
const people = input().split(" ").map(Number).reverse();

let seat = [];
for (const [index, num] of people.entries()) {
	const height = N - index;
	// num이 index와 같은 경우
	if (num === index) {
		seat.push(height);
	}
	// num이 index 보다 작은 경우
	else if (num < index) {
		seat.splice(num, 0, height);
	}
}

console.log(seat.join(" "));
