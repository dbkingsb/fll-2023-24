from pybricks.tools import hub_menu

# Choose a letter.
selected = hub_menu("A", "B", "C", "D", "E", "F", "G")

# Based on the selection, run a program.
if selected == "A":
    import run_westside_lift
elif selected == "B":
    import run_east_side_push
elif selected == "C":
    import run_emily
elif selected == "D":
    import run_Oliver
elif selected == "E":
    import run_rolly_banna_elin
elif selected == "F":
    import KFC
elif selected == "G":
    import KFC_2

