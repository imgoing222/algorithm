"strict mode";

const stdin = require("fs")
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
	.toString()
	.split("\n");

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

const [N, M] = input().split(" ").map(Number);

let 학기 = Array(N).fill(1);

let 선수과목 = [];
for (let i = 0; i < M; i++) {
	선수과목.push(
		input()
			.split(" ")
			.map((x) => Number(x) - 1)
	);
}

선수과목.sort((a, b) => a[0] - b[0]);

for (const [A, B] of 선수과목) {
	학기[B] = Math.max(학기[B], 학기[A] + 1);
}

console.log(학기.join(" "));
