function solution(wallpaper) {
    let result = [0, wallpaper[0].length, wallpaper.length, 0]
let [startFlag, endFlag] = [1, 0]
wallpaper[wallpaper.length - 1].indexOf("#") == -1 ? endFlag = 1 : endFlag

for (let i=0;i<wallpaper.length;i++) {
    if (startFlag && wallpaper[i].indexOf("#") != -1) {
        result[0] = i
        startFlag = 0
    }
    wallpaper[i].indexOf("#") < result[1] && wallpaper[i].indexOf("#") != -1 ? result[1] = wallpaper[i].indexOf("#") : result[1]
    if (endFlag && wallpaper[i].indexOf("#") != -1) {
        result[2] = i + 1
    }
    wallpaper[i].lastIndexOf("#") + 1 > result[3] ? result[3] = wallpaper[i].lastIndexOf("#") + 1 : result[3]
    
}
    return result;
}