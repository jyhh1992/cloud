function bubbleSort(arr) {
  const len = arr.length;
  for (let i = 0; i < len - 1; i++) {
    for (let j = 0; j < len - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        const cache = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = cache;
      }
    }
  }
  return arr;
}
function selectionSort(arr) {
  const len = arr.length;

  for (let i = 0; i < len; i++) {
    let maxIdx = len - i - 1;
    for (let j = 0; j < len - i; j++) {
      if (arr[j] > arr[maxIdx]) maxIdx = j;
    }
    if (maxIdx !== i) {
      const cache = arr[maxIdx];
      arr[maxIdx] = arr[len - i - 1];
      arr[len - i - 1] = cache;
    }
  }
  return arr;
}
let arr1 = [3,45,23,45,67,89,34,56,76,34,34,56, 5, 7, 2, 8, 9, 10, 40, 23, 45, 67, 23, 33, 22, 54, 56, 67, 35,20,25,26,69,69,33,10,12, 25,36,69,69,87,55,65,45,12,1,89,8,8,7,8,72,6,59,71,7];

// bubble sort
let startTime = new Date().getTime();
console.log(startTime);
let sorted = bubbleSort(arr1);
let endTime = new Date().getTime();

/*console.log(endTime);
console.log(sorted);
console.log(`버블 정렬 수행시간 : ${endTime - startTime} ms`); */

// select sort 
let startTime2 = new Date().getTime();
console.log(startTime2);
let sorted2 = selectionSort(arr1);
let endTime2 = new Date().getTime();
/*
console.log(endTime2);
console.log(sorted2);
console.log(`버블 정렬 수행시간 : ${endTime - startTime} ms`);*/

function myFunction(){
  const h2 = (text) => `<h2>${text}</h2>`
  document.body.innerHTML += h2(`선택정렬 : ${sorted}`)
  document.body.innerHTML += h2(`버블정렬 : ${sorted2}`)
}
