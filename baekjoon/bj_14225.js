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
const S = input().split(" ").map(Number);
let visited = Array(N * 100000 + 1).fill(0);

const subsets = (nums) => {
	const dfs = (start = 0, sum = 0, depth = 0) => {
		visited[sum] = 1;

		if (depth === N) return;

		for (let i = start; i < nums.length; i++) {
			dfs(i + 1, sum + nums[i], depth + 1);
		}
	};

	dfs();
};

subsets(S);

for (let i = 1; i < visited.length; i++) {
	if (!visited[i]) {
		console.log(i);
		break;
	}
}
