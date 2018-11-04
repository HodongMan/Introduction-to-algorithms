# 2. 시작하기

  

## 2.1 삽입 정렬

  

입력 : `n개 수들의 수열`  <a1, a2, ....., an>

  

출력 : `a'1 <= a'2 <= ... <= a'n을 만족하는 입력 순열`(재배치)

  

의사코드는 일반적으로 소프트웨어 공학 관점의 문제를 고려하지 않는다.

그래서 데이터 추상화, 모듈화, 오류 처리 등의 문제가 종종 무시되는데, 이는 알고리즘의 본질을 좀 더 간결하고 분명하게 전달하기 위해서다.

  

```

INSERTION_SORT( A )

1 for j = 2 to A.length

2 key = A[j]

3 // A[j]를 정렬된 배열 A[1.. j - 1]에 삽입한다

4 i = j - 1

5 while i > 0 그리고 A[i] > key

6 A[i + 1] = a[i]

7 i = i - 1

8 A[i + 1] = key

```

  

### 루프 :불변성과 삽입 정렬의 타당성

  

```

1-8의 부분 배열 A[1..j-1]은 원래 A[1..j-1] 원소지만 for 루프가 반복을

시작할 때마다 정렬된 순서로 구성된다.

```

  

초기 조건 : 루프가 첫 번째 반복을 시작하기 전에 루프 불변성이 참이어야 한다.

  

유지 조건 : 루프의 반복이 시작되기 전에 루프 불변성이 참이었다면 다음 반복이 시작되기 전까지도 계속 참이어야 한다.

  

종료 조건 : 루프가 종료될 때 그 불변성이 알고리즘의 타당성을 보이는 데 도움이 될 유용한 특성을 가져야 한다.

  

#### 삽입 정렬 알고리즘에서 이런 특성이 과연 어떻게 만족하는지 확인하면

  

초기 조건 : 먼저 INSORTION_SORT의 루프가 시작되기 전(j = 2) 루프 불변성이 성립하는지 확인하면 된다.

이 때 부분 배열 A[1 ... j-1]은 한 개의 원소로 구성되는데 이 배열은 정렬되어 있다고 볼 수 있다. 따라서 반복 시작 전에 루프 불변성이 성립한다.

  

유지 조건 : 매 반복 시 루프 불변성이 유지되는지를 살펴 본다.

  

종료 조건 : 마지막으로 루프가 종료되었을 때 어떤 상황이 발생하는지를 확인해야 한다.

삽입 정렬의 경우 for 루프는 j가 A.length = n보다 커질 때(j = n + 1) 종료 된다. 유지 조건에 따라 A[1 ... n]은 같은 원소로 구성되어 있지만 정렬된 순서로 저장됨을 알 수 있다. A[1 ... n]이 전체 배열이므로 배열 전체가 정렬되었으며 따라서 알고리즘이 타당함을 말할 수 있다.

  
  

#### 연습문제

  

## 2.2 알고리즘의 분석

  

알고리즘의 분석은 그 알고리즘을 실행하는 데 필요한 자원을 예측하는 것을 의미 한다. 대부분의 경우에 측정 대상은 계산 시간이다.

  

### 삽입 정렬의 분석

  

입력 크기에 대한 가장 정확한 개념은 주어진 문제에 따라 다르다. 정렬이나 이산 푸리에 변환 계산과 같은 입력이 많은 문제에서 가장 자연스러운 척도는 입력 항목의 개수이다.

  

어떤 입력에 대한 알고리즘의 수행시간은 기본 연산 개수 또는 실행된 단계의 횟수를 말한다.

  

먼저 INSERTION-SORT 프로시저를 각 명령문의 실행에 따른 시간 비용과 실행 횟수를 먼저 고려해 살펴본다. n = A.length 일때 t[j]를 j = 2, 3, ..., n인 각 경우에 대해 5행에서 while 루프의 검사가 실행되는 횟수라고 하자. for나 while 루프가 일반적인 방법으로 종료된다고 하면 검사는 그 루프의 바디 부분과 한번 더 실행된다.

  

```

INSERTION_SORT( A ) cost times

1 for j = 2 to A.length

2 key = A[j]

3 // A[j]를 정렬된 배열 A[1.. j - 1]에 삽입한다

4 i = j - 1

5 while i > 0 그리고 A[i] > key

6 A[i + 1] = a[i]

7 i = i - 1

8 A[i + 1] = key

```

  

line 1 cost ![](https://latex.codecogs.com/gif.latex?c_1) times ![](https://latex.codecogs.com/png.latex?n)

line 2 cost ![](https://latex.codecogs.com/gif.latex?c_2) times ![](https://latex.codecogs.com/gif.latex?n-1)

line 3 cost ![](https://latex.codecogs.com/gif.latex?0) times ![](https://latex.codecogs.com/png.latex?n-1)

line 4 cost ![](https://latex.codecogs.com/gif.latex?c_4) times ![](https://latex.codecogs.com/png.latex?n-1)

line 5 cost ![](https://latex.codecogs.com/gif.latex?c_5) times ![](https://latex.codecogs.com/png.latex?\sum_{j=2}^{n}t_j)

line 6 cost ![](https://latex.codecogs.com/gif.latex?c_6) times ![](https://latex.codecogs.com/png.latex?\sum_{j=2}^{n}(t_j-1))

line 7 cost ![](https://latex.codecogs.com/gif.latex?c_7) times ![](https://latex.codecogs.com/png.latex?\sum_{j=2}^{n}(t_j-1))

line 8 cost ![](https://latex.codecogs.com/gif.latex?c_8) times ![](https://latex.codecogs.com/png.latex?n-1)

> **Note:** **값의 체크 등의 예외처리는** 위 설명처럼 하지 않습니다

알고리즘의 수행시간은 각 명령문 수행시간의 합이다. 즉, 수행시간 * 가격 만큼 기여하게 된다. 

![](https://latex.codecogs.com/gif.latex?T%28n%29%20%3D%20c_1n%20&plus;%20c_2%28n-1%29%20&plus;%20c_4%28n%20-%201%29%20&plus;%20c_5sum_%7Bj%3D2%7D%5E%7Bn%7Dt_j%20&plus;%20c_6sum_%7Bj%3D2%7D%5E%7Bn%7D%28t_j-1%29%20&plus;%20c_7sum_%7Bj%3D2%7D%5E%7Bn%7D%28t_j-1%29%20&plus;%20c_8%28n-1%29)

입력의 크기가 정해진 경우라도 어떤 입력이 주어지느냐에 따라 알고리즘의 수행 시간은 변한다. 

예를 들어서 INSERTION-SORT에서 최선의 상황은 배열이 이미 정렬된 경우다 그러면 j = 2, 3, ..., n의 각 경우에 대해
5행에서 A[i] <= Key가 된다 따라서 최선의 상황은 j = 2, 3, ..., n에 대해 수행시간은 다음과 같게 된다

![](https://latex.codecogs.com/gif.latex?T%28n%29%20%3D%20c_1n%20&plus;%20c_2%28n-1%29%20&plus;%20c_4%28n-1%29%20&plus;%20c_5%28n-1%29%20&plus;%20c_8%28n-1%29)

    ![](https://latex.codecogs.com/gif.latex?%3D%20%28c_1%20&plus;%20c_2%20&plus;%20c_4%20&plus;%20c_5%20&plus;%20c_8%29n%20-%20%28c_2%20&plus;%20c_4%20&plus;%20c_5%20&plus;%20c_8%29)


이 수행시간은 명령문의 비용에 의존하는 상수 a, b에 대한 an + b로 표현할 수 있다 즉, n에 관한 **선형 함수**가 된다.

배열이 역순으로, 즉 감소하는 순서로 정렬된 경우는 최악의 상황이다. 이 경우 각 A[j]를 정렬된 부분 배열 A[1...j-1]과 전부 비교해야 되므로 

![](https://latex.codecogs.com/gif.latex?%5Csum_%7Bj%3D2%7D%5E%7Bn%7Dj%3D%5Cfrac%7Bn%28n&plus;1%29%7D%7B2%7D-1)

최악의 경우 INSERTION-SORT의 수행시간은 다음이 된다.