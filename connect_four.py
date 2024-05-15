def print_table(data):                                                    # 影印出棋盤的函數，data代表輸入的資料
    print('+'+'---+'*7)                                                   # 印出棋盤最上方，用'+'連接不會在中間產生空格，','則會
    for i in range(5,-1,-1):                                              # 總共6列，從資料最尾端由上往下印
        for j in range(7):                                                # 總共7行
            print('| ' + data[j][i] + ' ', end='')                        # 將每行資料出來，end函數則使下次呼叫print函數時直接接後面print不換行
        print('|')
        print('+'+'---+'*7)
    for j in range(7):
        print('  '+str(j)+' ', end='')                                    # 將輸出由數字型態轉為文字型態
    print(' ')

def input_ox(data, t):                                                    # 輸入資料，t代表次數，用來判別X或O輸入
    if t%2==0:
        text = 'Player X >> '
    else :
        text = 'Player O >> '                                             # 以判別式來給予input時輸出的文字
    while True :
        col = input(text)
        if len(col)==1 and ord('0') <= ord(col) <= ord('6') :             # ord:將文字轉換成ASCII標號，先設定字串長度為1防止轉換出錯
            go = int(col)                                                 # 確保col為整數且len=1後轉成整數型來呼叫list內容
            if ' ' in data[go] :
                put = data[go].index(' ')                                 # 先判別選取該行是否有空格，再找有空格的最小位置，用OX取代
                if t%2==0:
                    data[go][put] = 'X'
                else :
                    data[go][put] = 'O'                                   # 取代空格之內容判別式
                break
            else :
                print('This column is full. Try another column.')
        else :
            print('Invalid input, try again [0-6].')

def referee(data):                                                        # 是否連線的判別式
    # row
    for i in range(len(data[0])):                                         # 列欄位是各行欄位的相同位置，因此二重for迴圈需要寫相反
        for j in range(len(data)-3):                                      # 由於連線需要佔四行，因此實際上可能在線最左端的行數僅有四行，我們便-3以方便計算
            test = [data[j+k][i].upper() for k in range(4)]               # 由於可能會有四個以上的連線，所以另外創造list將要比較的元素裝進去處理，以免破壞資料
            if test.count(test[0]) == len(test):                          # 如果每個都長一樣，那在使用count函數將=4，和長度剛好相同
                    w = data[j][i].lower()
                    for k in range(4):
                        data[j+k][i] = w                                  # 統一將連線之元素在data裡變換成小寫，下面另外三種處理大同小異
    # column
    for i in range(len(data)):                                            # 正常處理
        for j in range(len(data[i])-3):
            test = [data[i][j+k].upper() for k in range(4)]
            if test.count(test[0]) == len(test):
                    w = data[i][j].lower()
                    for k in range(4):
                        data[i][j+k] = w
    # slash whose slope is positive
    for i in range(len(data)-3):
        for j in range(len(data[i])-3):                                   # 由於斜線可能佔4x4的格子，所以行列各減3跑for loop
            test = [data[i+k][j+k].upper() for k in range(4)]             # 由於第一行的第一筆資料位於左下，因此行列皆要增加
            if test.count(test[0]) == len(test):
                    w = data[i][j].lower()
                    for k in range(4):
                        data[i+k][j+k] = w
    # slash whose slope is negative
    for i in range(len(data)-3):
        for j in range(len(data[i])-1, len(data[i])-4, -1):               # 斜率為負之斜線從左上開始，因此列欄位要從尾到頭，行欄位正常順序
            test = [data[i+k][j-k].upper() for k in range(4)]
            if test.count(test[0]) == len(test):
                    w = data[i][j].lower()
                    for k in range(4):
                        data[i+k][j-k] = w

def main():                                                               # 主要運作函式
    data = [[' ',' ',' ',' ',' ',' '] for i in range(7)]                  # 生成空白資料
    t = 0                                                                 # 次數從0開始，偶數X，奇數O
    while True:
        input_ox(data, t)                                                 # 最先輸入，其次判別，最後再繪圖
        t += 1                                                            # 每輸入完一次便+1
        referee(data)
        print_table(data)
        w = True                                                          # 用作break停止之因子
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j].islower():                                  # 尋找資料是否為小寫英文字母已判別勝負是否已分
                    print('Winner:', data[i][j].upper())
                    w = False                                             # 轉換成True以分別將大小迴圈和while迴圈停止
                    break
            if w == False :
                break
        if w == False :
            break
        blank = [(' ' not in data[i]) for i in range(len(data))]          # 若可能平手，對每行資料尋找是否有空格並使用boolean值判別
        if False not in blank:                                            # 如果沒有False代表每行皆無空格，即為平手
            print('Draw')
            break

main()                                                                    # 實際運作

