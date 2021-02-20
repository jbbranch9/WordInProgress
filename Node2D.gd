extends Node2D

const press = preload("res://ASSETS/buttonSquare_grey_pressed.png")
const release = preload("res://ASSETS/buttonSquare_grey.png")

func _process(delta):
	if Input.is_action_pressed("pressed"):
		$Sprite.texture = press
		$Sprite.modulate = Color.coral
	else:
		$Sprite.texture = release

