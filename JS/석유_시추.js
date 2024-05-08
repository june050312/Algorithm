const land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]

for (let i=0;i<land[0].length;i++) {
    for (let j=0;j<land.length;j++) {
        let cnt = 0
        if (land[j][i] == 1) {
            cnt++
            let goRight = 1
            while (land[j][i+goRight] == 1) {
                let goDown = 1
                while (land[j+goDown][i] == 1) {
                    cnt++
                    goDown++
                }
                goRight++
            } 
        }
    }
}