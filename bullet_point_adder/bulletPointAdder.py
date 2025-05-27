import pyperclip

text = pyperclip.paste()


# Separate lines and add stars.
def takeTextAndMakeBulletLineByLine(text) -> str:
    lines = text.split("\n")
    for i in range(len(lines)):
        lines[i] = "* " + lines[i]

    output = "\n".join(lines)
    return output


pyperclip.copy(takeTextAndMakeBulletLineByLine(text))
