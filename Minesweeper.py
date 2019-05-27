from flask import Flask, render_template
import random

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

def set_value(cell, i, j):
	if cell[i][j] == 'B':
		return cell[i][j]
	else:
		bomb_count = 0
		#左上のチェック
		if i != 0 and j != 0:
			if cell[i - 1][j - 1] == 'B':
				bomb_count += 1
		#上のチェック
		if i != 0:
			if cell[i - 1][j] == 'B':
				bomb_count += 1
		#右上のチェック
		if i != 0 and j != 8:
			if cell[i - 1][j + 1] == 'B':
				bomb_count += 1
		#左のチェック
		if j != 0:
			if cell[i][j - 1] == 'B':
				bomb_count += 1
		#右のチェック
		if j != 8:
			if cell[i][j + 1] == 'B':
				bomb_count += 1
		#左下のチェック
		if i != 8 and j != 0:
			if cell[i + 1][j - 1] == 'B':
				bomb_count += 1
		#上のチェック
		if i != 8:
			if cell[i + 1][j] == 'B':
				bomb_count += 1
		#右上のチェック
		if i != 8 and j != 8:
			if cell[i + 1][j + 1] == 'B':
				bomb_count += 1
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
def hello():
	cell = create_cell()
	return render_template("index.html", cell = cell)

if __name__ == "__main__":
	app.run( debug = True )