class DateTimeGame{

    constructor(datetimeInfo){
        let textArray = datetimeInfo.trim().split(" ");

        this.day= textArray[1];
        this.monthAndYear = `${textArray[2]} de ${textArray[4]}`;
        this.hour = textArray[5];

    }
}


class Game{
    constructor(phaseName, datetimeInfo, teamA, teamB)
    {        
        this.phaseName = phaseName.split(":")[1];
    
        this.datetimeInfo = new DateTimeGame(datetimeInfo);

        this.teamA = teamA.split(":")[1];
       
        this.teamB = teamB.split(":")[1];       
    }
}



const games_of= [];

for(gameOne of games){
  //  console.log(gameOne);
    let [a, b, c, d] = gameOne.split(",",4);
    games_of.push(new Game(a, b, c, d));
}

console.log(games_of);

for(obj of games_of){

    console.log(obj.datetimeInfo.monthAndYear);
}
