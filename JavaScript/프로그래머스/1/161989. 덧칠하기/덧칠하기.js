function solution(n, m, section) {
    let cnt = 0

    for (let i=1;i<=n;i++) {
        if (i == section[0]) {
            cnt += 1
            do {
                section.shift()
            } while (section.length != 0 && section[0] < i + m);
        }
    }

    return cnt;
}