from celery import shared_task

@shared_task(bind=True)
def test_func(self):
    #operations
    for i in range(9):
        print(i)
    return 'Done Prints'