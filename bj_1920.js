"strict mode";
const fs = require("fs");
const stdin = `5
4 1 5 2 3
5
1 3 7 9 5`.split("\n");

function isExist(target) {
	// 이분탐색
	let start = 0;
	let end = N - 1;

	while (start <= end) {
		let mid = Math.floor((start + end) / 2);
		if (target === orderedA[mid]) return 1;

		if (target < orderedA[mid]) end = mid - 1;
		else if (target > orderedA[mid]) start = mid + 1;
	}

	return 0;
}

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

const N = +input();
const A = input().split(" ").map(Number);
const orderedA = [...A].sort(function (a, b) {
	return a - b;
});
const M = +input();
const nums = input().split(" ").map(Number);

nums.forEach((num) => {
	const res = isExist(num);
	console.log(res);
});
