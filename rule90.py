import cv2
import numpy as np

AtoW = [0] * 23
print(AtoW)

count = 50

def nextstep(cells,rule_pattern):
    next_cells = []
    for time,cell in enumerate(cells):
        if time == 0: #左端の場合
            next_cells.append(rule(rule_pattern,cells[-1],cells[time],cells[time+1]))
        elif time == 22: #右端の場合
            next_cells.append(rule(rule_pattern,cells[time-1],cells[time],cells[0]))
        else: #その他
            next_cells.append(rule(rule_pattern,cells[time-1],cells[time],cells[time+1]))
    return next_cells

def rule(rule_name,l_cell,c_cell,r_cell):
    if rule_name == 90:
        if l_cell == 1 and c_cell == 1 and r_cell == 0:
            return 1
        elif l_cell == 0 and c_cell == 1 and r_cell == 1:
            return 1
        elif l_cell == 1 and c_cell == 0 and r_cell == 0:
            return 1
        elif l_cell == 0 and c_cell == 0 and r_cell == 1:
            return 1
        elif l_cell == 1 and c_cell == 1 and r_cell == 1:
            return 0
        elif l_cell == 0 and c_cell == 0 and r_cell == 0:
            return 0
        elif l_cell == 1 and c_cell == 0 and r_cell == 1:
            return 0
        elif l_cell == 0 and c_cell == 1 and r_cell == 0:
            return 0
    
    if rule_name == 193:
        if l_cell == 1 and c_cell == 1 and r_cell == 1:
            return 1
        elif l_cell == 1 and c_cell == 1 and r_cell == 0:
            return 1
        elif l_cell == 1 and c_cell == 0 and r_cell == 1:
            return 0
        elif l_cell == 1 and c_cell == 0 and r_cell == 0:
            return 0
        elif l_cell == 0 and c_cell == 1 and r_cell == 1:
            return 0
        elif l_cell == 0 and c_cell == 1 and r_cell == 0:
            return 0
        elif l_cell == 0 and c_cell == 0 and r_cell == 1:
            return 0
        elif l_cell == 0 and c_cell == 0 and r_cell == 0:
            return 1


def print_cells(cells):
    return_text = ""
    for item in cells:
        if item == 0:
            return_text += "■"
        elif item == 1:
            return_text += "□"
    print(return_text)

def create_list_for_image(lists):
    return_lists = []
    for line in lists:
        tmp_line = []
        for i in line:
            if i == 0:
                tmp_line.append([255,255,255])
            if i == 1:
                tmp_line.append([0,0,0])
        return_lists.append(tmp_line)
    return return_lists

tmp_cells = [0] * 23
tmp_cells[11] = 1 #初期設定

print("rule90")
rule90_lists = []
for _ in range(count):
    #print_cells(tmp_cells)
    rule90_lists.append(tmp_cells)
    tmp_cells = nextstep(tmp_cells,90)
    

cv2.imwrite('rule90.png',np.array(create_list_for_image(rule90_lists)))

print("rule193")
tmp_cells = [0] * 23
tmp_cells[11] = 1 #初期設定
rule193_lists = []
for _ in range(count):
    
    #print_cells(tmp_cells)
    rule193_lists.append(tmp_cells)
    tmp_cells = nextstep(tmp_cells,193)
    


cv2.imwrite('rule193.png',np.array(create_list_for_image(rule193_lists)))





