players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

callings.forEach((element) => {
    runner = players.indexOf(element)
    passed = runner - 1

    var temp = players.splice(runner, 1, players[passed])
    players.splice(passed, 1, temp[0])
})

console.log(players);