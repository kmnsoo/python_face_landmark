import dlib 
import cv2 as cv
import numpy as np
import cv2, dlib, sys
scaler = 0.3
#얼굴 검출을 위해 디폴트 얼굴 검출기 사용
detector = dlib.get_frontal_face_detector()
#검출된 얼굴에서 눈, 코, 입 같은 랜드마크를 찾기 위해 사용할 학습 모델 로드 ('학습모델')
#아래 학습모델 'shape_predictor_68_face_landmarks.dat'은 구글링을 통해 다운 가능. 이 모델은 68개의 위치를 찾아준다.
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

#동영상 파일을 가져와서 이미 촬영한 동영상에 랜드마크 입히기
cap = cv.VideoCapture('girl.mp4')

overlay = cv2.imread('peach.png', cv2.IMREAD_UNCHANGED)

def overlay_transparent(background_img, img_to_overlay_t, x, y, overlay_size=None):
  bg_img = background_img.copy()
  # convert 3 channels to 4 channels
  if bg_img.shape[2] == 3:
    bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2BGRA)

  if overlay_size is not None:
    img_to_overlay_t = cv2.resize(img_to_overlay_t.copy(), overlay_size)

  b, g, r, a = cv2.split(img_to_overlay_t)

  mask = cv2.medianBlur(a, 5)

  h, w, _ = img_to_overlay_t.shape
  roi = bg_img[int(y-h/2):int(y+h/2), int(x-w/2):int(x+w/2)]

  img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))
  img2_fg = cv2.bitwise_and(img_to_overlay_t, img_to_overlay_t, mask=mask)

  bg_img[int(y-h/2):int(y+h/2), int(x-w/2):int(x+w/2)] = cv2.add(img1_bg, img2_fg)

  # convert 4 channels to 4 channels
  bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGRA2BGR)

  return bg_img
   
# range는 끝 값이 포함 안됨
#눈썹, 눈, 코, 입, 턱선의 번호가 정해져있다. 부위별 분리 후 출력 하기 위해 부위별 리스트 정의
ALL = list(range(0, 68)) 
RIGHT_EYEBROW = list(range(17, 22))
LEFT_EYEBROW = list(range(22, 27))
RIGHT_EYE = list(range(36, 42))
LEFT_EYE = list(range(42, 48))
NOSE = list(range(27, 36))
MOUTH_OUTLINE = list(range(48, 61))
MOUTH_INNER = list(range(61, 68))
JAWLINE = list(range(0, 17))

#결과물 초기 값은 전체 얼굴 랜드마크를 보여준다.
index = ALL

#웹캠으로부터 입력을 받으려면 while문을 통해 무한 반복을 해줘야 한다.
while True:

#웹캠으로부터 이미지를 가져와서 그레이스케일로 변환한다. (원래 코드)
    ret, img_frame = cap.read()
#내가 웹캠이 아닌 동영상 파일에 랜드마크 적용 후 동영상 파일 크기를 줄이기 위해 밑에 주석처리한 기존코드가 아닌 fram에 sacler를 씌우고
#데이터타입을 인트로 주어 리절트 동영상 파일의 크기를 조절했다
    img_frame = cv2.resize(img_frame, (int(img_frame.shape[1] * scaler), int(img_frame.shape[0] * scaler)))
    #img_gray = cv.cvtColor(img_frame, cv.COLOR_BGR2GRAY) (원래 코드)
    

#주어진 이미지에서 얼굴을 검출한다. 두 번째 아규먼트는 업샘플링 횟수이다. *업샘플링: 이미지 확대
    dets = detector(img_frame, 1)
    #dets = detector(img_gray, 1)
#검출된 얼굴 개수만큼 반복
    for face in dets:

        #얼굴에서 68개 점 찾기. 주어진 이미지 img_frame의 검출된 얼굴 영역 face에서 랜드마크 검출
        shape = predictor(img_frame, face)

#검출된 랜드마크를 리스트에 저장한다.
        list_points = []
        for p in shape.parts():
            list_points.append([p.x, p.y])

#리스트를 넘파이 배열로 변환해준다.
        list_points = np.array(list_points)

#검출된 랜드마크 중 index 변수에 지정된 부위만 이미지에 원으로 그려준다
        for i,pt in enumerate(list_points[index]):

            pt_pos = (pt[0], pt[1])
            cv.circle(img_frame, pt_pos, 2, (0, 255, 0), -1)

#검출된 얼굴 영역에 빨간색 사각형을 그려준다
        cv.rectangle(img_frame, (face.left(), face.top()), (face.right(), face.bottom()),
            (0, 0, 255), 3)
    ori = img_frame.copy()

    #detect faces
    faces = detector(img_frame)
    #face = faces[]

    
    
    dlib_shape = predictor(img_frame, face)
    #연산을 쉽게하기위해 numpy사용 그리고 shape_2d함수에 넣는다.
    shape_2d = np.array([[p.x, p.y] for p in dlib_shape.parts()])
    #compute center of face
    #numpy의 min, max함수를 이용하여 좌상단 우하단의 점을 구해준다
    top_left = np.min(shape_2d, axis=0)
    bottom_right = np.max(shape_2d, axis=0)
    
    #크기가 작으면 뒤에 * 1.8 등 숫자를 곱해서 키울 수있다. 소수점 있는 것을 곱하기 때문에 max앞에 int 사용
    face_size = int(max(bottom_right - top_left) * 1.3)  

    #얼굴의 중심을 구할 것이다. 모든 특징점의 평균을 구해 중심을 구한다.
    #평균이 소수점일 수 있어서 int로 설정한다.
    center_x, center_y = np.mean(shape_2d, axis=0).astype(np.int)

    result = overlay_transparent(ori, overlay, center_x -10, center_y  -25, overlay_size=(face_size, face_size))
#결과 영상을 화면에 보여준다
    cv.imshow('img', img_frame)
    cv2.imshow('result', result)
#키보드 입력을 받아 누르는 숫자에 따라 얼굴 전체, 부위 별로 보여준다.
    key = cv.waitKey(1)

#ESC키를 누르면 프로그램을 종료한다.
    if key == 27:
        break

#입력된 숫자에 따라 index 변수에 앞에서 지정한 리스트를 대입한다.
    elif key == ord('1'):
        index = ALL
    elif key == ord('2'):
        index = LEFT_EYEBROW + RIGHT_EYEBROW
    elif key == ord('3'):
        index = LEFT_EYE + RIGHT_EYE
    elif key == ord('4'):
        index = NOSE
    elif key == ord('5'):
        index = MOUTH_OUTLINE + MOUTH_INNER
    elif key == ord('6'):
        index = JAWLINE

#객체 해제
cap.release()