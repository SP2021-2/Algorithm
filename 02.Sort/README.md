# 정렬 (Sort)

## 버블 정렬(Bubble Sort)
---

## 선택 정렬(Select Sort)
- 손시연
## 삽입 정렬(Insert Sort)
- 성나영
## 병합 정렬(Merge Sort)

### 1.병합정렬의 정의

-재귀용법을 활용한 정렬 알고리즘 
  
  1. 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
  2. 각 부분 리스트를 재귀적으로 합병정렬을 이용해 정렬한다.
  3. 두 부분 리스틀르 다시 하나의 리스트로 합병한다.

---

### 2. 알고리즘의 구성

-병합정렬은 크게 2가지의 부분으로 나눌 수 있다.

  * 1단계 : 정렬되지 않은 배열을 끝까지 분리하는 단계
  * 2단계 : 분리한 데이터를 단계별로 합치는 단계
  
-예시 : 
  1. list[1,9,3,2]가 존재
  2. list를 우선 [1,9] 와 [3,2]로 나눈다. (1단계)
  3. 나눈리스트에서 다시 [1] [9]로 나눈다 (1단계)
  4. [1]과 [9]를 순서에 맞게 다시 합친다.(2단계)
  5. 위에서 구한 리스트 [1,9]를 뒤에서 정렬된 [2,3]과 합친다. -> 앞에서 부터 비교하며 붙여간다. (2단계)
  6. 위의 결과를 실행하여 정렬된 list [1,2,3,9]를 얻을 수 있다.
 
---

### 3. 코드의 구성 

* 재귀가 일어나는 함수 부분

<pre>
<code>
def merge_sort(list):
  if( len(list) <= 1 ) :
    return list
    
  medium = (int)len(list)/2
  
  left = []   <- 함수에 매개변수로 들어온 코드를 slicing을 통해 나누어 준다.
  right = []
  
  left = merge_sort(left)
  right = merge_sort(right) <- 재귀적 부분이 일어나는 부분
  
  return merge( left, right)
</code>
</pre>

* 정렬된 함수를 다시 합치는 부분

<pre>
<code>

def merge( left, right ):
  mergedList = []
  leftPoint = 0
  rightPoint = 0
  
  while ( len(left) > leftPoint && len(right) > rightPoint):
    if (left[leftPoint] > right[rightPoint] ):
      mergedList.append(right[rightPoint])
      rightPoint += 1
    else:
      mergedList.append(left[leftPoint])
      leftPoint += 1
   
   if ( len(right) > rightPoint ):
    나머지 부분 모두 mergedList에 삽입
   elif ( len(left) < leftPoint):
    나머지 부분 모두 mergedList에 삽입

</code>
</pre>

---

### 4.알고리즘 분석 

- 시간 복잡도
  1. 각 단계마다 배열의 길이가 반으로 나누어진다.   
  2. 각 단계마다 하나의 노드의 길이는 n / (2^i) 가 됨을 알 수 있다.
  3. 각 단계에는 2^i의 노드가 들어있다.
  4. 각 단계의 모든 값을 비교하므로 각 단계는 n / (2^i) * 2^i = O(n) 이다.
  5. 단계는 log(n) = O(logn) 만큼 만들어진다.
  6. 따라서 총 시간 복잡도는 O ( n * logn ) 이다.


## 힙 정렬 (Heap Sort)

## 퀵 정렬(Quick Sort)
