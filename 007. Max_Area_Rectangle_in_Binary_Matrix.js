//---------------------------------------------- MAX AREA IN HISTOGRAM LOGIC ------------------------------------------ 

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

//-------------------------------------------------------------------------------------------


let matrix = [
    [0,1,1,0],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,0,0]
];

let histograms = [matrix[0]];
let prev = histograms[0];

for(let i = 1; i < matrix.length; i++){
    let histogram = [];
    for(let j = 0; j < matrix[0].length; j++){
        if(matrix[i][j] === 0){
            histogram.push(0)
        } else{
            histogram.push(matrix[i][j] + prev[j]);
        }
    }
    histograms.push(histogram);
    prev = histogram;
}

let maxArea = 0;
histograms.forEach(histogram => {
    let area  = MAH(histogram);
    if(area > maxArea){
        maxArea = area;
    }
})

console.log("Maximum Rectangular Area in the given matrix is: ", maxArea)
