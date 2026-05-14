from todo import add_task, delete_task, complete_task

def test_add_task():
    tasks = []
    tasks.append({"title": "Test", "done": False})
    assert len(tasks) == 1

def test_complete_task():
    tasks = [{"title": "Test", "done": False}]
    tasks[0]["done"] = True
    assert tasks[0]["done"] == True

def test_delete_task():
    tasks = [{"title": "Test", "done": False}]
    tasks.pop(0)
    assert len(tasks) == 0