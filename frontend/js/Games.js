
class Game{
    constructor(phaseName, datetimeInfo, teamA, teamB)
    {
        this.phaseName = phaseName;
        this.datetimeInfo = datetimeInfo;
        this.teamA = teamA;
        this.teamB = teamB;
       
    }

}

const games_of= [];

for(gameOne of games){
    console.log(gameOne);
    let [a, b, c, d] = gameOne.split(",",4);
    games_of.push(new Game(a, b, c, d));
}

for(obj of games_of){

    console.log(obj);
}
