from prefect import flow

@flow(log_prints=True)
def buy():
    print("COMPRADOOOOOO 222")