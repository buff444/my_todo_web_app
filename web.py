import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    functions.write_todos(todos)
    st.session_state['new_todo'] = ""



st.title("my Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()
        print(checkbox)


st.text_input(label="Add Todo",
              placeholder="Add new todo",
              on_change=add_todo,
              key='new_todo')


