new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

# Переносим элемент task_005 из списка new_tasks в completed_tasks
completed_tasks.append(new_tasks.pop())

# Удаляем элемент task_007 из списка new_tasks
new_tasks.remove('task_007')

# Выводим на экран последний элемент из списка new_tasks
print(new_tasks[-1])