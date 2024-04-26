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



console.log(field);