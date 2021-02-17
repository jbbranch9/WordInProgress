extends Node2D

func _input(event):
	if event.is_action_pressed("exit_game"):
		get_tree().quit()

func _ready():
	OS.center_window()
	

