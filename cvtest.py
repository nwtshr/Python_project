# -*- coding: utf-8 -*-

import cv2

def main():
    gray = cv2.imread("test.jpg",0)     # 入力画像をグレースケールで取得
    edge = cv2.Canny(gray, 100, 200)    # Cannyアルゴリズムでエッジ検出
    cv2.imshow("Show Image",edge)       # エッジ画像を表示
    cv2.waitKey(0)                      # キー入力待機
    cv2.destroyAllWindows()             # ウィンドウ破棄


if __name__ == '__main__':
    main()
