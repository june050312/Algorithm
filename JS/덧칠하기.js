const n = 4
const m = 1
const section = [1, 2, 3, 4]

let cnt = 0

for (let i=1;i<=n;i++) {
    if (i == section[0]) {
        cnt += 1
        do {
            section.shift()
        } while (section.length != 0 && section[0] < i + m);
    }
}

console.log(cnt)