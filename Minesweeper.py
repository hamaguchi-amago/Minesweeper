from flask import Flask, render_template
from enum import IntEnum
import random

class Vertical(IntEnum):
    TOP = 1
    CENTER = 2
    BOTTOM = 3

class Horizontal(IntEnum):
    LEFT = 1
    CENTER = 2
    RIGHT = 3

def set_bomb():
	BOMB_NUMBER = 10
	cell =  [['' for i in range(9)] for j in range(9)]
	
	# 爆弾をランダムに配置
	index = 0
	while index < BOMB_NUMBER:
		row = random.randint(0, 8)
		col = random.randint(0, 8)
		value = cell[row][col]
		if	value != 'B':
			cell[row][col] = 'B'
			index += 1

	return cell

def check_value(cell, i, j, count , vertical ,horizontal):
    if (vertical == Vertical.TOP and i == 0) or \
       (vertical == Vertical.BOTTOM and i == 8) or \
       (horizontal == Horizontal.LEFT and j == 0) or \
       (horizontal == Horizontal.RIGHT and j == 8):
    	return count
    
    print("vertical" + str(vertical) +" horizontal" + str(horizontal))
    
    row = 0
    if vertical == Vertical.TOP:
    	row = i - 1 
    elif vertical == Vertical.CENTER:
    	row = i
    else:
    	row = i + 1
    
    col = 0
    if horizontal == Horizontal.LEFT:
    	col = j - 1 
    elif horizontal == Horizontal.CENTER:
    	col = j
    else:
    	col = j + 1

    if cell[row][col] == 'B':
    	count += 1
    return count

def set_value(cell, i, j):
	if cell[i][j] == 'B':
		return cell[i][j]
	else:
		bomb_count = 0
		for vertical in [1, 2, 3]:
			for horizontal in [1, 2, 3]:
				if vertical == Vertical.CENTER and horizontal == Horizontal.CENTER:
					continue
				bomb_count = check_value(cell, i, j, bomb_count, vertical, horizontal )
		return bomb_count

def set_number(cell):
	for i, row in enumerate(cell):
		for j, col in enumerate(row):
			cell[i][j] = set_value(cell, i ,j)

	return cell

def create_cell():
	return set_number(set_bomb())

app = Flask(__name__)

@app.route("/")
def index():
	cell = create_cell()
	return render_template("index.html", cell = cell)

if __name__ == "__main__":
	app.run( debug = True )