import FreeSimpleGUI as sg

sg.theme("Black")

label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="ft")

label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="in")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output", text_color="white")
exit_button = sg.Button("Exit")

layout = [[label1, input1],
          [label2, input2],
          [convert_button, exit_button, output_label]]

window = sg.Window("Convertor", layout)
while True:
    try:
        event, values = window.read()
        ans1 = float(values["ft"])
        ans2 = float(values["in"])
        def ft2inches(ans1):
            return ans1 * 12
        result = ft2inches(ans1) + ans2
        def inches2meters(result):
            return result * 0.0254
        result2 = f"{inches2meters(result)} m"
        match event:
            case "Convert":
                window["output"].update(value=result2)

            case "Exit":
                break
            case sg.WIN_CLOSED:
                break
    except ValueError:
        if event == "Convert":
            sg.popup("Please enter numbers in the input boxes!", font=("Helvetica", 10), text_color="red")
        else:
            break
    except TypeError:
        break
window.close()