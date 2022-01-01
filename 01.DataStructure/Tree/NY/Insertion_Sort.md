# Insertion Sort 삽입정렬

### summary : 이미 정렬된 array를 유지, 새로운 숫자가 "삽입"되면 정렬된 array 안에서 자기의 자리를 찾아가며 정렬
<br>

## 1. 원리 및 예시
<img src="https://postfiles.pstatic.net/MjAyMTAyMjdfMTg5/MDAxNjE0NDEyNTc2OTQx.aKYInKO1l_GhEyzK2ouylBe7XSSnCiS7kvMjzlXzKs4g.RWahau3NJx-VqWo4_FeSb-XoTjCR6AeXsKeZcdVlfjsg.PNG.comb0703/insertion_sort-recursion.png?type=w773"><br>
이미지 출처 : https://blog.naver.com/comb0703/222258698264
<br>

## 2. 코드 예시 - Python
``` py
def insertionSort(x):
    for size in range(1, len(x)):
        val = x[size]
        i = size
        while i > 0 and x[i-1] > val:
            x[i] = x[i-1]
            i -= 1
        x[i] = val
```


## 3. Time Complexity
- O(n^2)
- best : O(n) => 이미 정렬되어 있을 때
- worst : O(n^2) => 역순으로 정렬되어 있을 때