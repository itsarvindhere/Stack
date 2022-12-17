/*

    Given an array arr[] of size N having distinct elements, the task is to find the next smaller element for each element of the array in order of their appearance in the array.

    Next smaller element of an element in the array is the nearest element on the right which is smaller than the current element.

    If there does not exist next smaller of current element, then next smaller element for current element is -1. For example, next smaller of the last element is always -1.


    e.g. [ 1, 3, 2, 4]

    Here, if we take 1, all elements to its right are greater than it. So, there is no element that is smaller than 1 on its right. Hence for 1, the output is -1.

    For 3, only 2 is smaller on the right. Hence output is 2. 
    
    For 2, the only element to the right is 4. Since 4 is not smaller than 2, output is -1. 

    Finally, since 4 is the last element, automatically its output is -1.

    So, we have to return an array -> [-1, 2, -1, -1]

*/

//SOLUTION 

/*

    We can use a stack here because if we try to use a brute force approach, we will see a nested for loop where the inner loop depends on the outer loop (j = i + 1)

    So, using a stack, we need to iterate from the end of the given array and for each element, check if the top of stack has a smaller element or not. THe stack basically stores the elements to the right of an element. 

    If top is smaller, push the top to output array. Otherwise, pop the top element and move to the next element in stack. Keep doing it until stack is empty. If stack becomes empty, just push -1 to the output array since no element to right is smaller.

    No matter how big array is, the last element will have no elements to its right. So always for the last element, the output value will be -1. 
    
    We can use this to already set the output value for last as -1.

*/

function nextSmallerElement(arr, n)
    {
        let output = new Array(n);
        output[n - 1] = -1;

        let stack = [arr[arr.length-1]];
        
        for(let i = n - 2; i >= 0; i--) {
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