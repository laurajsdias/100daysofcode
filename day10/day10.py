# Functions with Outputs

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    print(f"{formated_f_name} {formated_l_name}")

format_name("laura", "DIAS")

# Another way to output with return:

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("laura", "DIAS")
print(formated_string)


