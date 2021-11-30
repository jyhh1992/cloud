function selectionSort(arr) {
  const arrLen = arr.length;
  for (let i = 0; i < arrLen; i++) {
    let minIdx = i; // 작은 값이 있는 인덱스
    for (let j = i + 1; j < arrLen; j++) {
      // 기준값인 minIdx의 위치 값보다 작은 값이면 minIdx에 j를 대입
      if (arr[minIdx] > arr[j]) minIdx = j;
    }
    if (arr[i] !== arr[minIdx]) {
      [arr[minIdx], arr[i]] = [arr[i], arr[minIdx]];
    }
  }
  return arr;
}
function bubbleSort(arr) {
  const arrLen = arr.length;
  for (let i = 0; i < arrLen - 1; i++) {
    for (let j = 1; j < arrLen - i; j++) {
      if (arr[j - 1] > arr[j]) {
        //javascript swapping 기능 : [a, b] = [b, a];
        [arr[j], arr[j - 1]] = [arr[j - 1], arr[j]];
      }
    }
  }
  return arr;
}
let arr1 = [3,45,23,45,67,89,34,56,76,34,34,56, 5, 7, 2, 8, 9, 10, 40, 23, 45, 67, 23, 33, 22, 54, 56, 67, 35,20,25,26,69,69,33,10,12, 25,36,69,69,87,55,65,45,12,1,89,8,8,7,8,72,6,59,71,7];

// bubble sort
let sorted = bubbleSort(arr1);

// select sort 
let sorted2 = selectionSort(arr1);

function myFunction(){
  const h2 = (text) => `<h2>${text}</h2>`
  document.body.innerHTML += h2(`선택정렬 : ${sorted}`)
  document.body.innerHTML += h2(`버블정렬 : ${sorted2}`)
}
