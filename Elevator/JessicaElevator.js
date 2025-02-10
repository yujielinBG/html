
const STATE_STOP = 0 ;
const STATE_UP = 1 ;
const STATE_DOWN = -1 ; 

class JassicaElevator {
    
    constructor(numberOfFloors, eventHandler ){
        this.numberOfFloors = numberOfFloors ;
        this.eventHandler = eventHandler ;
    }
    next() {
        //this.eventHandler.arrivedEvent( this.state, this.elevatorPos ) ;
    }
    up(fromFloor) {
    }
    down(fromFloor) {
    }
    goTo(toFloor) {
    }
}

