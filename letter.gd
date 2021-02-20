extends Node2D



func _ready():
#	#hides label scroll bar
#	$text_box.get_child(0).modulate.a = 0
	set_text("M")


func set_text(new_text):
	$text_box.bbcode_text = "[center]" + new_text + "[/center]"
