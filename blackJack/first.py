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
    del(card_list[i])

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

#카드의 값을 더하는 함수
def sum_of_cards(list):
    answer = 0
    for i in range(len(list)):
        answer += list[i].value1
    
    return answer

while True:
    print("*******게임*시작********")
    my_cards = []
    diller_cards = []


    #딜러가 카드를 먼저 받음
    diller_cards.append(     select_card()    )
    diller_cards.append(     select_card()    )
    diller_cards[0].open_card()
    print("딜러의 카드 목록")
    show_card(diller_cards)
    #사용자
    #카드를 두 장 지급
    my_cards.append(  select_card()  )

    my_cards.append(  select_card()  )
    
    #카드 공개
    print("**************************")
    print("첫 카드 두장을 지급받습니다")
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



    #딜러 카드를 모두 공개하고 승패를 판정함.
    print(sum_of_cards(diller_cards))
    print("*****게임종료")

    
    break
    


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



