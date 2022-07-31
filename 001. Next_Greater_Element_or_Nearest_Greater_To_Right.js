/*

    Given an array arr[] of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.

    Next greater element of an element in the array is the nearest element on the right which is greater than the current element.

    If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.


    e.g. [ 1, 3, 2, 4]

    Here, if we take 1, all elements to its right are greater than it. But the nearest element taht is greater than 1 is 3. Hence for 1, the output is 3.

    Similarly, for 3, only 4 is greater on the right. Hence output is 4. For 2, it is 4 and for 4, since there is no element to right, output is -1.

    So, we have to return an array -> [3,4,4,-1]

*/

//SOLUTION 

/*

    We can use a stack here because if we try to use a brute force approach, we will see a nested for loop where the inner loop depends on the outer loop (j = i + 1)

    So, using a stack, we need to iterate from the end of the given array and for each element, check if the top of stack has a bigger element or not. THe stack basically stores the elements to the right of an element. 

    If top is greater, push the top to output array. Otherwise, pop the top element and move to the next element in stack. Keep doing it until stack is empty. If stack becomes empty, just push -1 to the output array since no element to right is larger.

    No matter how big array is, the last element will have no elements to its right that are greater. So always for the last element, the output value will be -1. We can use this to already set the output value for last as -1.

*/

function nextLargerElement(arr, n)
    {
        let output = new Array(n);
        output[n - 1] = -1;

        let stack = [arr[arr.length-1]];
        
        for(let i = n - 2; i >= 0; i--) {
                while(stack.length > 0){
                    let top = stack[stack.length - 1];
                    if(top > arr[i]){
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
