## Python_face_landmark
- 파이썬 dlib라이브러리를 이용한 얼굴 랜드마크 인식
- 학습시킨 모듈을 통해 함수를 불러오고 dlib, opencv, numpy 라이브러리를 이용한다.
- 기본 틀은 얼굴에 68개 점을 입히고 인식한다. 
- 얼굴 전체, 눈썹, 코, 눈, 입술, 얼굴형 등 전체와 부분 랜드마크 인식이 가능하다.

## 구현 결과
- 동영상 버전 얼굴 전체, 각 부위 별 랜드마크 인식 가능.
![image](https://user-images.githubusercontent.com/78295968/125156864-b99da500-e1a2-11eb-9263-302f0b89c4e1.png)
![image](https://user-images.githubusercontent.com/78295968/125156871-c4f0d080-e1a2-11eb-93e6-ae65754384f3.png)
![image](https://user-images.githubusercontent.com/78295968/125156879-cf12cf00-e1a2-11eb-92c1-ff52a3b3116f.png)
![image](https://user-images.githubusercontent.com/78295968/125156887-d89c3700-e1a2-11eb-830f-7fe601841d30.png)
![image](https://user-images.githubusercontent.com/78295968/125156892-dd60eb00-e1a2-11eb-8927-9770bacaf5f1.png)
![image](https://user-images.githubusercontent.com/78295968/125156924-fc5f7d00-e1a2-11eb-8b25-9bb8e856dca9.png)


-이모티콘 이미지 합성
<br>
![image](https://user-images.githubusercontent.com/78295968/125156950-21ec8680-e1a3-11eb-8cd9-9e4cec9daec0.png)
<br>

-특정 부위 랜드마크 인식 후 이모티콘 합성
<br>

![image](https://user-images.githubusercontent.com/78295968/125156968-3c266480-e1a3-11eb-8ca3-61a0cb1cc72a.png)
<br>웹캠 버전 얼굴 전체
<br>
![image](https://user-images.githubusercontent.com/78295968/125157057-ae974480-e1a3-11eb-8c04-d281a64cf0c5.png)

![image](https://user-images.githubusercontent.com/78295968/125156842-9541c880-e1a2-11eb-8997-89b5ebde7348.png)
<br>부분 가능.



## 여러가지 버전이 존재한다
- 데모 버전은 아래 Reference의 유튜브를 통해 만들었다.
- 웹캠버전, 준비한 동영상 버전 둘 다 가능하다.
- 나는 기존 데모 버전에 여러 기능들을 추가했다.
- 랜드마크 인식 후 이모티콘 등 이미지 삽입 기능을 추가했다.
- 특정 랜드마크 인식후 이모티콘 이미지 삽입 기능을 추가했다. (개선중)

## Reference
https://www.youtube.com/user/webnautes/videos

이 유튜브를 참조하여 공부하였고 

토대가 되는 코드에 추가하고 싶은 기능 추가중.
