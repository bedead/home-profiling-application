import time
import eel

# import time
# import threading
from __insertData__ import insert_Many_into_Monitor
from __room_data__ import generate_Dummy_Room_Data


Room_Data = []
running_flag = False


def generateThread(user_id: str, user_type: str, selected_list: list, time_sec):
    global running_flag
    while running_flag and (time.time() < time_sec):
        data = generate_Dummy_Room_Data(user_id, selected_list)
        Room_Data.extend(data)
        print(Room_Data)
        insert_Many_into_Monitor(Room_Data, user_type)
        Room_Data.clear()

        eel.sleep(10)

    running_flag = False


@eel.expose
def runSimulator(user_id: str, user_type: str, selected_list: list, run_hour, run_min):
    global running_flag
    if running_flag:
        print("Generator already running.")

        return "Already running"
    else:
        t_end = time.time() + (run_hour * 3600) + (run_min * 60)
        if round(t_end) <= round(time.time()):
            return "Set time"
        else:
            running_flag = True

            eel.spawn(generateThread(user_id, user_type, selected_list, time_sec=t_end))

            return "Simulation Completed."


@eel.expose
def stopSimulator():
    global running_flag
    if running_flag:
        running_flag = False
        print("Generator Thread stopped.")

        return "Stopped"
    else:
        print("Thread is not running.")

        return "Not running"


@eel.expose
def isThreadRunning():
    return running_flag
