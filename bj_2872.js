"strict mode";

const stdin = require("fs")
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
	.toString()
	.split("\n");

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

function isOrdered(idx, num) {
	if (books[idx] === num) return true;
}

function findAnswer(i, N) {
	while (true) {
		if (i === 0) break;
		i--;
		N--;
		if (!isOrdered(i, N)) {
			N++;
			continue;
		}
		ans--;
	}
}

let N = Number(input());
let books = [];
for (let i = 0; i < N; i++) {
	books.push(Number(input()));
}

let ans = N - 1;

for (let j = 0; j < N; j++) {
	if (books[j] === N) {
		findAnswer(j, N);
		break;
	}
}

console.log(ans);
