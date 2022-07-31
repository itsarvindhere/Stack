/*  

    We are given an array which indicates the heights of buildings.We have to find the maximum area reactangle in the histogram that we make wit these heights. 

    When we analyze this problem, we will see that for each height, we will see what is the NSL and what is the NSR, we have to stop there. And whatever area is in between is the max area covered by that particular building. 


*/

// Method to get NSL index for each item in the array
const NSL  = (arr) => {

    let left = new Array(arr.length);
    let stack = [0]; //Push first index in stack
    let pseudoIndex = -1; //If NSL does not exist, we assume that the index before 0th index is the NSL index i.e., -1 index
    left[0] = pseudoIndex; //Set NSL for first element as -1

    for(let i = 1; i < arr.length; i++){
        while(stack.length > 0){
            let topIndex = stack[stack.length - 1];
            let top = arr[topIndex];
            if(top < arr[i]){
                left[i] = topIndex;
                stack.push(i);
                break;
            } else{
                stack.pop();
            }
        }
    
        if(stack.length === 0){
            left[i] = pseudoIndex;
            stack.push(i);
        }
    }

    return left;
}

// Method to get NSR index for each item in the array
const NSR  = (arr) => {

    let right = new Array(arr.length);
    let stack = [arr.length - 1]; //Push last index in stack
    let pseudoIndex = arr.length; //if NSR does not exist, we assume that the index after last index is the NSR index. i.e., n or length of heights array

    right[arr.length - 1] = pseudoIndex; //Set the NSR for last index as last index + 1 or the length of given array


    for(let i = arr.length - 2; i >= 0; i--){
        while(stack.length > 0){
            let topIndex = stack[stack.length - 1];
            let top = arr[topIndex];
            if(top < arr[i]){
                right[i] = topIndex;
                stack.push(i);
                break;
            } else{
                stack.pop();
            }
        }

        if(stack.length === 0){
            right[i] = pseudoIndex;
            stack.push(i);
        }
    }
    return right;
}

// MAH (Max Area in Histogram) Method
const MAH = (arr) => {
    let left = NSL(arr);
    let right = NSR(arr);

    let maxArea = 0;

    arr.forEach((height, i) => {
        let area = height * (right[i] - left[i] - 1);
        if(area > maxArea){
            maxArea = area;
        }
    })

    return maxArea;
}

// An array of heights of buildings
let arr = [6,2,5,4,5,1,6];
console.log("Maximum Area in Histogram is: ", MAH(arr))



