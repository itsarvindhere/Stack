
class MinStack {
    constructor() {
        this.stack = [];
        this.minElement = -1;
    }

    push(val) {
        if(this.stack.length > 0){
            if(val < this.minElement) {
                // flag = 2 x (value to push) - minElement
                this.stack.push(2 * val - this.minElement);
                this.minElement = val;
            } else {
                this.stack.push(val)
            }
        } else{
            this.stack.push(val)
            this.minElement = val;
        }
    }


    pop() {
        let val = this.stack.pop();
        // Previous Minimum = 2 x currentMinimum - (value To Pop)
        let newMin = 2 * this.minElement - val; 
        this.minElement = newMin;
    }

    getMin() {
        console.log("The min element in stack :", this.minElement);
    }
}


const minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.getMin(); // return -2