
const STATE_STOP = 0 ;
const STATE_UP = 1 ;
const STATE_DOWN = -1 ; 

class JessicaElevator {
    nowFloor = 0;
    state = STATE_STOP
    consumers = [];
    aimFloors = [];
    downW = true;
    draw ;
    constructor(numberOfFloors, eventHandler ){
        this.numberOfFloors = numberOfFloors ;
        this.eventHandler = eventHandler ;
        this.draw = new Draw(numberOfFloors);
    }
    next() {
        // console.log("next");
        this.eventHandler.arrivedEvent( this.state, this.nowFloor ) ;
        for(let i=0 ;i<this.consumers.length ;i++){
            if((this.consumers[i].fromFloor > this.nowFloor)||(this.aimFloors[i] > this.nowFloor)){
                this.state = STATE_UP;
                this.downW = false;
                // console.log("move"); //
                // this.nowFloor = this.nowFloor + this.state;
                // console.log(this.nowFloor);  //
            }
            // else if((this.consumers[i].fromFloor < this.nowFloor)||(this.aimFloors[i] < this.nowFloor)){
            //     if(this.state == STATE_DOWN){
            //         this.state = STATE_UP;
            //     }else if(this.state == STATE_UP){
            //         this.state = STATE_DOWN;
            //     }
            // }
        }
        if(this.downW){
            for(let i=0 ;i<this.consumers.length ;i++){
                if((this.consumers[i].fromFloor > this.nowFloor)||(this.aimFloors[i] > this.nowFloor)){
                    this.state = STATE_DOWN;
                }
            }
        }
        console.log(this.state);    //
        this.nowFloor = this.nowFloor + this.state;
        console.log(this.nowFloor);  //

        this.draw.drawing(this.nowFloor);
    }
    up(fromFloor) {
        this.consumers.push(new Consumer(fromFloor,STATE_UP));
        // console.log(this.consumers);    //
    }
    down(fromFloor) {
        this.consumers.push(new Consumer(fromFloor,STATE_DOWN));
        // console.log(this.consumers);    //
    }
    goTo(toFloor) {
        this.aimFloors.push(toFloor);
        console.log(this.aimFloors);    //
    }
}

class Consumer {
    fromFloor = 0;
    state = STATE_STOP;
    constructor(formFloor,state){
        this.fromFloor = formFloor;
        this.state = state;
    }
}

class Draw {
    numberOfFloors = 0 ;
    floorHight ;
    constructor(numberOfFloors){
        this.numberOfFloors = numberOfFloors;
        this.floorHight = canvas.height/this.numberOfFloors
    }
    floor(){
        ctx.beginPath();
        for(let i=0 ; i<canvas.height ; i+=this.floorHight ){
            ctx.moveTo(0,i);
            ctx.lineTo(canvas.width,i);
        }
        ctx.stroke();
    }
    elevator(nowFloor){
        ctx.beginPath();
        ctx.fillRect(canvas.width-this.floorHight, (this.numberOfFloors-nowFloor-1)*this.floorHight, this.floorHight, this.floorHight);
        ctx.stroke();
    }
    clean(){
        ctx.clearRect(0,0,canvas.width,canvas.height);
    }
    people(){
        ctx.beginPath();
        ctx.arc(100, 100, 20, 0, 360);
        ctx.stroke();
    }
    drawing(elevatorNowFloor){
        this.clean();
        this.floor();
        this.elevator(elevatorNowFloor);
        this.people();
    }
}