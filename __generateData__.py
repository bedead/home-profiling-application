import eel
# import time
# import threading
from __insertData__ import insert_Many_into_Monitor
from __room_data__ import generate_Dummy_Room_Data


Room_Data = []
running_flag = False


def generateThread(user_id : str, user_type : str, selected_list: list):
    while running_flag:
        data = generate_Dummy_Room_Data(user_id, selected_list);
        Room_Data.extend(data)

        print(Room_Data)
            
        # insert_Many_into_Monitor(Room_Data, user_type)
        Room_Data.clear()

        print("Post complete.")
        eel.sleep(5)

@eel.expose
def runSimulator(user_id: str ,user_type: str ,selected_list : list):
    global running_flag
    if (running_flag):
        print("Generator already running.")

        return "Already running"
    else:
        running_flag = True
        eel.spawn(generateThread(user_id, user_type, selected_list))

        return "Started"

    # new_thread = threading.Thread(target=generateThread(user_id, user_type, selected_list))
    # new_thread.start()

@eel.expose
def stopSimulator():
    global running_flag
    if (running_flag):
        running_flag = False
        print("Generator Thread stopped.")

        return "Stopped"
    else:
        print("Thread is not running.")

        return "Not running"

@eel.expose
def isThreadRunning():
    return running_flag