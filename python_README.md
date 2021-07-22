# 개요(Overview)
python 코딩테스트 정리

## 자료형

- 리스트(list)

    - 중복 제거되지 않음
    
    - 항목 제거하기
        
        ```python
        a = ['aa','bb']
        a.remove('aa')
        print(a) # ['bb']
        ```
      
    - 리스트 합치기
    
        ```python
        a = ['aa','bb']
        b = ['aa','cc']
        a + b
        ```

- 튜플 (tuple)

    - 중복 제거되지 않음

- 사전 (dict)

    - 중복 제거됨

- 집합 (set)

    - 중복 제거됨

## 유용한 함수
- zip : 여러개의 리스트를 하나의 딕셔너리(사전)으로 통합, 리스트를 차례대로 묶음

    ```python
    zip(리스트1, 리스트2, 리스트3 ...)

    --------------------------------------

    number = [1,2,3,4]
    name = ['hong','gil','dong','nim']
    number_name = zip(number,name)
    list(n for n in number_name)  # for문 실행시 number_name 소멸됨
    ```

- map : 리스트를 순차적으로 함수에 대입?

    ```python
    map(함수, 적용할 리스트)

    --------------------------------------

    # 띄어 쓰기로 입력 두개 받기
    a,b = map(int, input.split())

    --------------------------------------

    def add(a):
        return a+1
    list(map(add,[1,2,3,4,5]))  # [2, 3, 4, 5, 6]

    --------------------------------------

    list(map(lambda a: a+1,[1,2,3,4,5]))  # [2, 3, 4, 5, 6]

    --------------------------------------

    list(map(lambda x : x,range(5)))  # [0, 1, 2, 3, 4]
    ```

- set : 집합 초기화 함수, 리스트 -> 집합 변환 함수, 리스트 입력시 중복 제거 가능, 초기화시 원래 정렬에서 다르게 바뀜

    ```python
    a = set([1,2,3])  # a = {1,2,3} 하고 동일

    --------------------------------------

    set([1,2,3,3])  # {1, 2, 3}
    ```

- sort : 정렬 함수, (리스트,튜플,딕셔너리,집합) 정렬됨

    ```python
    a = [3, 2, 1]
    a.sort()  # [1, 2, 3] , sort시 변수에 바로 적용, 오름차순으로 정렬됨
    a.sort()  # [3, 2, 1] , sort시 변수에 바로 적용, 내림차순으로 정렬됨

    --------------------------------------

    sorted([3, 2, 1])   # [1, 2, 3]

    sorted([3, 2, 1], reverse=True)  # [3, 2, 1] , 반대로 정렬
    ```
  
  
- sorted : 정렬 함수 

    ```python
    # key를 줘서 조건으로 정렬 가능
    sorted([(1,2,3),(1,2,3),(1,2,3)], key=(lambda x: (-x[0], -x[1], x[2])), reverse=True)
    ```
  

- enumerate : list for문에서 index, value 분리? 가능

    ```python
    a = [('pop',1),('pop',2),('pop',3)]

    for i,idx in enumerate(a):
        print('========')
        print(i)
        print(idx)

    # 결과
    ##  ========
    ##  0
    ##  ('pop', 1)
    ##  ========
    ##  1
    ##  ('pop', 3)
    ```

- min : list 중에 작은값 찾기
    ```python
    a = [1,2,3]
    print(min(a))

    # 결과
    1
    ```
