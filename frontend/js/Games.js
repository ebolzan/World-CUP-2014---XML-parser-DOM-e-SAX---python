class DateTimeGame{

    monName = new Array ("janeiro", "fevereiro", "março", "abril", "maio", "junho","julho", "agosto", "outubro", "novembro", "dezembro")


    constructor(datetimeInfo){
        let textArray = datetimeInfo.trim().split(" ");

        this.day= textArray[1];
        this.monthAndYear = `${textArray[3]} de ${textArray[5]}`;
        this.hour = textArray[6];
        this.arena = textArray.slice(7);
        
    }

    get Day() {
        return this.day;
    }

    get MonthAndYear(){
        return this.monthAndYear;
    }

    get Hour(){
        return this.hour;
    }

    get Arena(){
        return this.arena.toString();
    }

    get numericDate(){
        let arrayMonthYear = this.monthAndYear.split(" ");
        let monthNumber = this.monName.indexOf(arrayMonthYear[0]) + 1;

        return this.day= this.Day+ "/"+monthNumber+ "/" + arrayMonthYear[2];
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

    get PhaseName(){
        return this.phaseName;
    }

    get TeamA(){
        return this.TeamA;
    }

    get TeamB(){
        return this.teamB;
    }

    get partDay(){
        return this.datetimeInfo.Day;
    }

    get partMonthYear(){
        return this.datetimeInfo.MonthAndYear;
    }

    get partNumericDate(){
        return this.datetimeInfo.numericDate;

    }

    get placeGame(){
        return this.datetimeInfo.Arena;
    }

    
}


/* 
const games_of= [];

for(gameOne of games){
  //  console.log(gameOne);
    let [a, b, c, d] = gameOne.split(",",4);
    games_of.push(new Game(a, b, c, d));
}

//console.log(games_of);

for(obj of games_of){

    console.log(obj.placeGame);
}
 */