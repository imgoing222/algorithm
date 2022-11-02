"strict mode";

const stdin = require("fs")
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
	.toString()
	.split("\n");

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

const S = input().trim().split("");
const T = input().trim().split("");

let ans = 0;

while (T.length > 0) {
	if (JSON.stringify(S) === JSON.stringify(T)) {
		ans = 1;
		break;
	}
	const lastLetter = T.pop();
	if (lastLetter === "B") T.reverse();
}

console.log(ans);
