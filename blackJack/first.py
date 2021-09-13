from abc import abstractproperty
import random
import im_Card


    
#카드 52장 생성    
card_list = []
shape_list = ["★", "♥", "♠", "♣"]
for i in range(4):
    card_list.append(im_Card.Card("{}".format(shape_list[i]),"A",1, 11, True))        #A는 1과 11의 가치를 갖음
    for j in range(2,11):
        card_list.append(im_Card.Card("{}".format(shape_list[i]), str(j), j, j, True))
    card_list.append(im_Card.Card("{}".format(shape_list[i]), "J",10, 10, True))
    card_list.append(im_Card.Card("{}".format(shape_list[i]), "Q",10, 10, True))
    card_list.append(im_Card.Card("{}".format(shape_list[i]), "K",10, 10, True))


#카드 뽑기
def select_card():
    random_number = random.randrange(len(card_list))
    get_card = card_list[random_number]
    del(card_list[random_number])

    return get_card
#카드 보여주기()
def show_card(my_list): 
    for i in range(len(my_list)):
        if my_list[i].status == True:                       #숨김 상태의 카드는
            print("?")                                      #?로 표시하고
        else:
            target = my_list[i].shape +" "+ my_list[i].name     #공개 상태의 카드는
            print(str(target))                              #그 값을 표시한다.
def get_card(): 
    print("추가적으로 카드를 지급받겠습니까?")
    print("동의하신다면 Y키를 입력하십시오.")
    print("그렇지 않다면 다른 키를 입력하십시오.")
    target = input()
    if target == 'Y':
        print("카드를 추가 지급합니다.")
        return select_card()
    elif target == 'y':
        print("카드를 추가 지급합니다.")
        return select_card()    
    else:
        print("카드지급을 종료합니다.")
        return 'False'

def judge_winner(diller_sum, player_value):
    #0은 딜러승리, 1은 플레이어 승리, 2는 무승부 의미
    answer = 0
    if diller_sum >21:
        answer = 1
    else:
        diller_point = abs(diller_sum - 21)
        player_value
        if diller_point < player_value:
            answer = 0
        elif diller_point == player_value:
            answer = 2
        else:
            answer = 1
    return answer
#카드의 값을 더하는 함수(딜러)
def sum_of_diller_cards(list):
    answer = 0
    for i in range(len(list)):
        answer += list[i].value1
    
    return answer

def make_binary_list(number):
    square = 2 ** number
    list_con_num = []
    for i in range(square):
        list_con_num.append(i)
    binary_list = [str(bin(x))[2:].zfill(number) for x in list_con_num]

    return binary_list
def sum_of_player_cards(list):
    count_list = len(list)
    binary_list = make_binary_list(len(list))
    answer_list = []
    copy_answer_list = []

    for i in range(len(binary_list)):
        print(binary_list[i], end="=>")
        sum = 0
        for j in range(len(list)):
            target = int(binary_list[i][j])
            sum += list[j].value_list[target]
        answer_list.append(sum)

    for i in range(len(binary_list)):
        copy_answer_list.append(abs(answer_list[i] - 21))
    target = min(copy_answer_list)
    return target
        





while True:
    print("*******게임*시작********")
    my_cards = []
    diller_cards = []

    #딜러가 카드를 먼저 받음
    diller_cards.append(     select_card()    )
    diller_cards.append(     select_card()    )
    diller_cards[0].open_card()
    #딜러는 카드의 합이 17이 될때까지 
    # 카드를 계속해서 지급받음
    while True:
        diller_sum = sum_of_diller_cards(diller_cards)       
        if diller_sum >17:
            break
        else :
            diller_cards.append(select_card())


    print("딜러의 카드 목록")
    show_card(diller_cards)



    #사용자
    #카드를 두 장 지급
    print("**************************")
    print("첫 카드 두장을 지급받습니다")
    my_cards.append(  select_card()  )
    my_cards.append(  select_card()  )
    
    #카드 공개
    for i in range(len(my_cards)):
        my_cards[i].open_card()
    show_card(my_cards)    
    while True:         
        target = get_card()
        if target == 'False':
            break
        else:
            target.open_card()
            my_cards.append(target)
            show_card(my_cards)

    player_sum = sum_of_player_cards(my_cards)

    print("**************************")
    #딜러 카드를 모두 공개하고 승패를 판정함.
    for i in range(len(diller_cards)):
        diller_cards[i].open_card()
    show_card(diller_cards)


    #0은 딜러승리, 1은 플레이어 승리, 2는 무승부 의미   
    judged_number = judge_winner(diller_sum, player_sum)
    if judged_number == 0:
        print("딜러의 승리")
    elif judged_number == 1:
        print("플레이어의 승리")
    else:
        print("무승부")



    print("*****게임종료")

    
    break
    
#########GOOD

###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
#  블랙잭 규칙
# 플레이어는 2장의 카드를 지급받고, 모두 오픈합니다.
# 딜러는 두 장의 카드를 받고 한장은 오픈, 한장은 하이드합니다.

# 플레이어는 본인의 패와 딜러의 카드 한장을 본 후,
# 카드를 더 받을지(히트), 그만받을지(스탠드) 선택합니다.

# 모든 플레이어가 스탠드를 하면 딜러의 카드를 오픈합니다.

# 딜러는 딜러의 카드 합이 17이 될 때까지 카드를 반드시 받으며
# 21이 넘으면 버스트되어 플레이어가 승리합니다.

# 딜러의 카드의 합이 버스트가 나지 않은 경우
# 딜러와 플레이어의 카드의 합을 비교해 21에 가까운 쪽이 승리합니다.
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
#카드의 가치
# 2~9는 숫자 그대로의 값을 갖습니다.
# 10,J,Q,K는 10을 의미합니다.
# A는 1 혹은 11로 플레이어가 선택합니다.
# 단, 딜러의 A카드는 11을 의미합니다
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################



