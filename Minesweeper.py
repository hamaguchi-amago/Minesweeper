from flask import Flask, render_template
import random

def create_cell():
	BOMB_NUMBER = 10
	cell =  [['' for i in range(9)] for j in range(9)]
	
	# 爆弾をランダムに配置
	index = 0
	while index <= BOMB_NUMBER:
		row = random.randint(0, 8)
		col = random.randint(0, 8)
		value = cell[row][col]
		if	value != 'B':
			cell[row][col] = 'B'
			index += 1
	return cell

app = Flask(__name__)

@app.route("/")
def hello():
	cell = create_cell()
	return render_template("index.html", cell = cell)

if __name__ == "__main__":
	app.run( debug = True )