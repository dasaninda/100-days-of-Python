guess_states = []
# all_state = data.state.to_list()


# while len(guess_states) <50:
#     answer_state = screen.textinput(title = f"{len(guess_states)}/50 States Correct", prompt= "State Name?" ).title()
   
#     if answer_state == "Exit":
#         missing_states = []
#         for state in all_state:
#             if state not in guess_states:
#                 missing_states.append(state)    
       
#         break
#     if answer_state in all_state:
#         if answer_state not in guess_states:
#             state_data = data[data.state == answer_state]
#             x_axis, y_axis = int(state_data.x), int(state_data.y)
#             t.goto(x_axis, y_axis)
#             t.write (answer_state)