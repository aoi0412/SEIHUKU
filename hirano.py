import cv2
from cv2 import aruco
import numpy as np

DEKA_MARKER_ID = 0
SMALL_MARKER_1_ID = 1
SMALL_MARDER_2_ID = 2


# テスト用関数
def Test():
    ### --- aruco設定 --- ###
    dict_aruco = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters()
    frameMarkers = None

    frame = cv2.imread("./images/testImage.jpg")
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    corners, ids, rejectedImgPoints = aruco.ArucoDetector(dictionary=dict_aruco,detectorParams=parameters).detectMarkers(gray)
    detectEachMarker(corners=corners,ids=ids)


### この関数を使うこと ###
# マーカー一覧からデカマーカーとスモールマーカーの識別を行う
def detectEachMarker(corners,ids):
    dekaMarkerIndex = np.where(ids == DEKA_MARKER_ID)[0][0]
    smallMarker1Index = np.where(ids == SMALL_MARKER_1_ID)[0][0]
    smallMarker2Index = np.where(ids == SMALL_MARDER_2_ID)[0][0]


    if(type(dekaMarkerIndex) != np.int64 or type(smallMarker1Index) != np.int64 or type(smallMarker2Index) != np.int64):
        print('画像からすべてのマーカーを検出できませんでした')
        return None
    dekaMarker = getEachPositions(corners[dekaMarkerIndex][0])
    smallMarker1 = getEachPositions(corners[smallMarker1Index][0])
    smallMarker2 = getEachPositions(corners[smallMarker2Index][0])
    print({
        'dekaMarker':dekaMarker,
        'smallMarker1':smallMarker1,
        'smallMarder2':smallMarker2
    })
    return {
        'dekaMarker':dekaMarker,
        'smallMarker1':smallMarker1,
        'smallMarder2':smallMarker2
    }



# それぞれ中心点と右上，左上，右下，左下の座標を算出して返す
def getEachPositions(corner):
    if(len(corner)<4):
        print('座標の数が足りません')
        return None
    # 座標をx座標でソートして、左側と右側の点を分ける
    sorted_by_x = sorted(corner, key=lambda x: x[0])

    # 左側の点をy座標でソートして、左上と左下を分ける
    left_points = sorted(sorted_by_x[:2], key=lambda x: x[1], reverse=True)
    lt, lb = left_points

    # 右側の点をy座標でソートして、右上と右下を分ける
    right_points = sorted(sorted_by_x[2:], key=lambda x: x[1], reverse=True)
    rt, rb = right_points

    # 四隅の中心の座標を計算
    center_x = sum(point[0] for point in corner) / 4
    center_y = sum(point[1] for point in corner) / 4
    center = [center_x, center_y]

    # 結果を辞書形式で格納
    result = {
        'lt': lt,
        'rt': rt,
        'lb': lb,
        'rb': rb,
        'center': center
    }
    print('左上 : {}'.format(result['lt']))
    print('右上 : {}'.format(result['rt']))
    print('左下 : {}'.format(result['lb']))
    print('右下 : {}'.format(result['rb']))

    print(result)

    return {'lt':lt, 'rt':rt, 'lb':lb, 'rb':rb,'center':center}

Test()