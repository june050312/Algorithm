let targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

let cnt = 0

targets.sort((m1, m2) => {
    if (m1[1] < m2[1]) return -1
    if (m1[1] > m2[1]) return 1
    if (m1[1] === m2[1]) {
        if (m1[0] < m2[0]) return -1
        if (m1[0] > m2[0]) return 1
        if (m1[0] === m2[0]) return 0
    }
})

let e = 0
targets.forEach(target => {
    if (target[0] >= e) {
        cnt++
        e = target[1] 
    }
});

console.log(cnt);