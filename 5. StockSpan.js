/*

    We are given an array that shows the prices of the stock at each day of the week. We have to find for each price, how many consecutive smaller or equal to prices are there before it. 

    e.g. [100, 80, 60, 70, 60, 75, 85];

    For 70, there is 60 before it that is smaller. But before that is 80 which is not smaller. Hence, the output will be 2. 

    NOTE - 2 because we will also count the current day as well. So for 70, we take 70 and 60 both, not just 60.

    For 80, no smaller price before it. SO, for it, output is just 1. i.e, 80 only. 

    If we analyze, we are stopping as soon as we find a price on left that is greater than current day's price (or if no price on left). That means, we are finding the "NEAREST GREATER TO LEFT" of a price and checking how many prices are between the nearest greater and the current price.

    SO, this problem is just a variation of NGL problem.

    For the first element, the output will always be 1 since apart from it, there is no element on its left that is smaller or equa to  it. 

    ALso, as we keep poppign elements from stack, there may be one case where the stack becomes empty again. This will only happen if all the elements on the left of an element are smaller than it. SO in that case we won't be able to find a Nearest Greater element.

    e.g.

    [10, 20, 30, 40, 50]

    At 50, stack will have [40,30,20,10] in top down order. As we keep comparing each with 50, since they are smaller than 50, we keep popping them. At the end, stack will be empty.

    Looking at the array itself, we know taht for 50, the output needs to be 5. So, if stack is empty, we simply need to push index + 1 to output. Here index of 50 = 4 so push 4 + 1 = 5 into output and that's it.

*/




// let arr = [100, 80, 80, 70, 60, 75, 85];

 
calculateSpan(price, n)
    {        
        let stack = [0]; //Keeping the index of first element in stack instead of element itself
        let output = new Array(n);
        
        output[0] = 1; 
        
        for(let i = 1; i < n; i++){
            while(stack.length > 0){
                let topIndex = stack[stack.length - 1]; //get index at top of stack
                let top = price[topIndex]; //Use this index to get the top most element in stack
                
                if(top > price[i]){
                    output[i] = i - topIndex; //In output push the current element's index - index of top of stack
                    stack.push(i); //Push the index of current element in the stack
                    break;
                } else{
                    stack.pop();
                }
            }
            
            if(stack.length === 0){
                output[i] = i + 1; //This case will be true when for any day, there are no prices on the left that are bigger. All are lesser. That means, for that day, output is index + 1.
                stack.push(i)
            }
        }
        
        return output;
    }