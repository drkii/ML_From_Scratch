course_dict = {
    'AIコース': {'Aさん', 'Cさん', 'Dさん'},
    'Railsコース': {'Bさん', 'Cさん', 'Eさん'},
    'Railsチュートリアルコース': {'Gさん', 'Fさん', 'Eさん'},
    'JS': {'Aさん', 'Gさん', 'Hさん'},
}


def find_person(want_to_find_person):
    """
    受講生がどのコースに在籍しているかを出力する。
    まずはフローチャートを書いて、どのようにアルゴリズムを解いていくか考えてみましょう。
    """
    # ここにコードを書いてみる
    for (course, person) in zip(course_dict.keys(), course_dict.values()):
        # print(course, person)
        # AIコース {'Cさん', 'Dさん', 'Aさん'}
        # Railsコース {'Cさん', 'Bさん', 'Eさん'}
        # Railsチュートリアルコース {'Gさん', 'Eさん', 'Fさん'}
        # JS {'Gさん', 'Aさん', 'Hさん'}

        # ２）want_to_find_personと、course_dictのバリュー
        matching_results = want_to_find_person & person
        # ２）ー１）want_to_find_personと、course_dictのバリューの積から誰も入っていない場合
        #  ただし、この参照するバリューはwant_to_find_person
        if len(matching_results) == 0:
            print(str(course) + "に{}".format(want_to_find_person) + "は在籍していません。")
        # ２）ー２）want_to_find_personと、course_dictのバリューの積から1人当たった場合
        elif len(matching_results) == 1:
            print(str(course) + "に{}".format(matching_results) + "のみ存在しています。")
        # ２）ー３）want_to_find_personと、course_dictのバリューの積から2人以上当たった場合
        else:
            print(str(course) + "に{}".format(matching_results) + "は在籍しています。")

def main():
    want_to_find_person = {'Cさん', 'Aさん'}
    print('探したい人: {}'.format(want_to_find_person))
    find_person(want_to_find_person)


if __name__ == '__main__':
    main()
