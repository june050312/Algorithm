let targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

let fieldLength = 0
targets.forEach(target => {
    Math.max(...target) > fieldLength ? fieldLength = Math.max(...target) : fieldLength
});

let field = new Array(fieldLength).fill(0)

targets.forEach(target => {
    for (let i=target[0]-1;i<target[1];i++) {
        field[i]++
    }
});

let cnt = 0
while(1) {
    let flag = 0
    field.forEach(element => {
        flag += element
    });
    if (flag == 0) {
        break
    }

    let removes = []
    let pos = field.indexOf(Math.max(...field)) + 1.5

    targets.forEach(target => {
        if (target[0] < pos && pos < target[1]) {
            removes.push(target)
        }
    });

    removes.forEach(remove => {
        for (let i=remove[0]-1;i<remove[1];i++) {
            field[i]--
        }
    });
    cnt++
}

console.log(cnt);