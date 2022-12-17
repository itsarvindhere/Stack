/*

    Given heights of the buildings. Find how much water can be trapped between the buildings (Each building is 1 unit in width)

*/


let arr = [3,0,0,2,0,4];

const maxOnLeft  = (arr) => {
    let output = new Array(arr.length);
    let maxLeft = arr[0];

    for(let i = 0; i < arr.length; i++){
        if(arr[i] >= maxLeft){
            output[i] = arr[i];
            maxLeft = arr[i]
        } else{
            output[i] = maxLeft;
        }
    }
    
    return output;
}

const maxOnRight  = (arr) => {
    let output = new Array(arr.length);
    let maxRight = arr[arr.length - 1];

    for(let i = arr.length - 1; i  >= 0; i--){
        if(arr[i] >= maxRight){
            output[i] = arr[i];
            maxRight = arr[i]
        } else{
            output[i] = maxRight;
        }
    }
    
    return output;
}

let maxLeft = maxOnLeft(arr);
let maxRight = maxOnRight(arr);

let waterTrapped = 0;

for(let i = 0; i < arr.length; i++){
    waterTrapped += (Math.min(maxRight[i],maxLeft[i])) - arr[i];
}

console.log("Water Trapped:", waterTrapped + " units.")

