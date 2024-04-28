const park = ["SOO","OOO","OOO"]
const routes = ["E 2", "N 2"]

let loc, temp

for (let i=0;i<park.length;i++) {
    if (park[i].indexOf("S") != -1) {
        loc = [i, park[i].indexOf("S")]
        break
    }
}

routes.forEach(route => {
    let flag = 1

    let [ dir, dis ] = route.split(" ")
    dis = parseInt(dis)

    temp = [...loc]
    
    for (let i=0;i<dis;i++) {
        switch (dir) {
            case "N":
                temp[0] -= 1
                break;
            case "S":
                temp[0] += 1
                break;
            case "W":
                temp[1] -= 1
                break;
            case "E":
                temp[1] += 1
                break;
        }
        if (temp[0] >= park.length || temp[0] < 0 || temp[1] >= park[0].length || temp[1] < 0 || park[temp[0]][temp[1]] == "X") {
            flag = 0
            break;
        }
    }
    if (flag) {
        loc = temp
    }
});

console.log(loc)