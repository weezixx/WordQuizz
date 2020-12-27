extends Node

#var path = "res://words.json"
#
#var file = File.new()
#
#var item_data
#
#func _ready():
#	var itemdata_file = File.new()
#	itemdata_file.open(path, File.READ)
#	var itemdata_json = JSON.parse(itemdata_file.get_as_text())
#	itemdata_file.close()
#	item_data = itemdata_json.result
#	print(item_data)

const SQLite = preload("res://addons/godot-sqlite/bin/gdsqlite.gdns")

var db_name = "res://bdd.db"

var result

func _ready():
	
	var db = SQLite.new();
	db.path = db_name
	
	db.open_db(db_name)
	
	result = db.query("SELECT * FROM words WHERE trials = 0 ORDER BY RANDOM() LIMIT 1;")
	
	for i in db.query_result:
		print(i)
		print(i.FR)
		print(i.NL)


	
	
	
