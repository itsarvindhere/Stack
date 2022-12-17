/*

    Given an array arr[] of size N having distinct elements, the task is to find the previous smaller element for each element of the array in order of their appearance in the array.

    Previous smaller element of an element in the array is the nearest element on the left which is smaller than the current element.

    If there does not exist previous smaller of current element, then previous smaller element for current element is -1. For example, previous smaller of the first element is always -1.


    e.g. [ 1, 3, 2, 4]

    Here, if we take 1, there is no element on the left of it. So, for 1, nearest smaller on the left is -1.

    Next we take 3, there is only one element to its left and it is 1. Since 1 is smaller than 3, that means for 3, nearest smaller is 1.

    Next is 2. Its nearest smaller on the left is 1 because 3 > 2 and 1 < 2. 

    And finally we have 4. Its nearest smaller is 2. 

    So, our output array becomes [-1, 1, 1, 2]

*/

//SOLUTION 

/*

    We can use a stack here because if we try to use a brute force approach, we will see a nested for loop where the inner loop depends on the outer loop (j = i - 1)

    So, using a stack, we need to iterate from the start of the given array and for each element, check if the top of stack has a smaller element or not. THe stack basically stores the elements to the left of an element. 

    If top is smaller, push the top to output array. Otherwise, pop the top element and move to the next element in stack. Keep doing it until stack is empty. If stack becomes empty, just push -1 to the output array since no element to left is smaller.

    No matter how big array is, the first element will have no elements to its left that are smaller. So always for the first element, the output value will be -1. We can use this to already set the output value for first as -1.

*/

function previousSmallerElement(arr, n)
    {
        let output = new Array(n);
        output[0] = -1;

        let stack = [arr[0]];
        
        for(let i = 1; i < n; i++) {
                while(stack.length > 0){
                    let top = stack[stack.length - 1];
                    if(top < arr[i]){
                        output[i] = top;
                        stack.push(arr[i]);
                        break;
                    } else{
                        stack.pop();
                    }
                }
                
                if(stack.length === 0){
                    output[i] = -1;
                    stack.push(arr[i])
                }
                
        }
            
           return output;
}

