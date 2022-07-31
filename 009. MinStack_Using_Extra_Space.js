class MinStack {
    constructor() {
        this.stack = [];
        this.supportingStack = [];
    }

    push(val) {
        this.stack.push(val);
        if(this.supportingStack.length > 0){
            let top = this.supportingStack[this.supportingStack.length - 1];
            if( top >= val){
                this.supportingStack.push(val);
            }
        } else{
            this.supportingStack.push(val);
        }
    }


    pop() {
        let val = this.stack.pop();
        let top = this.supportingStack[this.supportingStack.length - 1];
        if( top === val){
            this.supportingStack.pop();
        }
    }

    getMin() {
        console.log("The min element in stack :", this.supportingStack.length > 0 ? this.supportingStack[this.supportingStack.length - 1] : -1);
    }
}


const minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.getMin(); // return -2
