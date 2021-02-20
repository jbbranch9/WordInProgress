extends Node2D

const press = preload("res://ASSETS/UI/PNG/buttonSquare_grey_pressed.png")
const release = preload("res://ASSETS/UI/PNG/buttonSquare_grey.png")

var ltr_color = Color.black
var btn_color = Color.beige


onready var btn = $button
onready var ltr = $button/letter

func _input(event):
	name = event.as_text()
	if name in Alphabet.UPPER and len(name) == 1 and Input.is_action_pressed("letterbox_pressed"):
		ltr.set_text(name)

func _process(delta):
	if Input.is_action_just_pressed("letterbox_pressed"):
		btn.texture = press
		ltr.position += Vector2(0,2)
	elif Input.is_action_just_released("letterbox_pressed"):
		btn.texture = release
		ltr.position -= Vector2(0,2)


func _ready():
	ltr.modulate = ltr_color
	btn.modulate = btn_color
