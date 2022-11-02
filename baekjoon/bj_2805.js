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
trees = input().split(" ").map(Number);

let [left, right] = [1, 2000000000];
let H = 0;
let mid;

while (left <= right) {
	mid = Math.floor((left + right) / 2);

	let cnt = 0;
	for (const tree of trees) {
		if (tree - mid > 0) {
			cnt += tree - mid;
		}
	}
	if (cnt < M) {
		right = mid - 1;
	} else {
		H = mid;
		left = mid + 1;
	}
}

console.log(H);
