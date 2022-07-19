"strict mode";
const stdin = require("fs")
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
	.toString()
	.split("\n");

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

function isDuck(idx, letter) {
	temp.push(idx);
	for (let j = idx; j < sound.length; j++) {
		if (sound[j] === duck[letter] && !visited[j]) {
			isDuck(j, (letter + 1) % 5);
			return;
		}
	}
}

const sound = input();
let visited = new Array(sound.length).fill(0);

const duck = ["q", "u", "a", "c", "k"];
let cnt = 0;
let temp = [];

for (let i = 0; i < sound.length; i++) {
	if (sound[i] === duck[0] && !visited[i]) {
		isDuck(i, 1);
		for (let k = 0; k < temp.length - (temp.length % 5); k++) {
			visited[temp[k]] = 1;
		}
		if (temp.length >= 5) cnt += 1;
		temp = [];
	}
}

if (visited.includes(0)) {
	console.log(-1);
} else {
	console.log(cnt);
}
