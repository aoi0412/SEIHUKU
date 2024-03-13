### マーカーの座標を抽出する
import cv2
from cv2 import aruco
import numpy as np
import time


realWidth = 20 # [cm]
realHeight = 11.5 # [cm]

# target="左上" or "右上" or "左下" or "右下"
# ランダムな座標が入っているposition1~4からtargetに基づいた座標を返す
def calcSpuarePlace(position1,position2,position3,position4, target):
    print("position1 is {}".format(position1))
    print("position2 is {}".format(position2))
    print("position3 is {}".format(position3))
    print("position4 is {}".format(position4))
    print("target is {}".format(target))
    tmpx = sorted([position1, position2, position3, position4], key=lambda x:x[0])
    tmpy = sorted([position1, position2, position3, position4], key=lambda x:x[1])
    for i,x in enumerate(tmpx):
        for j,y in enumerate(tmpy):
            if(x[0] != y[0] or x[1] != y[1]):
                continue
            if(i <=1 and j <= 1):
                if(target == "左上"):
                    print("x is {}".format(x))
                    return x
            elif(i <=1 and j > 1):
                if(target == "左下"):
                    print("x is {}".format(x))
                    return x
            elif(i > 1 and j <= 1):
                if(target == "右上"):
                    print("x is {}".format(x))
                    return x
            elif(i > 1 and j > 1):
                if(target == "右下"):
                    print("x is {}".format(x))
                    return x
    return None
    

class MarkSearch :

    ### --- aruco設定 --- ###
    dict_aruco = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters()
    frameMarkers = None

    def __init__(self, cameraID):
        self.cap = cv2.VideoCapture(cameraID)

    def getMarkPosition(self):
        """
        静止画を取得し、所望のマークの座標を取得する
        """
        frame = cv2.imread("./images/testImage.jpg")
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        corners, ids, rejectedImgPoints = aruco.ArucoDetector(dictionary=dict_aruco,detectorParams=parameters).detectMarkers(gray)
        print(type(frame))
        frameMarkers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
        cv2.imshow('detect', frameMarkers)

        markers = np.ravel(ids)
        if(len(markers) == 4 and 0 in markers and 1 in markers and 2 in markers and 3 in markers):
            tmp1 = corners[0][0]
            tmp2 = corners[1][0]
            tmp3 = corners[2][0]
            tmp4 = corners[3][0]
            lt = None
            rt = None
            lb = None
            rb = None
            # tmp1~4をx座標でソートする
            tmpx = sorted([tmp1, tmp2, tmp3, tmp4], key=lambda x:x[0][0])
            # tmp1~4をy座標でソートする
            tmpy = sorted([tmp1, tmp2, tmp3, tmp4], key=lambda x:x[0][1])
            print("tmpx is {}".format(tmpx))
            print("tmpy is {}".format(tmpy))
            
            for i,x in enumerate(tmpx):
                for j,y in enumerate(tmpy):
                    if(x[0][0] != y[0][0] or x[0][1] != y[0][1]):
                        continue
                    else:
                        print("x[0][0] is {}".format(x[0]))
                        print("i is {}".format(i))
                        print('j is {}'.format(j))
                    if(i <=1 and j <= 1):
                        result = calcSpuarePlace(x[0], x[1], x[2], x[3], "右下")
                        if(result is not None):
                            lt = result
                        else:
                            print("左上の座標が見つかりませんでした。")
                            exit()
                    elif(i <=1 and j > 1):
                        result = calcSpuarePlace(x[0], x[1], x[2], x[3], "右上")
                        if(result is not None):
                            lb = result
                        else:
                            print("左下の座標が見つかりませんでした。")
                            exit()
                    elif(i > 1 and j <= 1):
                        result = calcSpuarePlace(x[0], x[1], x[2], x[3], "左下")
                        if(result is not None):
                            rt = result
                        else:
                            print("右上の座標が見つかりませんでした。")
                            exit()
                    elif(i > 1 and j > 1):
                        result = calcSpuarePlace(x[0], x[1], x[2], x[3], "左上")
                        if(result is not None):
                            rb = result
                        else:
                            print("右下の座標が見つかりませんでした。")
                            exit()
            

            print('左上 : {}'.format(lt))
            print('右上 : {}'.format(rt))
            print('左下 : {}'.format(lb))
            print('右下 : {}'.format(rb))
            return {'lt':lt, 'rt':rt, 'lb':lb, 'rb':rb, 'frameMarkers':frameMarkers}

        return None

def drawCircle(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print("左クリックされました。")
        pointPostions.append((x,y))
        cv2.circle(param, (x,y), 5, (0,0,255), -1)

if __name__ == "__main__" :

    import cv2
    from cv2 import aruco
    import numpy as np
    import time

    ### --- aruco設定 --- ###
    dict_aruco = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters()

    ### --- parameter --- ###
    cameraID = 0
    cam0MarkSearch = MarkSearch(cameraID)
    markerPositions = None
    try:
        while True:
            markerPositions = cam0MarkSearch.getMarkPosition()
            if markerPositions is not None:
                break
            print("マーカーが検出されませんでした。")
            time.sleep(0.5)
        print("マーカーの座標を取得しました。")
    except KeyboardInterrupt:
        cam0MarkSearch.cap.release()
    if(markerPositions is None):
        print("マーカーが検出されませんでした。")
        exit()
    print("マーカーの座標を取得しました。")
    cv2.destroyWindow('detect')
    # frameMardersのマウスで選択した場所に円を描画する
    cv2.namedWindow('frame')
    pointPostions = []
    cv2.setMouseCallback('frame', drawCircle, param=markerPositions['frameMarkers'])
    print("マウスで選択した場所に円を描画します。")
    while True:
        cv2.imshow('frame', markerPositions['frameMarkers'])
        if(len(pointPostions) ==2):
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    lt = markerPositions['lt']
    rt = markerPositions['rt']
    lb = markerPositions['lb']
    rb = markerPositions['rb']
    a = pointPostions[0]
    b = pointPostions[1]

    # 算出に使う変数を全て出力する
    print("lt : {}".format(lt))
    print("rt : {}".format(rt))
    print("lb : {}".format(lb))
    print("rb : {}".format(rb))
    print("a : {}".format(a))
    print("b : {}".format(b))
    print("realWidth : {}".format(realWidth))
    print("realHeight : {}".format(realHeight))


    # 2点間の横の距離を計算する
    xLength = abs(a[0]-b[0])/abs( ( (lt[0] - rt[0]) + (lb[0] - rb[0]) ) /2) * realWidth
    # 2点間の縦の距離を計算する
    yLength = abs(a[1]-b[1])/abs( ( (lt[1] - lb[1]) + (rt[1] - rb[1]) ) /2) * realHeight

    # 2点間の距離を算出
    length = np.sqrt(xLength**2 + yLength**2)
    
    # 選択した２点を結ぶ線を描画する
    cv2.line(markerPositions['frameMarkers'], a, b, (0, 0, 255), 2, cv2.LINE_AA)

    # 選択した２点の中心にlengthを描画する
    cv2.putText(markerPositions['frameMarkers'], str(length)+"cm", (int((a[0]+b[0])/2), int((a[1]+b[1])/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    # lt,rt,lb,rbに円を描画する
    cv2.circle(markerPositions['frameMarkers'], (int(lt[0]), int(lt[1])), 5, (0,0,255), -1)
    cv2.circle(markerPositions['frameMarkers'], (int(rt[0]), int(rt[1])), 5, (0,0,255), -1)
    cv2.circle(markerPositions['frameMarkers'], (int(lb[0]), int(lb[1])), 5, (0,0,255), -1)
    cv2.circle(markerPositions['frameMarkers'], (int(rb[0]), int(rb[1])), 5, (0,0,255), -1)
    while True:
        cv2.imshow('frame', markerPositions['frameMarkers'])
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
