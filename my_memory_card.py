from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QGroupBox,QButtonGroup
from random import shuffle, randint
app = QApplication([])
main_win = QWidget()
main_win.resize(600,300)

class Question():
    def __init__(self, question, right_k1, n_k2, n_k3, n_k4):
        self.question = question
        self.right_k1 = right_k1
        self.n_k2 = n_k2
        self.n_k3 = n_k3
        self.n_k4 = n_k4

spisok = []

spisok.append(Question('сколько нужно сочель на 1 деревянную дверь?', '2', '3', '6', '4'))
spisok.append(Question('сколько сочелей нужно на 1 каменную стену?','10','5','4','2'))
spisok.append(Question('1 из варинтов того, как можно сбить коптер','тут нет правильно ответа','с4','сочель','ракетой'))
spisok.append(Question('какой корпус нужен для крафта калаша','винтовки','пистолета-пулемёта','полуавтомотической винтовки','никакой'))
spisok.append(Question('чем обычно взрывают танк на космодроме?','ракетами','пзрк','минами','гранатами'))
spisok.append(Question('какие карты можно использовать на большой нефтевышке?','все','только красную','только синюю','только зелёную'))
spisok.append(Question('за сколько скрапа продается коптер в городе?','750','900','1200','500'))
spisok.append(Question('с какого оружия можно стрелять в воде?','гарпун','мп5','калаш','в воде нельзя стрелять вообще'))
spisok.append(Question('сколько сиденей в коптере?','2','5','3','1'))


vopr = QLabel('какой национальности не существет?')
otv  = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответов')
k1 = QRadioButton('1')
k2 = QRadioButton('2')
k3 = QRadioButton('3')
k4 = QRadioButton('4')
layout_1 = QHBoxLayout()
layout_2 = QVBoxLayout()
layout_3 = QVBoxLayout()

layout_2.addWidget(k1)
layout_2.addWidget(k2)
layout_3.addWidget(k3)
layout_3.addWidget(k4)
RadioGroup = QButtonGroup()
RadioGroup.addButton(k1)
RadioGroup.addButton(k2)
RadioGroup.addButton(k3)
RadioGroup.addButton(k4)
layout_1.addLayout(layout_2)
layout_1.addLayout(layout_3)

RadioGroupBox.setLayout(layout_1)




layout1 = QVBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()
layout4 = QHBoxLayout()

layout2.addWidget(vopr)
layout3.addWidget(RadioGroupBox)
layout4.addWidget(otv)
layout1.addLayout(layout2)
layout1.addLayout(layout3)
layout1.addLayout(layout4)

main_win.setLayout(layout1)



ResultBox = QGroupBox('Результат теста')
pravil_otv = QLabel('Правильно/Неправильно')
otvet2 = QLabel('Правильный ответ')
layout_otv1 = QVBoxLayout()
layout_otv2 = QHBoxLayout()
layout_otv3 = QHBoxLayout()



layout_otv2.addWidget(pravil_otv)
layout_otv3.addWidget(otvet2)
layout_otv1.addLayout(layout_otv2)
layout_otv1.addLayout(layout_otv3)
ResultBox.setLayout(layout_otv1)
layout3.addWidget(ResultBox)
ResultBox.hide()


def show_result():
    RadioGroupBox.hide()
    ResultBox.show()
    otv.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    ResultBox.hide()
    otv.setText('Ответить')
    RadioGroup.setExclusive(False)
    k1.setChecked(False)
    k2.setChecked(False)
    k3.setChecked(False)
    k4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [k1, k2, k3, k4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_k1)
    answers[1].setText(q.n_k2)
    answers[2].setText(q.n_k3)
    answers[3].setText(q.n_k4)
    otvet2.setText(q.right_k1)
    vopr.setText(q.question)
    show_question()

def show_correct(set_text):
    pravil_otv.setText(set_text)
    show_result()

main_win.total = 0
main_win.vern = 0


def chek_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.vern += 1
        print('Статистика\n-Всего вопросов: ',main_win.total,'\n-Правильных ответов: ',main_win.vern)
        print('Рейтинг: ',main_win.vern/main_win.total*100,'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно')
            print('Статистика\n-Всего вопросов: ',main_win.total,'\n-Правильных ответов: ',main_win.vern)
        print('Рейтинг: ',main_win.vern/main_win.total*100,'%')
    






def next_question():
    main_win.cur_question += 1
    if main_win.cur_question >= len(spisok):
        main_win.cur_question = 0
    cur_question = randint(0, len(spisok)-1)
    q = spisok[cur_question]
    ask(q)
    main_win.total += 1
    print('Статистика\n-Всего вопросов: ',main_win.total,'\n-Правильных ответов: ',main_win.vern)
    

    

def click_ok():
    if otv.text() == 'Ответить':
        chek_answer()
    else:
        next_question()
        



main_win.setWindowTitle('Memo Card')
main_win.cur_question = -1
otv.clicked.connect(click_ok)
next_question()










main_win.show()
app.exec_()









