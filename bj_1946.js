"strict mode";
const stdin = require("fs")
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
	.toString()
	.split("\n");

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

const T = Number(input());

for (let i = 0; i < T; i++) {
	const N = Number(input());
	let ans;

	let scores = [];
	for (let j = 0; j < N; j++) {
		scores.push(input().split(" ").map(Number));
	}

	scores.sort((a, b) => a[0] - b[0]);
	const scoresLength = scores.length;

	for (let p = 0; p < scoresLength; p++) {
		const x = scores[0][1];
		const [, interviewScore] = scores[p];

		if (interviewScore === 1) {
			ans = calculate(p, x);
		}
	}

	function calculate(idx, x) {
		let res = 0;
		for (let i = idx; i >= 0; i--) {
			if (scores[i][1] <= x) {
				res += 1;
			}
		}
		return res;
	}

	console.log(ans);
}
