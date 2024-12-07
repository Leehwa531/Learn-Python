import time
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd
import math
import sympy as sym
from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement
import datetime
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

def time_check(): #수행시간 확인 함수입니다. 내용 수정하지 말아주세요
    print("중간고사 시험 수행 인증시간:", "%s년 %s월 %s일 %s시 %s분" %(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day,datetime.datetime.now().hour,datetime.datetime.now().minute))

#미로찾기 함수입니다. 내용 수정하지 말아주세요.
def my_maze(maze, start, end):
    qu = []
    done = set()
    qu.append(start)
    done.add(start)

    print("시작")
    while qu:
        p = qu.pop(0)
        v = p[-1]
        
        if v == end:
            print("종료")
            return p

        for x in maze[v]:
            if x not in done:
                qu.append(p+x)
                done.add(x)



def exam_1():
    print("문제1번")
    #코딩은 여기부터 시작해주세요
    x = list(range(-10, 11))
    y1 = [2 * xi for xi in x]
    y2 = [xi / 2 for xi in x]

    plt.plot(x, y1, label='y=2x')
    plt.plot(x, y2, label='y=x/2')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Graph of y=2x and y=x/2')
    plt.legend()
    plt.grid()
    plt.show()

    #수행시간 확인 함수입니다. 함수 호출을 지우지 말아주세요
    time_check()

def exam_2():
    print("문제2번")
    #코딩은 여기부터 시작해주세요
    x = np.linspace(0, 10 * np.pi, 500)
    a = (x + 1) ** 2
    b = 2 * (x + 1)

    plt.figure(figsize=(12, 8))
    plt.subplot(3, 1, 1)
    plt.plot(x, np.sin(a), label='sin(a)')
    plt.legend()
    plt.subplot(3, 1, 2)
    plt.plot(x, np.cos(b), label='cos(b)')
    plt.legend()
    plt.subplot(3, 1, 3)
    plt.plot(x, np.sin(a + b), label='sin(a+b)')
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    #수행시간 확인 함수입니다. 함수 호출을 지우지 말아주세요
    time_check()

def exam_3():
    print("문제3번")
    #코딩은 여기부터 시작해주세요
    num = int(input("숫자를 입력하세요: "))
    A = set(range(1, num + 1, 2))
    B = set(range(3, num + 1, 3))
    C = set([2 ** i for i in range(num) if 2 ** i <= num])

    cartesian_product = set(product(B, C))
    print("A:", A)
    print("B:", B)
    print("C:", C)
    print("B x C:", cartesian_product)

    #수행시간 확인 함수입니다. 함수 호출을 지우지 말아주세요
    time_check()
    
def exam_4():
    print("문제4번")
    #코딩은 여기부터 시작해주세요
    total = 200000
    non_carriers = 184340
    carriers = 15660

    pos_non_carriers = 14250
    neg_carriers = 1120

    p_pos_given_non_carrier = pos_non_carriers / non_carriers
    p_neg_given_carrier = neg_carriers / carriers

    print(f"(1) A균 미보균자가 양성일 확률: {p_pos_given_non_carrier:.4f}")
    print(f"(2) A균 보균자가 음성일 확률: {p_neg_given_carrier:.4f}")

    #수행시간 확인 함수입니다. 함수 호출을 지우지 말아주세요
    time_check()
    
def exam_5():
    print("문제5번")
    #코딩은 여기부터 시작해주세요
    A = np.array([[1, -1, 2], [2, 1, -3], [4, 1, 1]])
    B = np.array([[3, -1, -2], [-4, 2, 1], [1, 4, -3]])

    AB_sum = A + B
    AB_product_transpose = np.dot(A, B).T
    AB_inverse = np.linalg.inv(np.dot(A, B))

    print("A + B:\n", AB_sum)
    print("(A x B)^T:\n", AB_product_transpose)
    print("(A x B)^(-1):\n", AB_inverse)

    #수행시간 확인 함수입니다. 함수 호출을 지우지 말아주세요
    time_check()


def final_exam(): #기말고사 문제 메뉴 입니다
    
    exam_1()
    exam_2()
    exam_3()
    exam_4()
    exam_5()
    
final_exam()
    
    
