"strict mode";
const stdin = require("fs")
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
	.toString()
	.split("\n");

// 막걸리의 용량은 2^31 -1 보다 작거나 같은 자연수 또는 0이다 & 1초

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

const [N, K] = input().split(" ").map(Number);

makgullis = [];
for (i = 0; i < N; i++) {
	makgullis.push(+input());
}

let [left, right] = [0, 2 ** 31 - 1];
let mid;
let res = 0;

while (left <= right) {
	mid = Math.floor((left + right) / 2);

	let cnt = 0;
	for (const makgulli of makgullis) {
		cnt += Math.floor(makgulli / mid);
	}

	if (cnt < K) {
		right = mid - 1;
	} else {
		left = mid + 1;
		res = Math.max(res, mid);
	}
}

console.log(res);
