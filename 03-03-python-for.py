WEEK_LIST = ['月', '火', '水', '木', '金', '土', '日']
SUBJECT_LIST = ['Python', '数学', '機械学習', '深層学習','エンジニアプロジェクト']

def output_schedule(study_time_list):
    '''今週の勉強予定を出力します'''
    # １）４）に出てくるが、科目を番号で指定する必要があるため変数初期値を設定（後付けやけど）　
    SUBJECT_LIST_NUBER = 1
    #　２）print(dow,hour)  Day of the week とstudy hourの両方をzipでがっちゃんこ
    for dow,hour in zip(WEEK_LIST, study_time_list):

        if hour > 0:
        	print("{}曜日は、".format(dow) + str(hour)  + "時間勉強する予定です。")
        else:
        	print("{}曜日は、".format(dow) + "お休みです。")

        # ３）for文の中で何限目のfor文を回す→これで１行目の中で複数の行を回せる
        # ４）科目を順番にするためSUBJECT_LIST_NUMBERを初期値1で設定（数学から開始）
        for period in range(hour):
            print("{}限目 {}".format(period+1, SUBJECT_LIST[SUBJECT_LIST_NUBER]))
            SUBJECT_LIST_NUBER += 1
            if SUBJECT_LIST_NUBER == 5:
                SUBJECT_LIST_NUBER = 0


def main():
    '''勉強情報をoutput_scheduleに渡します'''
    # 1日に何時間勉強するか（1週間　月曜日〜日曜日）
    study_time_list = [3, 1, 3, 0, 4, 2, 2]
    output_schedule(study_time_list)


if __name__ == '__main__':
    main()
