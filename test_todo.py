from todo import add_task, delete_task, complete_task

def test_add_task():
    tasks = []
    add_task(tasks, "Test")
    assert len(tasks) == 1

def test_complete_task():
    tasks = [{"title": "Test", "done": False}]
    complete_task(tasks, 0)
    assert tasks[0]["done"] == True

def test_delete_task():
    tasks = [{"title": "Test", "done": False}]
    delete_task(tasks, 0)
    assert len(tasks) == 0