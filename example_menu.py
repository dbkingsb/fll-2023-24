from pybricks.tools import hub_menu

# Choose a letter.
selected = hub_menu("F", "D", "Z")

# Based on the selection, run a program.
if selected == "F":
    import example_run_1
elif selected == "D":
    import example_run_2
elif selected == "Z":
    import example_run_3