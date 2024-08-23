def apply_styles(widget):
    # Налаштування кольорів, шрифтів і відступів для загального стилю
    widget.configure(bg="#f0f0f0")
    widget.option_add("*Font", "Arial 10")
    widget.option_add("*Button.Font", "Arial 10 bold")
    widget.option_add("*Button.Background", "#4CAF50")
    widget.option_add("*Button.Foreground", "#ffffff")
    widget.option_add("*Label.Font", "Arial 12 bold")
    widget.option_add("*Checkbutton.Font", "Arial 10")
    widget.option_add("*Checkbutton.Background", "#f0f0f0")
    widget.option_add("*Checkbutton.Foreground", "#333333")
