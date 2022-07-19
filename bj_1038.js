"strict mode";
const stdin = require("fs")
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
	.toString()
	.split("\n");

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

function isDescending(x) {
	let temp = String(x);
	if (temp.length === 1) return true;
	for (let i = 0; i < temp.length - 1; i++) {
		if (Number(temp[i]) <= Number(temp[i + 1])) return false;
	}

	return true;
}

N = Number(input());

let num = 0;
let idx = 0;
while (true) {
	if (idx === N || num === 10000000000) break;
	if (isDescending(num)) {
		idx += 1;
	}
	num += 1;
}

console.log(num === 10000000000 ? -1 : num);
