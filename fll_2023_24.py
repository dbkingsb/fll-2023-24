from pybricks.tools import hub_menu

# Choose a letter.
selected = hub_menu("A", "B", "C")

# Based on the selection, run a program.
if selected == "A":
    import run_example_1
elif selected == "B":
    import example_run_2
elif selected == "C":
    import example_run_2
