import eel
from __room_data__ import generate_Dummy_Room_Data


@eel.expose
def runSimulator(user_id: str ,lis : list):
    while True:
        generate_Dummy_Room_Data(user_id, lis);

    # return True
